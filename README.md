# Browser Automation Projects

This repository groups browser automation projects by framework:

- `Playwright/Microsoft teams/`
- `Selenium/Microsoft teams/`

Add future site projects under the relevant framework, for example `Playwright/Amazon/` or `Selenium/Flipkart/`.

## Setup

Run from this repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install chromium
```

## Run

Playwright:

```powershell
python -m pytest "Playwright/Microsoft teams/tests/" -v -s
```

Selenium:

```powershell
python "Selenium/Microsoft teams/tests/test_teams.py"
```

Both flows sign in to Teams and may schedule and save a meeting.
