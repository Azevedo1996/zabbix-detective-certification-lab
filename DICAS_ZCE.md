# Dicas Específicas para ZCE — Zabbix Certified Expert

A preparação para ZCE deve ser orientada por arquitetura, troubleshooting, segurança, performance e integração. O foco é raciocinar como quem projeta e sustenta ambientes grandes.

## Mentalidade ZCE

ZCE não deve ser estudado como uma lista de comandos. Estude pensando em impactos:

- O que acontece se o banco atrasar?
- O que acontece se a queue crescer?
- O que acontece se o proxy perder conexão?
- O que acontece se um segredo vazar?
- O que acontece se uma integração externa falhar?
- O que acontece durante upgrade ou manutenção?

## Tópicos críticos

### 1. Performance

- Queue alta.
- Pollers ocupados.
- Cache insuficiente.
- Banco lento.
- Preprocessing sobrecarregado.
- History syncers e escrita em banco.
- Retenção de history/trends.

### 2. Segurança

- TLS entre componentes.
- PSK vs certificado.
- Proteção de private keys e PSK.
- HTTPS no frontend.
- LDAP, SAML, MFA.
- API tokens com escopo mínimo.
- Roles, user groups e host groups.
- Segredos em vault/cofre.

### 3. Arquitetura

- Server, Proxy, Frontend e Database.
- Proxy ativo/passivo.
- HA conceitual.
- Separação de ambientes.
- Monitoramento distribuído.
- Planejamento de capacidade.

### 4. Integrações

- Zabbix API JSON-RPC.
- Ansible e idempotência.
- AWS IAM e CloudWatch.
- Azure service principal.
- Database monitor via ODBC.
- Webhooks para ITSM.

## Dicas de prova para ZCE

### 1. Encontre o gargalo real

Se a questão fala em atraso de coleta, não escolha uma resposta de interface visual. Pense em pollers, proxy, rede, cache ou banco.

### 2. Não confunda segurança de camadas diferentes

- TLS interno protege comunicação entre componentes.
- HTTPS protege navegador até frontend.
- SAML/LDAP/MFA autentica usuários.
- API token autentica automações Zabbix.
- IAM AWS, service principal Azure e ODBC são identidades externas.

### 3. Pense em rollback

Em cenários de TLS, upgrade, proxy ou automação, a melhor resposta geralmente preserva disponibilidade e permite rollback.

### 4. Evite soluções irreversíveis

Excluir lost resources imediatamente, apagar histórico ou aplicar mudança global sem teste costuma ser mais arriscado que desabilitar, testar e validar.

### 5. Em performance, monitore o próprio Zabbix

Ambiente grande precisa monitorar Zabbix server, proxy, database, queues, caches e processos internos.

### 6. Em API, pense em idempotência

Antes de criar, consulte. Antes de atualizar em massa, rode em lote. Antes de automatizar, registre logs, retries e backoff.

## Laboratórios recomendados para ZCE

- Simular queue alta com item lento.
- Criar proxy ativo e testar perda temporária de comunicação.
- Configurar TLS PSK em ambiente de laboratório.
- Criar API token com usuário de baixa permissão e testar chamadas permitidas/negadas.
- Criar role restrita e validar acesso por host group.
- Criar item HTTP agent com preprocessing e dependent items.
- Criar integração fake de webhook para ITSM.
- Testar DSN ODBC com usuário read-only.

## Checklist ZCE final

- [ ] Sei explicar causa provável de queue alta.
- [ ] Sei diferenciar gargalo de coleta, preprocessing e banco.
- [ ] Sei explicar TLS interno vs HTTPS do frontend.
- [ ] Sei explicar PSK, certificado, TLSConnect e TLSAccept.
- [ ] Sei explicar API token, role e permissões por grupo.
- [ ] Sei separar identidades de Zabbix, AWS, Azure, banco e ITSM.
- [ ] Sei descrever estratégia segura de upgrade ou mudança crítica.
- [ ] Sei explicar LLD avançado, filters, overrides e lost resources.
- [ ] Sei propor tuning sem sair aumentando parâmetros aleatoriamente.

## Materiais complementares

- Consulte [`PLANO_ESTUDO_ZCE.md`](PLANO_ESTUDO_ZCE.md) para cronograma ZCE completo.
- Consulte [`TRIGGERS_COMPLEXAS.md`](TRIGGERS_COMPLEXAS.md) para aprofundar triggers complexas.
