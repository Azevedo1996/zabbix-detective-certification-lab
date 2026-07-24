@echo off
setlocal
REM Para todos os containers do projeto sem apagar volumes.
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0parar.ps1"
if not "%ERRORLEVEL%"=="0" pause
endlocal
