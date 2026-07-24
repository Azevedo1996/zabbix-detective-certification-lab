# Homelab Docker do Zabbix Detective

Este arquivo sobe o homelab completo com Django + Zabbix real.

## Serviços criados

- `django` em `http://localhost:8989`
- `zabbix-db` com PostgreSQL persistente
- `zabbix-server`
- `zabbix-web` em `http://localhost:4000`
- `zabbix-agent`
- rede Docker dedicada `zabbix_detective_lab`
- volumes persistentes para banco do Zabbix e banco SQLite do Django

## Subir no Windows PowerShell

```powershell
.\iniciar.ps1
```

Ou manualmente:

```powershell
docker compose up -d --build
```

## Acessos

- Zabbix Detective: `http://localhost:8989`
- Zabbix Lab: `http://localhost:4000`
- Usuário padrão do Zabbix: `Admin`
- Senha padrão do Zabbix: `zabbix`

Na primeira subida, o Zabbix pode levar alguns minutos para inicializar o schema do banco.

## Verificar status

```powershell
docker compose ps
docker compose logs -f zabbix-db zabbix-server zabbix-web
```

## Reset completo do laboratório

```powershell
scripts\reset_zabbix_lab.ps1
```

Isso remove containers e volumes do homelab.


## Um comando apenas

Use somente:

```powershell
.\iniciar.ps1
```

Não execute `python manage.py runserver` separadamente. O Django já roda dentro do container `django` e fica acessível em `http://localhost:8989`.


## Observação sobre migrations

O script `iniciar.ps1` remove automaticamente o volume `zabbix_detective_django_data`, que guarda apenas o SQLite do Zabbix Detective. Isso evita erro por banco antigo quando o código muda. Os volumes do Zabbix (`zabbix_pgdata`) não são removidos pelo iniciar normal.
