# Playwright Teams Automation

The Microsoft Teams automation project, including page objects and pytest tests, is in `Microsoft teams/`.

From the repository root, install dependencies and browsers with:

```powershell
python -m pip install -r requirements.txt
playwright install chromium
```

Run the tests with:

```powershell
python -m pytest "Playwright/Microsoft teams/tests/" -v -s
```
