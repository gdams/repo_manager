#!/usr/bin/env python3

from github import Github
import os
import yaml

def config_parser(repo, key, default):
    if key in repo:
        if repo[key] == default:
            return default
        else:
            return repo[key]
    else:
        return default

g = Github(os.getenv('GITHUB_TOKEN'))

user = g.get_user()

# Set GitHub organization
organization = g.get_organization("openruntime")

# Load config yaml file
f = open('adoptium/repositories.yml')
repositories = yaml.safe_load(f)

for repo in repositories['repositories']:
    try:
        repository = organization.get_repo(repo['name'])
    except:
        organization.create_repo(
            repo['name'],
            auto_init = True, # Initialize the repository with a README
        )
        repository = organization.get_repo(repo['name'])

    repository.edit(
        name = repo['name'],
        # Defaults pulled from https://docs.github.com/en/rest/repos/repos#create-an-organization-repository
        description = repo['description'],
        homepage = config_parser(repo, 'homepage', ""),
        private = config_parser(repo, 'private', False),
        has_issues = config_parser(repo, 'has_issues', True),
        has_wiki = config_parser(repo, 'has_wiki', True),
        has_downloads= config_parser(repo, 'has_downloads', True),
        has_projects = config_parser(repo, 'has_projects', True),
        allow_merge_commit = config_parser(repo, 'allow_merge_commit', True),
        allow_squash_merge = config_parser(repo, 'allow_squash_merge', True),
        allow_rebase_merge = config_parser(repo, 'allow_rebase_merge', True),
        delete_branch_on_merge = config_parser(repo, 'delete_branch_on_merge', False),
    )

    if 'branch_protection' in repo:
        branch = organization.get_repo(repo['name']).get_branch(repo['branch_protection']['branch'])
        branch.edit_protection(
            required_approving_review_count = config_parser(repo['branch_protection'], 'required_approving_review_count', 0),
            dismiss_stale_reviews = config_parser(repo['branch_protection'], 'dismiss_stale_reviews', False),
            require_code_owner_reviews = config_parser(repo['branch_protection'], 'require_code_owner_reviews', False),
            enforce_admins = config_parser(repo['branch_protection'], 'enforce_admins', False),
        )

        if 'dismissal_users' in repo['branch_protection']:
            branch.edit_protection(
                dismissal_users = config_parser(repo['branch_protection'], 'dismissal_users', [])
            )

        if 'dismissal_teams' in repo['branch_protection']:
            branch.edit_protection(
                dismissal_teams = config_parser(repo['branch_protection'], 'dismissal_teams', [])
            )

f.close()