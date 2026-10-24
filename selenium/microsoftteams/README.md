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
