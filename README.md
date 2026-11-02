# Browser Automation Projects

This repository contains Microsoft Teams browser automation projects using Playwright and Selenium:

- [Playwright Teams](playwright_teams/README.md): page objects, pytest checks, and BDD examples using Behave, pytest-bdd, Radish, and Cucumber-style Gherkin with Python steps.
- [Selenium Teams](selenium_teams/README.md): Selenium page objects and tests, plus a Robot Framework smoke test using SeleniumLibrary.
- [Teams page check](api/README.md): a Python `requests` check that the public Teams sign-in page responds.

## Setup

The `.venv` lives one level above this project at `F:\Project\Browser\.venv` so it is shared across sibling projects.

```bash
# Git Bash — create shared venv once, from the Browser root
cd /f/Project/Browser
python -m venv .venv
source .venv/Scripts/activate
pip install -r Microsoft_teams/requirements.txt
python -m playwright_teams install chromium
```

```powershell
# PowerShell — create shared venv once, from the Browser root
Set-Location F:\Project\Browser
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r Microsoft_teams\requirements.txt
python -m playwright install chromium
```

Activate the shared venv before running any tests:

```bash
# Git Bash
source /f/Project/Browser/.venv/Scripts/activate
```

```powershell
# PowerShell
& F:\Project\Browser\.venv\Scripts\Activate.ps1
```

> **Important:** Always `cd` into `Microsoft_teams` before running tests.
> `pytest.ini` is configured there so pytest resolves paths correctly.

## Running tests

```bash
# Git Bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest -v -s
```

```powershell
# PowerShell
Set-Location F:\Project\Browser\Microsoft_teams
python -m pytest -v -s
```

## CI

**Playwright:** GitHub Actions runs a credential-free browser check of the public Teams sign-in page on pushes and pull requests to `main`. It installs Python dependencies and Chromium on the hosted runner.

**Selenium:** Jenkins runs the public sign-in page Robot Framework check using the root [Jenkinsfile](Jenkinsfile). Configure a Windows Jenkins agent with the label `windows-chrome`, Python 3, and Google Chrome, then create a Pipeline job that loads this repository's `Jenkinsfile` from SCM.

The pipelines do not sign in to a Teams account or deploy an application.

## BDD suites

The repository includes these BDD examples, using only Given, When, and Then steps:

- **Behave** — Python BDD suite for Playwright.
- **pytest-bdd** — pytest-integrated BDD suite for Playwright.
- **Radish** — Python BDD suite for Playwright.
- **Cucumber-style Gherkin with Python steps** — the feature format is Cucumber's Gherkin; Behave runs its Python step definitions because Cucumber has no official Python runner.
- **Robot Framework with SeleniumLibrary** — Selenium Teams smoke test.

The four Playwright suites sign in to Teams and verify that the home page is displayed. They prompt for an email and masked password, or read `TEAMS_EMAIL` and `TEAMS_PASSWORD` from the environment or `playwright/.env`. They do not schedule meetings. Setup and run commands are in [playwright/bdd/README.md](playwright_teams/bdd/README.md).

Run the Selenium Robot Framework suite from inside `Microsoft_teams`:

```bash
# Git Bash
cd /f/Project/Browser/Microsoft_teams
python -m robot --outputdir selenium_teams/robot/results selenium_teams/robot/teams_login.robot
```

```powershell
# PowerShell
Set-Location F:\Project\Browser\Microsoft_teams
python -m robot --outputdir selenium\robot\results selenium\robot\teams_login.robot
```

Its setup and details are in [selenium/README.md](selenium_teams/README.md). It checks the public sign-in entry point without logging in.
# Run all pytest suites

In Git Bash:

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest -v -s
```

This runs all pytest-discovered tests, including API, Playwright, and Selenium tests. To run Playwright or Selenium separately, use the commands in their respective project READMEs.

