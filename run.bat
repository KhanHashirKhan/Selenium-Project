@echo off
cd /d %~dp0
echo Running Selenium Test Cases...
pytest tests/
pause