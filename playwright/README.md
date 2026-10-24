# Playwright Automation

The Microsoft Teams Playwright project, including page objects, pytest tests, and BDD examples, is in [`microsoftteams/`](microsoftteams/README.md).

## Setup

Run from the repository root (`F:\Project\Browser`). Create and activate `.venv` first (PowerShell: `.\.venv\Scripts\Activate.ps1`; Git Bash: `source .venv/Scripts/activate`) so the commands use the project dependencies rather than a different global Python installation.

```
python -m venv .venv
```

After activating the environment, install dependencies and Chromium:

```
python -m pip install -r playwright/microsoftteams/requirements.txt
python -m playwright install chromium
```

## Run pytest tests

From the repository root:

```
python -m pytest playwright/microsoftteams/tests/ -v -s
```

Or first change to `playwright/microsoftteams`, then use the shorter project-relative path:

```
Set-Location playwright/microsoftteams
python -m pytest tests/ -v -s
```

See the [Teams project README](microsoftteams/README.md) for credentials, test behavior, and BDD commands.
