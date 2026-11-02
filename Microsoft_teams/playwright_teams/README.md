# Playwright Microsoft Teams

> **Note:** The shared `.venv` is at `F:\Project\Browser\.venv` (one level above this project).
> Always run commands from inside `F:\Project\Browser\Microsoft_teams` — `pytest.ini` is
> configured there so pytest resolves `playwright/tests/` correctly.

## Git Bash

### Activate shared venv

```bash
source /f/Project/Browser/.venv/Scripts/activate
cd /f/Project/Browser/Microsoft_teams
```

### Setup (first time only)

```bash
cd /f/Project/Browser
python -m venv .venv
source .venv/Scripts/activate
pip install -r Microsoft_teams/requirements.txt
python -m playwright_teams install chromium
```

### pytest

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest -v -s

Run only Playwright UI tests:

```bash
python -m pytest playwright_teams/tests/ -v -s
```

Run only Playwright pytest-BDD tests:

```bash
python -m pytest playwright_teams/bdd/pytest_bdd/ -v -s
```
```

### Behave

```bash
cd /f/Project/Browser/Microsoft_teams
python -m behave --no-capture playwright_teams/bdd/behave/features
```

### pytest-bdd

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest playwright_teams/bdd/pytest_bdd/ -v -s
```

### Radish

```bash
cd /f/Project/Browser/Microsoft_teams
/f/Project/Browser/.venv/Scripts/radish.exe -b playwright_teams/bdd/radish/features/steps playwright_teams/bdd/radish/features/
```

### Cucumber-style Gherkin with Python steps

```bash
cd /f/Project/Browser/Microsoft_teams
python -m behave --no-capture playwright_teams/bdd/cucumber_python/features
```

## PowerShell

### Activate shared venv

```powershell
& F:\Project\Browser\.venv\Scripts\Activate.ps1
Set-Location F:\Project\Browser\Microsoft_teams
```

### Setup (first time only)

```powershell
Set-Location F:\Project\Browser
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r Microsoft_teams\requirements.txt
python -m playwright install chromium
```

### pytest

```powershell
Set-Location F:\Project\Browser\Microsoft_teams
python -m pytest -v -s
```

### Behave

```powershell
Set-Location F:\Project\Browser\Microsoft_teams
python -m behave --no-capture playwright/bdd/behave/features
```

### pytest-bdd

```powershell
Set-Location F:\Project\Browser\Microsoft_teams
python -m pytest playwright/bdd/pytest_bdd/ -v -s
```

### Radish

```powershell
Set-Location F:\Project\Browser\Microsoft_teams
& F:\Project\Browser\.venv\Scripts\radish.exe -b playwright/bdd/radish/features/steps playwright/bdd/radish/features/
```

### Cucumber-style Gherkin with Python steps

```powershell
Set-Location F:\Project\Browser\Microsoft_teams
python -m behave --no-capture playwright/bdd/cucumber_python/features
```

## GitHub Actions CI

The root `.github/workflows/playwright.yml` runs a credential-free public sign-in page browser check on pushes and pull requests to `main`. GitHub Actions installs the Playwright Python dependencies and Chromium on its hosted runner. It does not perform an account sign-in.
# Run Playwright tests with pytest

In Git Bash, navigate to the repository root and run the Playwright UI and pytest-BDD tests separately from Selenium:

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest playwright_teams/tests/ playwright_teams/bdd/pytest_bdd/ -v -s
```

# Run the full project pytest suite

In Git Bash, from any directory:

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest -v -s
```

This runs the API, Playwright, and Selenium pytest suites. To run only Playwright tests, use the command below.

# Run only Playwright pytest tests

In Git Bash:

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest playwright_teams/tests/ playwright_teams/bdd/pytest_bdd/ -v -s
```

# Run Playwright UI tests only

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest playwright_teams/tests/ -v -s
```

# Run Playwright pytest-BDD tests only

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest playwright_teams/bdd/pytest_bdd/ -v -s
```

