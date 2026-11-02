# Teams public page checks with requests

## Git Bash

```bash
cd /f/Project/Browser/Microsoft_teams
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m pytest api/tests/ -v -s
```

## PowerShell

```powershell
Set-Location F:\Project\Browser\Microsoft_teams
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m pytest api/tests/ -v -s
```
