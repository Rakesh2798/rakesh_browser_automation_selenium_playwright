# Browser Automation Projects

This repository contains browser automation projects organized by framework:

- `Playwright/` contains the Playwright page objects and pytest tests.
- `Selenium/` contains the Selenium page objects and tests.

Each framework has its own README and requirements file. Install the shared dependencies from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install chromium
```

## Run

Playwright:

```powershell
python -m pytest Playwright/tests/ -v -s
```

Selenium:

```powershell
python Selenium/tests/test_teams.py
```

Both flows sign in to Teams and may schedule and save a meeting.
