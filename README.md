# Browser Automation Projects

This repository contains Microsoft Teams browser automation projects using Playwright and Selenium:

- [Playwright Teams](playwright/microsoftteams/README.md): page objects, pytest checks, and BDD examples using Behave, pytest-bdd, Radish, and Cucumber-style Gherkin with Python steps.
- [Selenium Teams](selenium/microsoftteams/README.md): Selenium page objects and tests, plus a Robot Framework smoke test using SeleniumLibrary.
- [Teams page check](api/README.md): a Python `requests` check that the public Teams sign-in page responds.

## Setup

From the repository root, install all Python project dependencies:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
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

The four Playwright suites sign in to Teams and verify that the home page is displayed. They prompt for an email and masked password, or read `TEAMS_EMAIL` and `TEAMS_PASSWORD` from the environment or `playwright/microsoftteams/.env`. They do not schedule meetings. Setup and run commands are in [playwright/microsoftteams/bdd/README.md](playwright/microsoftteams/bdd/README.md).

Run the Selenium Robot Framework suite from the repository root:

```powershell
python -m robot --outputdir selenium/microsoftteams/robot/results selenium/microsoftteams/robot/teams_login.robot
```

Its setup and details are in [selenium/microsoftteams/README.md](selenium/microsoftteams/README.md). It checks the public sign-in entry point without logging in. The existing account sign-in flows may schedule and save a meeting.
