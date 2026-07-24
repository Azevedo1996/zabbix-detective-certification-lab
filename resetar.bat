@echo off
setlocal
REM Reseta o homelab, removendo containers e volumes.
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0resetar_lab.ps1"
if not "%ERRORLEVEL%"=="0" pause
endlocal
