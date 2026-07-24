# Para todos os containers do lab, sem apagar volumes.
$ErrorActionPreference = "Stop"
docker compose down
Write-Host "Ambiente parado. Para iniciar novamente, execute .\iniciar.bat ou .\iniciar.ps1" -ForegroundColor Green
