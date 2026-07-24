@echo off
setlocal
REM Zabbix Detective - inicializacao completa com um comando
REM Execute na raiz do projeto:
REM   iniciar.bat

cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0iniciar.ps1"
set EXITCODE=%ERRORLEVEL%
if not "%EXITCODE%"=="0" (
    echo.
    echo Falha ao iniciar o ambiente. Codigo: %EXITCODE%
    echo Rode o comando abaixo para ver logs:
    echo docker compose logs -f django zabbix-web zabbix-server
    echo.
    pause
    exit /b %EXITCODE%
)
endlocal
