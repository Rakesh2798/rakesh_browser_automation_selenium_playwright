# Microsoft Teams Browser Automation

This repository contains two independent implementations of Teams browser automation:

- `Playwright/` uses Playwright and pytest.
- `Selenium/` uses Selenium WebDriver.

Each project keeps its own page objects, locators, tests, and dependency list. Both can use the root virtual environment.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install chromium
```

## Run

Run each framework separately from this repository root:

```powershell
python -m pytest Playwright/tests -v -s
python Selenium/tests/test_teams.py
```

Both workflows sign in to a real Teams account. The current flows also navigate through the app and may schedule a meeting, so use an account and environment where those actions are appropriate.

The two original repositories remain separate backups; this combined repository contains their current project files as a clean snapshot.
