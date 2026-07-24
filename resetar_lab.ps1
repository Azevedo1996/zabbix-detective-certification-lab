# ATENCAO: remove containers e volumes do homelab.
$ErrorActionPreference = "Stop"
docker compose down -v
$djangoVolume = "zabbix_detective_django_data"
$existingVolume = docker volume ls -q --filter name=$djangoVolume
if ($existingVolume -contains $djangoVolume) {
    docker volume rm $djangoVolume | Out-Null
}
Write-Host "Containers e volumes removidos. Execute .\iniciar.bat ou .\iniciar.ps1 para recriar tudo." -ForegroundColor Yellow
