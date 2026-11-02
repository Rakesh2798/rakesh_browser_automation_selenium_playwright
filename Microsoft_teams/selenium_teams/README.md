# Selenium Microsoft Teams

## Git Bash

### Setup

```bash
cd /f/Project/Browser/Microsoft_teams
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
```

### Robot Framework

```bash
python -m robot --outputdir selenium_teams/robot/results selenium_teams/robot/teams_login.robot
```

### Selenium pytest

```bash
.venv/Scripts/python.exe -m pytest selenium_teams/tests/ -v -s
```

## PowerShell

### Setup

```powershell
Set-Location F:\Project\Browser\Microsoft_teams
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Robot Framework

```powershell
& .\.venv\Scripts\python.exe -m robot --outputdir selenium\robot\results selenium\robot\teams_login.robot
```

### Selenium pytest

```powershell
& .\.venv\Scripts\python.exe -m pytest selenium/tests/ -v -s
```

## Jenkins CI

The repository-root `Jenkinsfile` runs the Robot Framework check for the public Teams sign-in page. Configure a Windows Jenkins agent with the label `windows-chrome` and install Python 3 and Google Chrome on that agent. Then create a Pipeline job from SCM pointing to this repository and its root `Jenkinsfile`. Jenkins checks out the code, installs `selenium/requirements.txt`, runs Chrome headlessly, and archives the Robot Framework results.

This pipeline checks the public sign-in entry point; it does not sign in to a Teams account.
# Run Selenium tests with pytest

In Git Bash, navigate to the repository root and run the Selenium tests separately from Playwright:

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest selenium_teams/tests/ -v -s
```

# Run the full project pytest suite

In Git Bash, from any directory:

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest -v -s
```

This runs the API, Playwright, and Selenium pytest suites. To run only Selenium tests, use the command below.

# Run only Selenium pytest tests

In Git Bash:

```bash
cd /f/Project/Browser/Microsoft_teams
python -m pytest selenium_teams/tests/ -v -s
```

# Run Selenium Robot Framework tests

From Git Bash, run from the repository root:

```bash
cd /f/Project/Browser/Microsoft_teams
python -m robot --outputdir selenium_teams/robot/results selenium_teams/robot/teams_login.robot
```

