# Plano de Revisão Semanal — Zabbix Detective

Este plano deve ser usado junto com o `GUIA_ESTUDO.md`. A ideia é criar ciclos semanais de revisão para evitar esquecer tópicos já estudados.

## Ciclo semanal padrão

### Segunda-feira — Revisão de fundamentos

- Rever anotações da semana anterior.
- Refazer 5 questões erradas.
- Escolher 1 tema fraco para laboratório.

### Terça-feira — Coleta e configuração

- Revisar itens, item types, interfaces e preprocessing.
- Refazer desafios de Data Collection e ZCS.
- Criar ou revisar 1 item e 1 trigger em laboratório.

### Quarta-feira — Detecção e alertas

- Revisar triggers, `nodata()`, recovery expression e hysteresis.
- Refazer desafios de Alerts.
- Explicar em voz alta a diferença entre trigger, event, problem e action.

### Quinta-feira — Automação e escala

- Revisar LLD, proxies, API e Ansible.
- Refazer desafios de ZCP, Automação API e Ansible.
- Desenhar um fluxo idempotente de onboarding.

### Sexta-feira — Segurança e integrações

- Revisar autenticação, API tokens, roles, grupos e TLS.
- Refazer desafios de Segurança e Autenticação.
- Revisar AWS, Azure ou Bancos alternando por semana.

### Sábado — Simulado curto

- Fazer 20 a 40 questões sem consultar gabarito.
- Cronometrar o tempo.
- Marcar dúvidas mesmo que a resposta esteja correta.

### Domingo — Correção e descanso ativo

- Corrigir erros.
- Ler links oficiais dos tópicos errados.
- Atualizar checklist pessoal de gaps.

## Revisão por ciclo de certificação

### Semana ZCU

- Prioridade: operação visual, telas, conceitos básicos e componentes.
- Simulado recomendado: 20 questões / 30 minutos.

### Semana ZCS

- Prioridade: configuração prática, itens, triggers, templates, actions e coleta.
- Simulado recomendado: 50 questões / 60 minutos.

### Semana ZCP

- Prioridade: LLD, proxy, automação, API, discovery, escala e correlação.
- Simulado recomendado: 60 a 75 questões / 90 minutos.

### Semana ZCE

- Prioridade: segurança, performance, tuning, processos internos, banco, TLS, API e troubleshooting.
- Simulado recomendado: cenários longos + revisão dos erros críticos.

## Matriz de revisão rápida

```text
Coleta       -> itens, item types, agent, SNMP, HTTP agent, ODBC, dependent item
Detecção     -> triggers, functions, nodata, hysteresis, severity
Notificação  -> actions, media types, escalations, maintenance
Escala       -> proxies, LLD, discovery, preprocessing, trends
Segurança    -> users, roles, LDAP, SAML, MFA, API tokens, TLS
Integrações  -> API, Ansible, AWS, Azure, bancos, ITSM
Performance  -> queue, cache, pollers, preprocessors, DB, history syncers
```

## Regra 70/20/10

- **70% prática:** responder desafios e criar laboratório.
- **20% revisão:** corrigir erros e consultar documentação.
- **10% resumo:** escrever explicações próprias.
