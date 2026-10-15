# Selenium Teams Automation

This project automates Microsoft Teams with Selenium WebDriver. Its page objects, locators, and runner are kept in this folder.

## Setup

From the repository root, install the shared dependencies:

```powershell
python -m pip install -r requirements.txt
```

Selenium Manager obtains the matching ChromeDriver when needed. This may require network access on first run.

## Run

From the repository root:

```powershell
python "Selenium/Microsoft teams/tests/test_teams.py"
```

The script displays interactive sign-in prompts, navigates through Teams, and may schedule and save a meeting.
