# Plano de Estudo ZCE — Zabbix Certified Expert

Este plano é focado em preparação para **Zabbix Certified Expert (ZCE)** usando o Zabbix Detective como simulador prático. O objetivo é sair de uma revisão genérica e treinar raciocínio de arquitetura, performance, segurança, integrações, upgrade e troubleshooting.

> Observação: a ZCE exige domínio de cenários avançados. Use este plano junto com laboratório prático e documentação oficial.

## Sumário

- [Objetivo do plano](#objetivo-do-plano)
- [Pré-requisitos](#pré-requisitos)
- [Cronograma de 8 semanas](#cronograma-de-8-semanas)
- [Rotina semanal ZCE](#rotina-semanal-zce)
- [Laboratórios obrigatórios](#laboratórios-obrigatórios)
- [Critério de aprovação pessoal](#critério-de-aprovação-pessoal)
- [Checklist final ZCE](#checklist-final-zce)

## Objetivo do plano

Ao final do plano, você deve conseguir:

- explicar arquitetura Zabbix em ambientes grandes;
- diagnosticar gargalos de coleta, preprocessing, queue, cache e banco;
- desenhar estratégia de segurança com TLS, PSK, certificados, SAML, LDAP, MFA e API tokens;
- planejar upgrade com baixo risco;
- integrar Zabbix com API, Ansible, AWS, Azure, banco de dados e ITSM;
- justificar decisões de tuning sem aplicar parâmetros aleatórios.

## Pré-requisitos

Antes de iniciar este plano, revise:

- ZCU Core;
- ZCS Core;
- ZCP Core;
- Automação API;
- Segurança;
- Autenticação;
- Bancos de Dados;
- AWS e Azure, se fizerem parte do seu ambiente.

## Cronograma de 8 semanas

### Semana 1 — Arquitetura e baseline

**Tema:** entender arquitetura e estado atual.

Estude:

- Server, proxy, frontend e database;
- fluxo de dados;
- processos internos;
- server vs proxy;
- telemetria do próprio Zabbix.

Prática:

- Desenhe o fluxo: host -> proxy/agent -> server -> history syncer -> database -> frontend.
- Liste quais métricas indicam saúde do próprio Zabbix.
- Refazer desafios ZCE Core e Administration.

Meta:

- Conseguir explicar o caminho de uma métrica desde a coleta até a exibição.

### Semana 2 — Banco, history e trends

**Tema:** performance e retenção.

Estude:

- history;
- trends;
- housekeeping;
- retenção;
- tuning MySQL/PostgreSQL;
- TimescaleDB/partitioning conceitual.

Prática:

- Identificar quais itens têm maior volume.
- Criar proposta de retenção por tipo de métrica.
- Revisar desafios de Database monitor e performance.

Meta:

- Explicar por que armazenar tudo por muito tempo pode degradar performance.

### Semana 3 — Queue, pollers e preprocessing

**Tema:** troubleshooting de gargalos.

Estude:

- queue;
- pollers;
- preprocessors;
- trapper;
- cache;
- history syncers;
- itens lentos.

Prática:

- Simular cenário de “queue alta”.
- Criar matriz: sintoma -> causa provável -> evidência -> ação.
- Refazer desafios de performance, data collection e preprocessing.

Meta:

- Diagnosticar queue alta sem sair aumentando parâmetros sem critério.

### Semana 4 — Segurança enterprise

**Tema:** proteger plataforma e credenciais.

Estude:

- TLS interno;
- PSK;
- certificados;
- HTTPS do frontend;
- SAML;
- LDAP;
- MFA;
- API tokens;
- user roles;
- user groups;
- vault/segredos.

Prática:

- Criar desenho de segurança com separação entre autenticação e autorização.
- Criar plano de rotação de API tokens.
- Refazer desafios de Segurança e Autenticação.

Meta:

- Explicar diferença entre TLS interno, HTTPS, SSO e autorização por host group.

### Semana 5 — API, automação e integrações

**Tema:** automação segura e idempotente.

Estude:

- JSON-RPC;
- API token;
- login token;
- filtros de API;
- idempotência;
- Ansible community.zabbix;
- onboarding/offboarding.

Prática:

- Desenhar fluxo de onboarding de host.
- Definir validações antes de criar/atualizar recursos.
- Refazer Automação API e Ansible.

Meta:

- Explicar como evitar duplicidade e alterações perigosas em automações.

### Semana 6 — LLD, discovery e correlação avançada

**Tema:** escala com descoberta automática.

Estude:

- LLD macros;
- prototypes;
- filters;
- overrides;
- lost resources;
- dependent discovery;
- correlação de eventos;
- trigger dependencies.

Prática:

- Criar cenário com filesystem/interface descobertos.
- Definir filtro para descartar recursos irrelevantes.
- Definir estratégia para lost resources sem perder histórico.

Meta:

- Explicar quando usar filter, override, dependency e correlation.

### Semana 7 — Cloud, bancos e sistemas externos

**Tema:** múltiplos sistemas.

Estude:

- AWS by HTTP;
- IAM/access key/assume role;
- Azure by HTTP;
- service principal;
- ODBC/DSN;
- ITSM/webhooks;
- credenciais separadas por sistema.

Prática:

- Criar matriz de identidade:
  - Zabbix API token;
  - AWS IAM;
  - Azure service principal;
  - DB user;
  - ITSM token.

Meta:

- Explicar por que um token Zabbix não substitui IAM, Azure SP ou credencial ODBC.

### Semana 8 — Simulado e revisão final

**Tema:** consolidação.

Faça:

- ZCE Core;
- Segurança;
- Autenticação;
- Automação API;
- LLD/ZCP;
- AWS;
- Azure;
- Bancos.

Método:

- responder sem gabarito;
- marcar dúvidas;
- revisar links oficiais;
- repetir questões erradas.

Meta:

- 90%+ nos desafios ZCE e extras críticos.

## Rotina semanal ZCE

```text
Segunda  -> arquitetura e processos internos
Terça    -> banco, history/trends e performance
Quarta   -> queue, pollers, preprocessing e troubleshooting
Quinta   -> segurança, TLS, autenticação e permissões
Sexta    -> API, automação, integrações e cloud
Sábado   -> simulado prático
Domingo  -> correção, documentação oficial e resumo
```

## Laboratórios obrigatórios

- Configurar item com preprocessing e dependent item.
- Criar trigger com problem expression e recovery expression.
- Criar trigger dependency para reduzir alerta em cascata.
- Criar API token com usuário limitado e testar permissão negada.
- Criar user group com acesso somente a um host group.
- Simular queue alta e documentar investigação.
- Criar plano de retenção history/trends.
- Criar desenho de TLS/PSK/certificado para componentes.
- Criar fluxo de onboarding idempotente via API/Ansible.
- Criar mapa de credenciais para Zabbix, AWS, Azure, banco e ITSM.

## Critério de aprovação pessoal

Antes de considerar o estudo pronto:

- [ ] 90%+ nos desafios ZCE e extras críticos.
- [ ] 85%+ no simulado completo.
- [ ] Todos os erros documentados.
- [ ] Pelo menos 5 laboratórios práticos concluídos.
- [ ] Explicação verbal clara sobre performance, segurança, API e LLD.

## Checklist final ZCE

- [ ] Sei explicar arquitetura Zabbix para ambiente grande.
- [ ] Sei diagnosticar queue alta.
- [ ] Sei diferenciar gargalo de coleta, preprocessing, cache e banco.
- [ ] Sei explicar TLS, PSK, certificados e HTTPS.
- [ ] Sei explicar SAML, LDAP, MFA, API tokens, roles e host groups.
- [ ] Sei explicar LLD avançado, filters, overrides, lost resources e dependencies.
- [ ] Sei planejar integração com AWS, Azure, ODBC e ITSM.
- [ ] Sei justificar mudanças com evidências.
- [ ] Sei propor rollback para mudança crítica.
