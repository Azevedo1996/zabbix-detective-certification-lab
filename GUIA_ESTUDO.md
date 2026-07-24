# Guia de Estudo e Cronograma — Zabbix Detective

Este guia organiza o uso do **Zabbix Detective: A Missão** como trilha de preparação para as certificações **ZCU**, **ZCS**, **ZCP** e **ZCE**, além das missões extras de aprendizado prático.

> **Importante:** o projeto cobre tópicos públicos, documentação oficial e competências práticas esperadas para estudo. O banco oficial de perguntas de exame não é público; portanto, use este guia como preparação estruturada e não como garantia automática de aprovação.

## Sumário

- [1. Como usar este guia](#1-como-usar-este-guia)
- [2. Rotina diária recomendada](#2-rotina-diária-recomendada)
- [3. Cronograma principal de 12 semanas](#3-cronograma-principal-de-12-semanas)
- [4. Cronograma acelerado de 4 semanas](#4-cronograma-acelerado-de-4-semanas)
- [5. Cronograma estendido de 16 semanas](#5-cronograma-estendido-de-16-semanas)
- [6. Estratégia por certificação](#6-estratégia-por-certificação)
- [7. Dicas para certificações](#7-dicas-para-certificações)
- [8. Checklists de revisão](#8-checklists-de-revisão)
- [9. Como simular prova](#9-como-simular-prova)
- [10. Plano de reforço por dificuldade](#10-plano-de-reforço-por-dificuldade)
- [11. Referências oficiais](#11-referências-oficiais)

## Arquivos complementares

- [`SIMULADOS.md`](SIMULADOS.md): links para exames, simulados e prática complementar.
- [`PLANO_REVISAO_SEMANAL.md`](PLANO_REVISAO_SEMANAL.md): rotina semanal de revisão.
- [`DICAS_ZCS.md`](DICAS_ZCS.md): guia focado na certificação ZCS.
- [`DICAS_ZCE.md`](DICAS_ZCE.md): guia focado na certificação ZCE.
- [`PLANO_ESTUDO_ZCE.md`](PLANO_ESTUDO_ZCE.md): plano aprofundado de 8 semanas para ZCE.
- [`TRIGGERS_COMPLEXAS.md`](TRIGGERS_COMPLEXAS.md): técnicas para triggers complexas.
- [`CHECKLIST_PREPARACAO.md`](CHECKLIST_PREPARACAO.md): checklist de prontidão por certificação.
- [`FORUNS_ESTUDO.md`](FORUNS_ESTUDO.md): fóruns e comunidades de estudo.

## 1. Como usar este guia

Use o projeto em três passagens:

1. **Primeira passagem — aprendizado:** leia o conceito antes da questão, responda sem consultar o gabarito e leia a explicação completa.
2. **Segunda passagem — revisão:** refaça apenas os desafios errados e consulte a documentação oficial indicada.
3. **Terceira passagem — simulado:** responda em sequência, sem consultar documentação, anotando os tópicos em que ainda houver dúvida.

O jogo possui atualmente:

- **19 missões**;
- **173 desafios**;
- eixo principal com ZCU, ZCS, ZCP e ZCE;
- missões extras sobre Monitoramento, Serviços, Inventário, Relatórios, Data Collection, Alerts, Users, Administration, API, Segurança, Ansible, AWS, Bancos de Dados, Azure e Autenticação.

## 2. Rotina diária recomendada

### Rotina de 60 a 90 minutos

1. **10 minutos — revisão rápida**
   - Releia anotações do dia anterior.
   - Liste 3 conceitos que ainda estão fracos.

2. **30 a 45 minutos — desafios do jogo**
   - Faça de 8 a 15 desafios.
   - Não use gabarito na primeira tentativa.
   - Após errar, leia a pista e tente novamente.

3. **15 a 25 minutos — documentação oficial**
   - Abra os links oficiais das questões que geraram dúvida.
   - Registre o trecho/conceito principal.

4. **10 minutos — resumo próprio**
   - Escreva, com suas palavras, o que foi aprendido.
   - Crie um exemplo real do seu ambiente ou laboratório.

### Regra dos 3 erros

Se errar o mesmo assunto 3 vezes, transforme o tema em laboratório prático. Exemplo:

- Errou `nodata()`? Crie um item e simule ausência de coleta.
- Errou LLD? Monte uma discovery rule simples.
- Errou API token? Crie token com usuário de baixa permissão e teste `host.get`.
- Errou ODBC? Valide DSN, driver e usuário de banco.

## 3. Cronograma principal de 12 semanas

### Semana 1 — Fundamentos e ZCU

**Objetivo:** dominar navegação, conceitos básicos e operação visual.

- Fase principal: **ZCU Core**.
- Missões extras recomendadas: **Monitoring**, **Services**, **Inventory**.
- Tópicos: Server, Proxy, Database, Frontend, Agent, portas padrão, Problems, Latest data, Dashboards, Maps, tags, severidade e maintenance.

**Meta:** concluir ZCU Core e refazer todos os erros.

### Semana 2 — ZCS: itens e coleta

**Objetivo:** entender como o Zabbix coleta dados.

- Fase principal: início da **ZCS Core**.
- Missão extra recomendada: **Data Collection**.
- Tópicos: item types, Zabbix agent, SNMP agent, HTTP agent, Database monitor, key, intervalo, tipo de informação, history e trends.

**Meta:** explicar a diferença entre item agent, SNMP, HTTP, dependent e database monitor.

### Semana 3 — ZCS: triggers, templates e alertas

**Objetivo:** transformar dados coletados em detecção de problemas.

- Fase principal: continuação da **ZCS Core**.
- Missão extra recomendada: **Alerts**.
- Tópicos: trigger expression, `last`, `min`, `avg`, `nodata`, problem expression, recovery expression, hysteresis, severidade, templates, actions e media types.

**Meta:** escrever e explicar pelo menos 5 expressões de trigger.

### Semana 4 — ZCS: revisão prática

**Objetivo:** consolidar configuração básica e intermediária.

- Refaça todos os desafios ZCS errados.
- Faça as missões extras: **Users**, **Administration**, **Reports**.
- Tópicos: user groups, roles, audit log, availability report, manutenção e organização por host groups.

**Meta:** fazer um simulado ZCU + ZCS sem consultar gabarito.

### Semana 5 — ZCP: LLD e descoberta

**Objetivo:** dominar descoberta automática.

- Fase principal: início da **ZCP Core**.
- Tópicos: LLD rules, item prototypes, trigger prototypes, graph prototypes, macros `{#MACRO}`, filtros, overrides, lost resources e discovery dependente.

**Meta:** explicar como um JSON de discovery vira itens e triggers reais.

### Semana 6 — ZCP: proxy, escala e preprocessamento

**Objetivo:** preparar raciocínio de ambientes distribuídos.

- Continuação da **ZCP Core**.
- Tópicos: active proxy vs passive proxy, auto-registration, preprocessing pipeline, discard unchanged, dependent item, history vs trends e correlação de eventos.

**Meta:** resolver cenários de filial, NAT, limitação de API e ruído de eventos.

### Semana 7 — ZCP: automação e API

**Objetivo:** conectar automação com operação.

- Missão extra: **Automação API**.
- Missão extra: **Ansible**.
- Tópicos: endpoint `api_jsonrpc.php`, JSON-RPC, `host.get`, `host.create`, `host.update`, API token, idempotência, `community.zabbix` e manutenção automatizada.

**Meta:** desenhar um fluxo idempotente de onboarding de hosts.

### Semana 8 — ZCE: segurança e autenticação

**Objetivo:** entender segurança de plataforma e acesso.

- Fase principal: início da **ZCE Core**.
- Missões extras: **Segurança** e **Autenticação**.
- Tópicos: TLS, PSK, certificados, `TLSConnect`, `TLSAccept`, LDAP, SAML, MFA, API tokens, roles, user groups, break-glass e multi-tenant.

**Meta:** separar autenticação, autorização e integração em cenários multi-sistema.

### Semana 9 — ZCE: performance e processos internos

**Objetivo:** diagnosticar gargalos.

- Continuação da **ZCE Core**.
- Tópicos: queue, pollers, cache, preprocessors, DB performance, partitioning, history syncers, NVPS conceitual e tuning de coleta.

**Meta:** explicar queue alta com pelo menos 3 causas possíveis e 3 ações de mitigação.

### Semana 10 — Integrações: AWS, Azure e Bancos

**Objetivo:** aplicar Zabbix em ecossistemas corporativos.

- Missões extras: **AWS**, **Azure**, **Bancos de Dados**.
- Tópicos: AWS by HTTP, IAM policy, assume role, CloudWatch, RDS discovery, Azure service principal, macros Azure, Azure cost management, Database monitor, unixODBC, DSN, `odbcinst.ini` e `odbc.ini`.

**Meta:** explicar por que Zabbix API token não substitui IAM AWS, service principal Azure ou credencial ODBC.

### Semana 11 — Revisão integrada

**Objetivo:** simular prova e operação real.

- Refazer todos os erros do eixo principal.
- Refazer desafios de Autenticação, Segurança, LLD e API.
- Criar mapa mental com 4 blocos: coleta, detecção, notificação e segurança/automação.

**Meta:** identificar rapidamente se um problema é de coleta, trigger, autorização, API, banco ou cloud.

### Semana 12 — Simulado final

**Objetivo:** consolidar confiança.

- Fazer sequência completa sem consultar gabarito.
- Revisar somente erros.
- Consultar documentação oficial dos tópicos errados.
- Repetir os desafios errados até atingir 90%+ de acerto.

**Meta:** estar confortável explicando cada resposta em voz alta, como se estivesse ensinando outra pessoa.

## 4. Cronograma acelerado de 4 semanas

Use este cronograma se você já trabalha com Zabbix e precisa revisar rapidamente.

- **Semana 1:** ZCU completo + ZCS itens, triggers, templates e actions.
- **Semana 2:** ZCP com LLD, proxy, discovery, preprocessing e correlação.
- **Semana 3:** ZCE com segurança, autenticação, performance, API e processos internos.
- **Semana 4:** AWS, Azure, Bancos de Dados, simulado completo e revisão de erros.

## 5. Cronograma estendido de 16 semanas

Use este cronograma se você quer aprender com laboratório prático.

- **Semanas 1–2:** ZCU + operação visual.
- **Semanas 3–6:** ZCS completo com laboratório de itens, triggers e templates.
- **Semanas 7–9:** ZCP com LLD, proxy, discovery e automação.
- **Semanas 10–12:** ZCE com segurança, performance, API e troubleshooting.
- **Semanas 13–14:** integrações AWS, Azure e bancos.
- **Semana 15:** revisão de gaps.
- **Semana 16:** simulado final e revisão por documentação oficial.

## 6. Estratégia por certificação

### ZCU

Foque em interface, leitura de problemas, dashboards, filtros e conceitos básicos. A maior armadilha é confundir tela de operação com tela de configuração.

### ZCS

Foque em configuração prática. ZCS exige que você entenda como criar itens, triggers, templates e ações, além de conectar coleta com detecção e notificação.

### ZCP

Foque em escala e automação. O ponto crítico é entender LLD, proxies, discovery, preprocessamento e redução de ruído operacional.

### ZCE

Foque em arquitetura, segurança, performance e integração. A prova tende a exigir raciocínio sobre impactos: banco, queue, cache, TLS, API, HA e troubleshooting.

## 7. Dicas para certificações

### Dicas gerais

- Não decore apenas respostas: entenda por que as alternativas erradas estão erradas.
- Sempre pergunte: este cenário é de coleta, trigger, ação, permissão, autenticação ou integração?
- Leia os links oficiais das questões erradas.
- Refazer erro vale mais do que fazer questões novas sem revisar.
- Explique os conceitos em voz alta; se não conseguir explicar, ainda não consolidou.

### Dicas para ZCU

- Domine o fluxo: Problems → reconhecer evento → consultar Latest data → investigar host/template/tag.
- Saiba diferenciar dashboard, map, problems e reports.
- Entenda severidade e manutenção.

### Dicas para ZCS

- Treine criação mental de item: tipo, key, interface, tipo de informação, intervalo e retenção.
- Treine trigger: função, `/host/key`, período, operador e threshold.
- Entenda `nodata()`, hysteresis e recovery expression.
- Entenda quando usar SNMP, HTTP agent, Zabbix agent, dependent item e Database monitor.

### Dicas para ZCP

- Em LLD, sempre pense em: discovery rule → macros → prototypes → filters → overrides → lost resources.
- Em proxy, pense em quem inicia conexão e onde o dado fica armazenado se a WAN falhar.
- Em automação, pense em idempotência e consulta antes de criação.

### Dicas para ZCE

- Em performance, não chute: identifique se o gargalo é poller, trapper, preprocessor, cache, banco ou rede.
- Em segurança, diferencie TLS interno, HTTPS do frontend, autenticação de usuário e autorização de API.
- Em integrações, separe identidades: API token Zabbix, IAM AWS, service principal Azure e usuário ODBC.

## 8. Checklists de revisão

### Checklist ZCU

- [ ] Sei identificar Server, Proxy, DB, Frontend e Agent.
- [ ] Sei as portas padrão 10051 e 10050.
- [ ] Sei usar Problems, Latest data e dashboards.
- [ ] Sei interpretar severidade e tags.
- [ ] Sei o objetivo de maintenance.

### Checklist ZCS

- [ ] Sei escolher item type correto.
- [ ] Sei configurar key e type of information.
- [ ] Sei explicar history vs trends.
- [ ] Sei criar trigger com função, período e threshold.
- [ ] Sei explicar recovery expression e hysteresis.
- [ ] Sei usar templates e actions.

### Checklist ZCP

- [ ] Sei explicar LLD completo.
- [ ] Sei usar filters e overrides.
- [ ] Sei diferenciar active e passive proxy.
- [ ] Sei explicar dependent items e preprocessing.
- [ ] Sei planejar automação idempotente.

### Checklist ZCE

- [ ] Sei diagnosticar queue alta.
- [ ] Sei explicar processos internos.
- [ ] Sei diferenciar TLS, PSK, certificados e HTTPS.
- [ ] Sei explicar API tokens e permissões.
- [ ] Sei separar credenciais Zabbix, AWS, Azure e banco.

## 9. Como simular prova

1. Escolha a certificação alvo.
2. Faça todos os desafios daquela fase sem consultar gabarito.
3. Marque questões incertas, mesmo que tenha acertado.
4. Revise explicações e links oficiais.
5. Refaça apenas questões erradas no dia seguinte.
6. Só considere o tópico dominado quando conseguir explicar a resposta sem olhar.

### Critério sugerido de prontidão

- **Abaixo de 70%:** ainda está em fase de aprendizado.
- **70% a 84%:** revise tópicos fracos.
- **85% a 94%:** bom nível de preparação.
- **95% ou mais:** pronto para simulado final e revisão leve.

## 10. Plano de reforço por dificuldade

### Se errar itens e coleta

Estude: item types, key, interface, tipo de informação, preprocessing e dependent items.

### Se errar triggers

Estude: funções, períodos, `#N` vs tempo, hysteresis, recovery expression e `nodata()`.

### Se errar LLD

Estude: discovery rules, macros `{#MACRO}`, prototypes, filters, overrides e lost resources.

### Se errar segurança/autenticação

Estude: user types, roles, user groups, host group permissions, LDAP/SAML/MFA, API tokens, break-glass e segregação de credenciais.

### Se errar cloud/bancos

Estude: AWS IAM, CloudWatch, Azure service principal, macros Azure, ODBC, DSN e permissões SQL.

## 11. Referências oficiais

- Zabbix Training: https://www.zabbix.com/training_courses_core
- Zabbix Exams: https://www.zabbix.com/exams
- Zabbix Documentation 7.0: https://www.zabbix.com/documentation/7.0/en/manual
- Zabbix API: https://www.zabbix.com/documentation/7.0/en/manual/api
- Zabbix Authentication: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- Zabbix API tokens: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- Zabbix Permissions: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- Zabbix LLD: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- Zabbix AWS integration: https://www.zabbix.com/integrations/aws
- Zabbix Azure integration: https://www.zabbix.com/integrations/azure
- Zabbix Database monitor: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
