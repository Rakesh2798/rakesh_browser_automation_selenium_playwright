# Playwright BDD examples

Each framework has a Given–When–Then scenario that signs in to Teams and verifies the home page. These examples require Teams credentials and do not schedule meetings. They read `TEAMS_EMAIL` and `TEAMS_PASSWORD` from the environment or `playwright/.env`; when missing, they prompt for the email and masked password. Password masking uses `prompt_toolkit`, installed with the project requirements. Behave commands use `--no-capture` so prompts and progress messages stay visible. Chromium opens visibly by default for MFA; set `TEAMS_HEADLESS=true` to run headless when interactive verification is not needed.

Run the commands in each section from the repository root (`F:\Project\Browser\Microsoft_teams`). If your current directory is `playwright`, use the project-relative commands in the table below; using repository-root paths from that folder duplicates `playwright` in the resolved path and Behave cannot find the `steps` directory.

The pytest-bdd command below uses the repository-root path. If you run it from `playwright` instead, use `python -m pytest bdd/pytest_bdd/ -v -s`.

## Setup

Run from the repository root. Activate `.venv` in your terminal before running the BDD commands so `python` resolves to the environment with Behave and the other dependencies installed. In PowerShell run `.\\.venv\\Scripts\\Activate.ps1`; in Git Bash run `source .venv/Scripts/activate`.

```bash
python -m pip install -r requirements.txt
python -m playwright_teams install chromium
```

## Behave

From the repository root:

```bash
python -m behave --no-capture playwright_teams/bdd/behave/features
```

From `playwright`:

```bash
python -m behave --no-capture bdd/behave/features
```

## pytest-bdd

```bash
python -m pytest playwright_teams/bdd/pytest_bdd/ -v -s
```

## Radish

Run from Git Bash at the repository root (`/f/Project/Browser/Microsoft_teams`):

```bash
cd /f/Project/Browser/Microsoft_teams
.venv/Scripts/radish.exe -b playwright_teams/bdd/radish/features/steps playwright_teams/bdd/radish/features/
```

## Cucumber-style Gherkin with Python steps

Cucumber has no official Python runner. This example uses Cucumber's Gherkin `.feature` format with Python step definitions run by Behave; it needs no JavaScript or Node.js setup.

From the repository root:

```bash
python -m behave --no-capture playwright_teams/bdd/cucumber_python/features
```

From `playwright`:

```bash
python -m behave --no-capture bdd/cucumber_python/features
```

See [Cucumber's supported implementations](https://github.com/cucumber) for details about the official runners and Behave's relationship to Cucumber.
