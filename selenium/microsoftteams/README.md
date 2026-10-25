# Selenium Microsoft Teams

## Git Bash

### Setup

```
cd /f/Project/Browser
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r selenium/microsoftteams/requirements.txt
```

### Robot Framework

```
.venv/Scripts/python.exe -m robot --outputdir selenium/microsoftteams/robot/results selenium/microsoftteams/robot/teams_login.robot
```

### Selenium pytest

```
.venv/Scripts/python.exe -m pytest selenium/microsoftteams/tests/ -v -s
```

## PowerShell

### Setup

```
Set-Location F:\Project\Browser
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r selenium/microsoftteams/requirements.txt
```

### Robot Framework

```
& .\.venv\Scripts\python.exe -m robot --outputdir selenium/microsoftteams/robot/results selenium/microsoftteams/robot/teams_login.robot
```

### Selenium pytest

```
& .\.venv\Scripts\python.exe -m pytest selenium/microsoftteams/tests/ -v -s
```

## Jenkins CI

The repository-root `Jenkinsfile` runs the Robot Framework check for the public Teams sign-in page. Configure a Windows Jenkins agent with the label `windows-chrome` and install Python 3 and Google Chrome on that agent. Then create a Pipeline job from SCM pointing to this repository and its root `Jenkinsfile`. Jenkins checks out the code, installs `selenium/microsoftteams/requirements.txt`, runs Chrome headlessly, and archives the Robot Framework results.

This pipeline checks the public sign-in entry point; it does not sign in to a Teams account.
