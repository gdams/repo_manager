# Eclipse Repo Organiser

Each directory (based on the top level project) contains a `repositories.yml` file which contains the set of repositories to maintain.

## Configuration

There are several parameters available for each repository configuration:

|Parameter|Description|Default|Required|
|---|---|---|---|
|`name`| Repository Name |n/a |yes|
|`description`|Repository Description|n/a|yes|
|`homepage`|Repository Website URL|n/a|no|
|`private`|Create a Private Repository|`False`|No|
|`has_issues`|Enable GitHub Issues|`True`|No|
|`has_wiki`| Enable GitHub Wiki|`True`|No|
|`has_downloads`| Enable GitHub Downloads|`True`|No|
|`has_projects`| Enable GitHub Projects Board|`True`| No|
|`allow_merge_commit` | Enable merge commits| `True`| No |
|`allow_squash_merge` | Enable squash merging| `True`| No |
|`allow_rebase_merge` | Enable rebase merging| `True`| No |
|`delete_branch_on_merge`| Automatically delete branches on Merge | `False`| No |

### Branch protection configuration

|Parameter|Description|Default|Required|
|---|---|---|---|
|`branch`| Name of Branch to protect | n/a |yes|
|`dismiss_stale_reviews`| Dismiss Stale Reviews | `False` | No |
|`required_approving_review_count`| Number of required reviewers | `0` | No |
|`require_code_owner_reviews`| Require an approved review from code owner |
|`enforce_admins`| Enforce same rules for Admins | `False` | No |
|`dismissal_users` | Users that are allowed to dismiss reviews | n/a | No |
|`dismissal_teams` | Teams that are allowed to dismiss reviews | n/a | No |


### Sample `repositories.yml` file

```yml
repositories:
  - name: test-repo
    description: Test repository
    homepage: https://example.com
    has_wiki: false
    allow_merge_commit: false
    delete_branch_on_merge: true
    branch_protection:
      branch: 'main'
      required_approving_review_count: 2

  - name: test-repo2
    description: Test repository2
    allow_squash_merge: false
    has_wiki: false
    has_issues: false
    has_projects: false
```

## Running locally

Install prerequisites

```bash
pip install -r requirements.txt
```

Run the updater

```bash
export GITHUB_TOKEN=<github_personal_access_token>
python repo.py
```