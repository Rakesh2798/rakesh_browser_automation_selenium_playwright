# Playwright Teams Automation

This project uses Playwright and pytest for Microsoft Teams browser checks. Its page objects, locators, and tests are kept in this folder.

## Setup

From the repository root, install the shared dependencies and Chromium:

```powershell
python -m pip install -r requirements.txt
playwright install chromium
```

## Run

From the repository root:

```powershell
python -m pytest "Playwright/Microsoft teams/tests/" -v -s
```

The `-s` option displays the interactive sign-in prompts. The current setup signs in, navigates Teams, then opens and saves a meeting.
