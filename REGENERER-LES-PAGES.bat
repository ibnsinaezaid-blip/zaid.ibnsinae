@echo off
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
  py -3 -X utf8 generate.py
) else (
  python -X utf8 generate.py
)
pause
