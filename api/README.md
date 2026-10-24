# Teams public page checks with requests

## Git Bash

```
cd /f/Project/Browser
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r api/requirements.txt
.venv/Scripts/python.exe -m pytest api/tests/ -v -s
```

## PowerShell

```
Set-Location F:\Project\Browser
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r api/requirements.txt
& .\.venv\Scripts\python.exe -m pytest api/tests/ -v -s
```
