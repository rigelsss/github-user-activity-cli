# GitHub User Activity CLI

Command-line application that fetches a GitHub user's recent activity through the GitHub API and displays it in the terminal. Based on the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) project from roadmap.sh.

> Uses only the Python standard library (`urllib` and `json`). There are no external dependencies and no `requirements.txt` to install.

## Project Structure

```
github-user-activity-cli/
├── main.py         # Entry point: reads the command-line argument and handles errors
├── github_api.py   # Makes the HTTP request to the GitHub API using urllib
└── formatter.py    # Formats each event into a readable line using match/case by event type
```

## Features

- Fetches recent activity from the `https://api.github.com/users/<username>/events` endpoint
- Formats several event types:
  - Push
  - Star (watch)
  - Fork
  - Issues
  - Issue comments
  - Pull requests
  - Pull request reviews
  - Create
  - Delete
- Generic fallback for unmapped event types
- Error handling for:
  - User not found (`404`)
  - API rate limit exceeded (`403`)
  - Network failure

## Prerequisites

- Python 3.10 or higher (required for `match/case`)

## Usage

```bash
python main.py <github_username>
```

Example:

```bash
python main.py kamranahmedse
```

## Example Output

Illustrative output (actual activity will vary):

```text
Recent activity for kamranahmedse: 3 events found.
--------------------------------
Pushed to kamranahmedse/developer-roadmap on (refs/heads/main)
Starred kamranahmedse/developer-roadmap
opened issue 'Update documentation' on kamranahmedse/developer-roadmap
```