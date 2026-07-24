# Zabbix Detective - inicializacao completa com um comando
# Execute na raiz do projeto:
#   .\iniciar.ps1
# ou use:
#   iniciar.bat

$ErrorActionPreference = "Stop"

function Run-Cmd($commandLine) {
    Write-Host "> $commandLine" -ForegroundColor DarkGray
    cmd.exe /c $commandLine
    if ($LASTEXITCODE -ne 0) {
        throw ("Comando falhou com codigo {0}: {1}" -f $LASTEXITCODE, $commandLine)
    }
}

Write-Host "============================================" -ForegroundColor Cyan
Write-Host " Zabbix Detective + Zabbix Lab" -ForegroundColor Cyan
Write-Host " Inicializacao automatica" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

if (!(Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker nao encontrado. Instale/abra o Docker Desktop e tente novamente." -ForegroundColor Red
    exit 1
}

if (!(Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "Arquivo .env criado a partir do .env.example" -ForegroundColor Yellow
}

Write-Host "Verificando possivel conflito na porta 8989..." -ForegroundColor Yellow
try {
    $portCheck = Test-NetConnection -ComputerName localhost -Port 8989 -InformationLevel Quiet -WarningAction SilentlyContinue
    if ($portCheck) {
        Write-Host "A porta 8989 ja esta em uso. O docker compose tentara parar containers antigos primeiro." -ForegroundColor Yellow
    }
} catch {}

Write-Host "Parando containers antigos, se existirem..." -ForegroundColor Yellow
Run-Cmd "docker compose down --remove-orphans"

Write-Host "Limpando somente o banco SQLite do Zabbix Detective para evitar conflito de migrations antigas..." -ForegroundColor Yellow
$djangoVolume = "zabbix_detective_django_data"
$existingVolume = docker volume ls -q --filter name=$djangoVolume
if ($existingVolume -contains $djangoVolume) {
    Run-Cmd "docker volume rm $djangoVolume"
    Write-Host "Volume $djangoVolume removido." -ForegroundColor Yellow
}

Write-Host "Construindo imagem e subindo todos os containers..." -ForegroundColor Green
Write-Host "O container django executa automaticamente: migrate, seed_game, seed_simulados e runserver." -ForegroundColor DarkGray

# Importante: nao usar pipe/Tee-Object aqui.
# No PowerShell 5.1, saidas de stderr de comandos nativos podem virar NativeCommandError
# e quebrar o script mesmo quando o docker compose esta apenas imprimindo progresso normal.
Run-Cmd "docker compose up -d --build"

Write-Host ""
Write-Host "Aguardando Django iniciar na porta 8989..." -ForegroundColor Yellow
$ok = $false
for ($i = 1; $i -le 40; $i++) {
    Start-Sleep -Seconds 3
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:8989" -UseBasicParsing -TimeoutSec 2
        if ($response.StatusCode -ge 200 -and $response.StatusCode -lt 500) {
            $ok = $true
            break
        }
    } catch {
        # Ainda inicializando.
    }
}

Run-Cmd "docker compose ps"

if (-not $ok) {
    Write-Host "" -ForegroundColor Red
    Write-Host "O Django ainda nao respondeu em http://localhost:8989." -ForegroundColor Red
    Write-Host "Logs do container django:" -ForegroundColor Yellow
    cmd.exe /c "docker compose logs --tail=200 django"
    Write-Host "" -ForegroundColor Yellow
    Write-Host "Se o Zabbix ainda estiver inicializando, aguarde alguns minutos e rode:" -ForegroundColor Yellow
    Write-Host "docker compose logs -f django zabbix-web zabbix-server" -ForegroundColor DarkGray
    exit 1
}

Write-Host "" -ForegroundColor Green
Write-Host "Pronto." -ForegroundColor Green
Write-Host "Zabbix Detective: http://localhost:8989" -ForegroundColor Cyan
Write-Host "Zabbix Lab:       http://localhost:4000" -ForegroundColor Cyan
Write-Host "Login Zabbix:     Admin / zabbix" -ForegroundColor Cyan
Write-Host ""
Write-Host "Para acompanhar logs:" -ForegroundColor DarkGray
Write-Host "docker compose logs -f django zabbix-web zabbix-server" -ForegroundColor DarkGray
