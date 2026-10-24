# Playwright Microsoft Teams

## Git Bash

### Setup

```
cd /f/Project/Browser
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r playwright/microsoftteams/requirements.txt
python -m playwright install chromium
```

### pytest

```
python -m pytest playwright/microsoftteams/tests/ -v -s
```

### Behave

```
python -m behave --no-capture playwright/microsoftteams/bdd/behave/features
```

### pytest-bdd

```
python -m pytest playwright/microsoftteams/bdd/pytest_bdd/ -v -s
```

### Radish

```
cd /f/Project/Browser
.venv/Scripts/radish.exe -b playwright/microsoftteams/bdd/radish/features/steps playwright/microsoftteams/bdd/radish/features/
```

### Cucumber-style Gherkin with Python steps

```
python -m behave --no-capture playwright/microsoftteams/bdd/cucumber_python/features
```

## PowerShell

### Setup

```
Set-Location F:\Project\Browser
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r playwright/microsoftteams/requirements.txt
python -m playwright install chromium
```

### pytest

```
python -m pytest playwright/microsoftteams/tests/ -v -s
```

### Behave

```
python -m behave --no-capture playwright/microsoftteams/bdd/behave/features
```

### pytest-bdd

```
python -m pytest playwright/microsoftteams/bdd/pytest_bdd/ -v -s
```

### Radish

```
Set-Location F:\Project\Browser
& .\.venv\Scripts\radish.exe -b playwright/microsoftteams/bdd/radish/features/steps playwright/microsoftteams/bdd/radish/features/
```

### Cucumber-style Gherkin with Python steps

```
python -m behave --no-capture playwright/microsoftteams/bdd/cucumber_python/features
```
