# Zabbix Detective: A Missão

**Zabbix Detective: A Missão** é um jogo/simulador educacional em Django para preparação progressiva nas certificações **ZCU**, **ZCS**, **ZCP** e **ZCE**, com fases extras de aprendizado prático sobre Segurança, Autenticação, Automação, Ansible, AWS, Azure e Bancos de Dados.

> **Aviso importante:** este projeto é uma ferramenta independente de estudo e simulação. Ele não é material oficial da Zabbix LLC e não garante aprovação automática em exame. A proposta é cobrir, de forma prática e orientada por documentação oficial, os tópicos públicos e competências esperadas para estudo.

## Sumário

- [Visão geral](#visão-geral)
- [Objetivos do projeto](#objetivos-do-projeto)
- [Guia de estudo e cronograma](#guia-de-estudo-e-cronograma)
- [Links para simulados](#links-para-simulados)
- [Fóruns e comunidades de estudo](#fóruns-e-comunidades-de-estudo)
- [Checklist de preparação](#checklist-de-preparação)
- [Dicas avançadas para ZCE](#dicas-avançadas-para-zce)
- [Plano de estudo ZCE](#plano-de-estudo-zce)
- [Triggers complexas](#triggers-complexas)
- [Plano de revisão semanal](#plano-de-revisão-semanal)
- [Dicas avançadas para ZCS](#dicas-avançadas-para-zcs)
- [Dicas rápidas para certificações](#dicas-rápidas-para-certificações)
- [Cobertura por certificação](#cobertura-por-certificação)
- [Eixo principal](#eixo-principal)
- [Missões extras](#missões-extras)
- [Como executar](#como-executar)
- [Estrutura técnica](#estrutura-técnica)
- [Regras de progresso](#regras-de-progresso)
- [Metodologia dos desafios](#metodologia-dos-desafios)
- [Documentação oficial de referência](#documentação-oficial-de-referência)
- [Gabarito completo](#gabarito-completo)
- [Checklist de validação](#checklist-de-validação)
- [Roadmap sugerido](#roadmap-sugerido)
- [Licença e uso](#licença-e-uso)

## Visão geral

- **Total de missões:** 19
- **Total de desafios:** 173
- **Desafios no eixo principal:** 62
- **Desafios em missões extras:** 111
- **Explicações com referência oficial:** 87

O jogo é dividido em duas áreas:

1. **Eixo principal de certificação**, com progressão de ZCU para ZCE.
2. **Missões extras no menu lateral**, voltadas a temas práticos e integrações reais.

## Objetivos do projeto

- Transformar estudo teórico em prática por cenários.
- Simular raciocínio de prova de certificação sem copiar questões oficiais.
- Explicar por que a alternativa correta é correta.
- Explicar por que as demais alternativas não atendem ao cenário.
- Guiar consulta à documentação oficial.
- Apoiar revisão de tópicos por área: itens, triggers, LLD, API, segurança, autenticação, cloud e banco de dados.

## Guia de estudo e cronograma

Foi adicionado um guia profissional de estudos no arquivo [`GUIA_ESTUDO.md`](GUIA_ESTUDO.md), com:

- cronograma principal de **12 semanas**;
- cronograma acelerado de **4 semanas**;
- cronograma estendido de **16 semanas**;
- rotina diária recomendada;
- estratégia por certificação;
- checklists ZCU, ZCS, ZCP e ZCE;
- plano de reforço por dificuldade;
- dicas de simulado e critérios de prontidão.

Resumo recomendado:

```text
Semanas 1-4   -> ZCU + ZCS
Semanas 5-7   -> ZCP + Automação + LLD
Semanas 8-9   -> ZCE + Segurança + Autenticação + Performance
Semana 10     -> AWS + Azure + Bancos de Dados
Semana 11     -> Revisão integrada
Semana 12     -> Simulado final
```

## Dicas rápidas para certificações

### ZCU

- Foque em operação visual, navegação e interpretação de problemas.
- Diferencie Problems, Latest data, Maps, Dashboards e Reports.
- Entenda componentes básicos, severidade, tags e maintenance.

### ZCS

- Foque em configuração prática: itens, triggers, templates, actions, SNMP, HTTP agent e preprocessing.
- Treine raciocínio de item: tipo, key, interface, tipo de informação, intervalo e retenção.
- Treine raciocínio de trigger: função, item, período, operador, threshold e recuperação.

### ZCP

- Foque em escala e automação: LLD, proxies, discovery, preprocessing, correlação e API.
- Entenda o fluxo LLD: discovery rule -> macros -> prototypes -> filters -> overrides -> lost resources.
- Pense sempre em idempotência quando o cenário envolver automação.

### ZCE

- Foque em arquitetura, segurança, performance, API, HA, banco e troubleshooting.
- Em performance, identifique se o gargalo está em poller, trapper, preprocessor, cache, banco ou rede.
- Em segurança, separe autenticação, autorização, TLS interno, HTTPS do frontend, API token e credenciais de integrações.

## Links para simulados

Foi adicionado o arquivo [`SIMULADOS.md`](SIMULADOS.md), com links para:

- exames oficiais da Zabbix;
- páginas oficiais de ZCU, ZCS e ZCP;
- simulado interno usando o próprio jogo;
- recursos externos de prática complementar;
- checklist antes de marcar o exame.

> Use simulados de terceiros apenas como complemento. A documentação oficial e os exames oficiais devem ser a fonte principal.

## Plano de revisão semanal

Foi adicionado o arquivo [`PLANO_REVISAO_SEMANAL.md`](PLANO_REVISAO_SEMANAL.md), com uma rotina semanal organizada por tema:

- segunda: fundamentos;
- terça: coleta e configuração;
- quarta: triggers e alertas;
- quinta: automação e escala;
- sexta: segurança e integrações;
- sábado: simulado curto;
- domingo: correção e revisão leve.

## Dicas avançadas para ZCS

Foi adicionado o arquivo [`DICAS_ZCS.md`](DICAS_ZCS.md), com foco específico em Zabbix Certified Specialist:

- itens e tipos de coleta;
- active vs passive checks;
- triggers, events, problems e actions;
- preprocessing;
- dependent items;
- SNMP e OID;
- maintenance vs acknowledge;
- checklist final de ZCS.

## Fóruns e comunidades de estudo

Foi adicionado o arquivo [`FORUNS_ESTUDO.md`](FORUNS_ESTUDO.md), com links para:

- comunidade oficial Zabbix;
- fórum oficial Zabbix;
- fóruns por tema, como Help, Troubleshooting, Large Environments e Português/Español;
- Reddit, GitHub e materiais complementares;
- modelo de como pedir ajuda corretamente sem expor dados sensíveis.

## Checklist de preparação

Foi adicionado o arquivo [`CHECKLIST_PREPARACAO.md`](CHECKLIST_PREPARACAO.md), com checklists para:

- preparação geral;
- ZCU;
- ZCS;
- ZCP;
- ZCE;
- revisão 24 horas antes do exame;
- critério de prontidão por percentual de acerto.

## Dicas avançadas para ZCE

Foi adicionado o arquivo [`DICAS_ZCE.md`](DICAS_ZCE.md), com foco específico em Zabbix Certified Expert:

- performance;
- segurança;
- arquitetura;
- integrações;
- troubleshooting;
- rollback;
- API e idempotência;
- laboratórios recomendados.

## Plano de estudo ZCE

Foi adicionado o arquivo [`PLANO_ESTUDO_ZCE.md`](PLANO_ESTUDO_ZCE.md), com um plano focado em Zabbix Certified Expert:

- cronograma de **8 semanas**;
- rotina semanal específica para ZCE;
- laboratórios obrigatórios;
- checklist final;
- foco em arquitetura, performance, segurança, API, LLD, banco, cloud e troubleshooting.

## Triggers complexas

Foi adicionado o arquivo [`TRIGGERS_COMPLEXAS.md`](TRIGGERS_COMPLEXAS.md), com dicas práticas para criar, revisar e diagnosticar triggers complexas:

- problem expression vs recovery expression;
- hysteresis;
- `nodata()`;
- `10m` vs `#10`;
- dependencies;
- macros de threshold;
- exemplos de padrões úteis;
- checklist de revisão de triggers.

## Cobertura por certificação

### ZCU

- Operação básica da interface, navegação, Problems, Latest data, dashboards, manutenção e severidade.
- Conceitos de arquitetura: Server, Proxy, Database, Frontend, Agent e portas padrão.
- Noções de host groups, templates, tags e leitura operacional de eventos.

### ZCS

- Configuração de hosts, interfaces, itens, tipos de itens, SNMP, HTTP agent, Database monitor e preprocessing.
- Triggers, expressão de problema, recuperação, hysteresis, nodata, severidade e tags para roteamento.
- Templates, ações, notificações, LLD básico e dependent items.

### ZCP

- Automação, escala, proxies, auto-registration, correlação, discovery e LLD avançado.
- Prototypes, filters, overrides, lost resources, macros customizadas e discovery dependente.
- Histórico versus trends, throttling e preprocessamento em escala.

### ZCE

- Performance, queues, pollers, cache, processos internos, API, HA conceitual e tuning.
- Segurança avançada: TLS, PSK, certificados, autenticação, API tokens, permissões e segredos.
- Integrações enterprise e cenários multi-sistema com AWS, Azure, banco de dados, ITSM e automação.

## Eixo principal

### Fase 1 — ZCU: Fase 1: ZCU - Fundamentos e Operação Visual

- **Nível:** Básico
- **Desafios:** 11
- **Descrição:** Preparação para Zabbix Certified User: GUI, arquitetura, problemas, filtros, dashboards e conceitos essenciais.

### Fase 2 — ZCS: Fase 2: ZCS - Implantação e Configuração

- **Nível:** Intermediário
- **Desafios:** 21
- **Descrição:** Preparação para Zabbix Certified Specialist: instalação, hosts, itens, triggers, templates, ações, macros, SNMP e LLD básico.

### Fase 3 — ZCP: Fase 3: ZCP - Automação e Escala

- **Nível:** Avançado
- **Desafios:** 18
- **Descrição:** Preparação para Zabbix Certified Professional: proxy, LLD avançado, preprocessamento, correlação, discovery e ambientes distribuídos.

### Fase 4 — ZCE: Fase 4: ZCE - Expertise, Performance e Segurança

- **Nível:** Expert
- **Desafios:** 12
- **Descrição:** Preparação para Zabbix Certified Expert: tuning, HA, segurança, API, processos internos, bancos e troubleshooting avançado.

## Missões extras

### Monitoring

- **Categoria:** `monitoring`
- **Desafios:** 3
- **Descrição:** Treine Problems, Latest data, gráficos e reconhecimento de incidentes.

### Services

- **Categoria:** `services`
- **Desafios:** 3
- **Descrição:** Simulador de serviços, SLA, dependências e impacto no negócio.

### Inventory

- **Categoria:** `inventory`
- **Desafios:** 3
- **Descrição:** Treine inventário automático/manual e classificação de ativos.

### Reports

- **Categoria:** `reports`
- **Desafios:** 3
- **Descrição:** Missões de relatórios, disponibilidade, tendências e auditoria.

### Data collection

- **Categoria:** `data_collection`
- **Desafios:** 4
- **Descrição:** Treine itens, discovery, SNMP, HTTP agent e preprocessamento.

### Alerts

- **Categoria:** `alerts`
- **Desafios:** 4
- **Descrição:** Treine ações, media types, escalonamento e supressões.

### Users

- **Categoria:** `users`
- **Desafios:** 3
- **Descrição:** Treine usuários, grupos, roles e acesso por host group.

### Administration

- **Categoria:** `administration`
- **Desafios:** 3
- **Descrição:** Treine housekeeping, proxies, macros globais e auditoria.

### Automação API

- **Categoria:** `automation_api`
- **Desafios:** 10
- **Descrição:** Desafios práticos para automatizar operações do Zabbix: criar hosts, consultar dados, abrir manutenções, integrar incidentes e evitar automações perigosas.

### Segurança

- **Categoria:** `security`
- **Desafios:** 13
- **Descrição:** Laboratório lateral sobre TLS, PSK/certificados, autenticação, MFA, roles, menor privilégio, segredos e exposição segura do frontend.

### Ansible

- **Categoria:** `ansible`
- **Desafios:** 11
- **Descrição:** Laboratório lateral para automatizar Zabbix com playbooks, inventory, roles, community.zabbix, Vault, idempotência e pipeline de onboarding.

### AWS

- **Categoria:** `aws`
- **Desafios:** 8
- **Descrição:** Cenários reais de monitoramento AWS com Zabbix by HTTP, macros, IAM, CloudWatch, EC2, RDS, S3, Lambda e descoberta automática.

### Bancos de Dados

- **Categoria:** `databases`
- **Desafios:** 8
- **Descrição:** Cenários reais de integração com bancos via ODBC/Database monitor, drivers, DSN, queries, permissões, latência, filas e health checks.

### Azure

- **Categoria:** `azure`
- **Desafios:** 8
- **Descrição:** Cenários reais de monitoramento Azure by HTTP com service principal, macros, subscriptions, VMs, SQL, MySQL, PostgreSQL, Storage e Cost Management.

### Autenticação

- **Categoria:** `authentication`
- **Desafios:** 27
- **Descrição:** Cenários reais de autenticação e autorização envolvendo Zabbix, LDAP, SAML, MFA, API tokens, roles, user groups, AWS IAM, Azure service principal, banco de dados e ITSM.

## Como executar

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py runserver
```

Se o PowerShell bloquear a ativação:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

Depois acesse:

```text
http://127.0.0.1:8000/
```

### Linux/macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Estrutura técnica

```text
zabbix_detective_missao_v11/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── zabbix_detective/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── game/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    ├── templates/
    └── static/
```

## Regras de progresso

- O progresso é salvo em sessão do navegador.
- O eixo principal libera fases em sequência.
- As missões extras ficam disponíveis pelo menu lateral.
- Cada desafio concluído aumenta o progresso da fase/missão.
- O dashboard calcula a preparação geral com base nos desafios do eixo principal.

Campos de sessão usados:

```python
request.session['fase_atual']
request.session['desafios_concluidos']
```

## Metodologia dos desafios

Cada desafio segue a estrutura:

1. **Antes de responder** — introdução conceitual sem entregar a resposta.
2. **Questão prática** — cenário ou pergunta no estilo certificação.
3. **Alternativas ou formulário** — múltipla escolha, multiselect, resposta curta ou tela simulada.
4. **Pista de raciocínio** — exibida ao errar.
5. **Comentário estilo certificação** — exibido ao acertar.
6. **Referência oficial** — link para documentação, integração ou página oficial relacionada.

## Documentação oficial de referência

- Zabbix Documentation 7.0: https://www.zabbix.com/documentation/7.0/en/manual
- Items: https://www.zabbix.com/documentation/7.0/en/manual/config/items/item
- Item types: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes
- Trigger expressions: https://www.zabbix.com/documentation/7.0/en/manual/config/triggers/expression
- Preprocessing: https://www.zabbix.com/documentation/7.0/en/manual/config/items/preprocessing
- Low-level discovery: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- API: https://www.zabbix.com/documentation/7.0/en/manual/api
- Encryption: https://www.zabbix.com/documentation/7.0/en/manual/encryption
- Authentication: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- API tokens: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- Permissions: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- Database monitor / ODBC: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- AWS integration: https://www.zabbix.com/integrations/aws
- Azure integration: https://www.zabbix.com/integrations/azure
- Ansible community.zabbix: https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/index.html

## Gabarito completo

> O gabarito abaixo foi gerado a partir do banco `db.sqlite3` do projeto. Ele reflete exatamente os valores aceitos pela validação atual do jogo.

### Fase 1 — ZCU: Fase 1: ZCU - Fundamentos e Operação Visual

#### 1. Portas padrão Server e Agent

- **Tipo:** `formulario`
- **Pergunta:** Preencha as portas padrão usadas na comunicação básica.
- **Conceito/cenário:** Em uma questão de certificação, portas padrão costumam validar se você reconhece a função de cada componente. Pense em qual porta pertence ao serviço central de processamento e qual pertence ao agente instalado no host monitorado, sem confundir com porta de frontend, banco ou SNMP.
- **Resposta correta:** Porta do Zabbix Server: 10051 | Porta do Zabbix Agent: 10050
- **Pista ao errar:** Pista: pense no fluxo de comunicação entre o serviço central e o agente do host. Não use porta de HTTP/HTTPS, banco de dados ou SNMP.
- **Explicação:** Comentário: esta questão valida memorização operacional de comunicação básica. A porta do Server é usada pelo processo central do Zabbix, enquanto a porta do Agent pertence ao serviço instalado nos hosts monitorados. Portas de web, banco, SNMP ou SSH pertencem a outros fluxos e não respondem ao cenário.

#### 2. Componentes centrais

- **Tipo:** `multiselect`
- **Pergunta:** Selecione os componentes fundamentais da arquitetura Zabbix.
- **Conceito/cenário:** A arquitetura do Zabbix é formada por componentes que coletam, processam, armazenam e apresentam informações. Antes de responder, separe o que é componente da plataforma do que é apenas cliente de acesso do usuário.
- **Resposta correta:** Zabbix Server; Zabbix Proxy; Database; Frontend
- **Pista ao errar:** Pista: procure os elementos que fazem parte da própria plataforma Zabbix. Um navegador acessa uma tela, mas não processa coleta nem armazena dados do Zabbix.
- **Explicação:** Comentário: a alternativa correta separa componentes da solução Zabbix de elementos externos de acesso. Zabbix Server é o núcleo de processamento; Proxy permite coleta distribuída; Database armazena configuração, histórico e eventos; Frontend entrega a interface administrativa. O browser é apenas o cliente usado para acessar o Frontend, portanto não deve ser tratado como componente central da plataforma.

#### 3. Tela Problems

- **Tipo:** `multipla`
- **Pergunta:** Na tela Problems, qual ação do usuário reconhece que o evento foi visto e permite registrar comentário?
- **Conceito/cenário:** A operação diária depende de telas de observabilidade, como Problems, Latest data, Dashboards e Maps. Cada tela responde a uma pergunta operacional diferente.
- **Resposta correta:** Acknowledge
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Acknowledge é usado para reconhecer/acompanhar problema. Desabilitar trigger ou apagar item altera configuração e não é o fluxo operacional correto.

#### 4. Severidade de eventos

- **Tipo:** `multipla`
- **Pergunta:** Qual opção representa uma classificação de severidade do problema?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** High
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** High é uma severidade de problema. Item, Host group e Interface são objetos/configurações, não severidade.

#### 5. Dashboard e widgets

- **Tipo:** `multipla`
- **Pergunta:** Qual recurso agrupa widgets para visualização operacional rápida?
- **Conceito/cenário:** A operação diária depende de telas de observabilidade, como Problems, Latest data, Dashboards e Maps. Cada tela responde a uma pergunta operacional diferente.
- **Resposta correta:** Dashboard
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Dashboard agrega widgets como Problems, Graphs e Maps. Template padroniza configuração; Action executa notificação; Proxy coleta remotamente.

#### 6. Janela de manutenção

- **Tipo:** `multipla`
- **Pergunta:** Para evitar alertas durante uma parada planejada, o que deve ser configurado?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Maintenance period
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Maintenance define janela planejada e pode suprimir ações. Acknowledgement é manual; macro só parametriza; grupo não agenda parada.

#### 7. Filtros e tags

- **Tipo:** `multipla`
- **Pergunta:** Qual recurso ajuda a classificar problemas por aplicação, ambiente ou serviço?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Tags
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Tags permitem filtrar, correlacionar e rotear eventos. Interfaces são conexão; macros são variáveis; templates são herança.

#### 8. Problems vs Latest data

- **Tipo:** `multipla`
- **Pergunta:** Um operador precisa saber se existe um evento ativo aberto agora. Qual tela é mais adequada?
- **Conceito/cenário:** Perguntas de ZCU frequentemente testam navegação e objetivo de cada tela. Antes de escolher, diferencie tela de valores coletados, tela de eventos ativos e telas de configuração.
- **Resposta correta:** Problems
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: Problems é a tela orientada a eventos/problemas ativos. Latest data é usada para valores coletados de itens, mas não substitui a visão de incidentes. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual

#### 9. Host groups

- **Tipo:** `multipla`
- **Pergunta:** Qual é o principal objetivo de organizar hosts em host groups?
- **Conceito/cenário:** Em questões básicas, host group costuma aparecer como agrupamento lógico e base de permissão, não como mecanismo de coleta.
- **Resposta correta:** Organização, filtros e base para permissões
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: host groups ajudam a organizar hosts e também são usados em permissões e filtros. Eles não coletam métricas, não enviam alertas e não substituem templates. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/hosts
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/hosts

#### 10. Templates no nível usuário

- **Tipo:** `multipla`
- **Pergunta:** Por que templates são usados em Zabbix?
- **Conceito/cenário:** Pense em padronização: prova de usuário espera que o candidato saiba por que hosts herdam configuração pronta.
- **Resposta correta:** Reutilizar e padronizar monitoramento
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: templates permitem reutilizar configuração de monitoramento em muitos hosts, incluindo itens, triggers, gráficos e discovery. Criar tudo manualmente em cada host aumenta erro operacional. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/templates
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/templates

#### 11. Maintenance e ações

- **Tipo:** `multipla`
- **Pergunta:** Uma janela de manutenção planejada foi configurada para um host. Qual é o resultado esperado no fluxo de alertas?
- **Conceito/cenário:** Quando a questão fala em parada planejada, procure o recurso próprio de janela programada, não uma ação manual pós-incidente.
- **Resposta correta:** Reduzir/suprimir alertas planejados conforme configuração
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: Maintenance representa parada planejada e pode evitar ruído operacional durante a janela. Acknowledge reconhece um evento já existente, enquanto manutenção é preventiva. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/maintenance
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/maintenance

### Fase 2 — ZCS: Fase 2: ZCS - Implantação e Configuração

#### 1. Criar item de CPU

- **Tipo:** `formulario`
- **Pergunta:** Na tela simulada de Items, configure um item de CPU.
- **Conceito/cenário:** Em itens do Zabbix, a prova costuma avaliar se você sabe escolher o tipo de item, a key e o tipo de dado armazenado. Para métricas percentuais, considere se o valor pode ter casas decimais e se será usado em gráficos e triggers.
- **Resposta correta:** Key: system.cpu.util | Type of information: Numeric float
- **Pista ao errar:** Pista: a métrica de utilização normalmente é percentual e pode ter casas decimais. Evite escolher um tipo que transforme o valor em texto ou descarte precisão.
- **Explicação:** Comentário: a configuração correta precisa alinhar key, semântica da métrica e tipo de armazenamento. A key escolhida deve representar utilização de CPU, e o tipo numérico com ponto flutuante preserva valores percentuais com casas decimais. Tipos textuais impedem cálculos corretos, e inteiro sem sinal pode perder precisão.

#### 2. Tipo de item para agente

- **Tipo:** `multipla`
- **Pergunta:** Para coletar uma métrica via agente instalado no host, qual tipo de item é mais direto?
- **Conceito/cenário:** Itens são a base da coleta no Zabbix. Cada item precisa ter tipo de coleta, key ou identificador, tipo de informação, intervalo e retenção coerentes com a métrica.
- **Resposta correta:** Zabbix agent
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Zabbix agent é o tipo nativo. SNMP é para dispositivos/serviços SNMP; HTTP agent consulta endpoints; Calculated calcula a partir de outros itens.

#### 3. Trigger CPU alta

- **Tipo:** `texto`
- **Pergunta:** Digite uma expressão que dispare quando o último valor de CPU for maior que 90%. Use Host e system.cpu.util.
- **Conceito/cenário:** Triggers avaliam valores dos itens e decidem quando uma condição vira problema. Pense sempre em função, item, operador, limite, severidade e recuperação.
- **Resposta correta:** last(/Host/system.cpu.util)>90
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** last(/Host/system.cpu.util)>90 compara o último valor coletado contra 90. Usar < inverteria o problema; usar item diferente monitoraria outro recurso.

#### 4. Herança por template

- **Tipo:** `multipla`
- **Pergunta:** Qual objeto deve receber itens/triggers reutilizáveis para muitos hosts Linux?
- **Conceito/cenário:** Templates padronizam monitoramento, evitando configurar item e trigger manualmente em cada host. Eles são essenciais para escala e consistência.
- **Resposta correta:** Template
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Template centraliza itens/triggers/gráficos para herança. Criar tudo direto em cada host aumenta retrabalho e inconsistência.

#### 5. Ações e notificações

- **Tipo:** `multipla`
- **Pergunta:** Qual objeto define condições e operações para enviar alertas?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Action
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Action avalia condições e executa operações como mensagem, script remoto ou escalonamento. Media type define canal, mas não a regra completa.

#### 6. SNMP em switch

- **Tipo:** `formulario`
- **Pergunta:** Configure um item básico para coletar via SNMP.
- **Conceito/cenário:** Em coleta SNMP, a prova tende a diferenciar key de agente Zabbix, OID SNMP e interface do host. A resposta deve refletir o tipo de item correto e o identificador SNMP solicitado pelo cenário.
- **Resposta correta:** Type: SNMP agent | SNMP OID: 1.3.6.1.2.1.1.3.0
- **Pista ao errar:** Pista: em SNMP, o identificador da métrica é um OID, não uma key de agente. O tipo de item precisa corresponder ao protocolo do dispositivo.
- **Explicação:** SNMP agent usa OID. OID 1.3.6.1.2.1.1.3.0 representa sysUpTime em MIB-II; key de agente Zabbix não é usada para SNMP puro.

#### 7. LLD básico

- **Tipo:** `multipla`
- **Pergunta:** Qual recurso descobre automaticamente interfaces, discos ou serviços e cria protótipos?
- **Conceito/cenário:** Discovery automatiza a criação de entidades repetitivas, como discos, interfaces e serviços. Macros LLD carregam valores descobertos para protótipos.
- **Resposta correta:** Low-Level Discovery
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Low-Level Discovery cria entidades a partir de regras e protótipos. Network discovery acha hosts; template herda configuração; action dispara operações.

#### 8. Item: Numeric float vs unsigned

- **Tipo:** `multipla`
- **Pergunta:** Um item retorna 37.85% de uso de memória. Qual Type of information preserva o valor corretamente?
- **Conceito/cenário:** Itens são a base da coleta no Zabbix. Cada item precisa ter tipo de coleta, key ou identificador, tipo de informação, intervalo e retenção coerentes com a métrica.
- **Resposta correta:** Numeric float
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Numeric float preserva casas decimais; Numeric unsigned converteria o valor para inteiro, perdendo precisão. Character e Text impedem cálculos numéricos e uso adequado em triggers.

#### 9. Item: intervalo de atualização

- **Tipo:** `multipla`
- **Pergunta:** Você precisa coletar uma métrica a cada minuto. Qual valor é adequado no Update interval?
- **Conceito/cenário:** Itens são a base da coleta no Zabbix. Cada item precisa ter tipo de coleta, key ou identificador, tipo de informação, intervalo e retenção coerentes com a métrica.
- **Resposta correta:** 1m
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** O campo Update interval aceita sufixos de tempo como 1m. Valores muito baixos aumentam NVPS e carga; 1d seria lento para alerta operacional.

#### 10. Item: chave única

- **Tipo:** `multipla`
- **Pergunta:** Dentro de um mesmo host, o que deve ser verdadeiro sobre a Key do item?
- **Conceito/cenário:** Itens são a base da coleta no Zabbix. Cada item precisa ter tipo de coleta, key ou identificador, tipo de informação, intervalo e retenção coerentes com a métrica.
- **Resposta correta:** Deve ser única no host
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** A key deve ser única dentro de um host; duplicar keys no mesmo host causa conflito de configuração. O nome visual pode mudar, mas a key identifica a coleta.

#### 11. Trigger: sintaxe base

- **Tipo:** `texto`
- **Pergunta:** Digite uma expressão simples para problema quando CPU do Host for maior que 90 usando last.
- **Conceito/cenário:** Uma trigger transforma dados coletados em condição de problema. A expressão combina uma função, um item no formato /host/key, um operador e um limite.
- **Resposta correta:** last(/Host/system.cpu.util)>90
- **Pista ao errar:** Use a estrutura função(/Host/key)>limite. A função pedida é last e a key é system.cpu.util.
- **Explicação:** Comentário: uma trigger válida combina função, item, operador e limiar. Nesta questão, last avalia o valor mais recente do item informado. O operador maior que representa condição de problema acima do limite. Inverter o operador mudaria completamente o significado do alerta.

#### 12. Trigger: recuperação e hysteresis

- **Tipo:** `multipla`
- **Pergunta:** Por que usar expressão de recuperação separada em uma trigger?
- **Conceito/cenário:** Métricas próximas de um limite podem oscilar e gerar abre/fecha de eventos. Hysteresis usa critérios diferentes para problema e recuperação para reduzir ruído.
- **Resposta correta:** Evitar flapping/oscilação
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Comentário: hysteresis é usado para evitar flapping. Em prova, quando o cenário fala em métrica oscilando perto do limite, a melhor resposta tende a envolver expressão de recuperação ou limites diferentes para abertura e fechamento do problema.

#### 13. Trigger: nodata

- **Tipo:** `multipla`
- **Pergunta:** Qual função é adequada para detectar que um item parou de receber dados?
- **Conceito/cenário:** Além de valores altos ou baixos, monitoramento também precisa detectar ausência de coleta. Para isso existe função específica para falta de dados.
- **Resposta correta:** nodata()
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Comentário: ausência de dados não é igual a valor baixo ou alto. A função nodata foi criada para detectar interrupção de coleta em uma janela de tempo. Funções como last, avg ou min operam sobre valores recebidos e não resolvem diretamente o caso de silêncio de coleta.

#### 14. Trigger: severidade correta

- **Tipo:** `multipla`
- **Pergunta:** Uma trigger de serviço indisponível para produção deve receber severidade operacional compatível com impacto. Qual opção é mais apropriada que Info?
- **Conceito/cenário:** Triggers avaliam valores dos itens e decidem quando uma condição vira problema. Pense sempre em função, item, operador, limite, severidade e recuperação.
- **Resposta correta:** High
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** High/Disaster comunicam impacto maior. Info/Warning podem subestimar incidentes críticos e dificultar priorização no NOC.

#### 15. Tags para roteamento

- **Tipo:** `multipla`
- **Pergunta:** Qual par de tags ajuda a rotear alertas por time e ambiente?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** service=database, env=prod
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Tags como service e env permitem filtros, actions condicionais e dashboards. Chaves aleatórias sem significado enfraquecem roteamento e relatórios.

#### 16. Item type: HTTP agent

- **Tipo:** `multipla`
- **Pergunta:** Uma aplicação expõe JSON em um endpoint HTTPS e não há agente instalado no servidor da aplicação. Qual tipo de item é mais adequado?
- **Conceito/cenário:** Em prova, identifique primeiro o método de aquisição de dados. Se o cenário fala em endpoint HTTP/JSON, procure um tipo de item compatível com HTTP.
- **Resposta correta:** HTTP agent
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: HTTP agent é indicado quando a coleta será feita por requisição HTTP/HTTPS a um endpoint. Zabbix agent exige agente no host; SNMP exige dispositivo/serviço SNMP; Calculated depende de outros itens já existentes. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes

#### 17. Preprocessing: ordem das etapas

- **Tipo:** `multipla`
- **Pergunta:** Um item possui duas etapas de preprocessamento. Como o Zabbix processa essas etapas?
- **Conceito/cenário:** Questões de preprocessamento costumam avaliar pipeline: uma transformação pode preparar o valor para a próxima.
- **Resposta correta:** Na ordem configurada
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: etapas de preprocessamento são executadas na ordem em que estão configuradas. Isso importa quando uma etapa transforma o formato que a próxima etapa irá consumir. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/preprocessing
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/preprocessing

#### 18. Preprocessing: falha e unsupported

- **Tipo:** `multipla`
- **Pergunta:** Se uma etapa de preprocessamento falhar sem tratamento customizado, qual efeito pode ocorrer no item?
- **Conceito/cenário:** Procure a consequência operacional de uma transformação falhar antes do valor ser armazenado.
- **Resposta correta:** O item pode ficar unsupported
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: falha de preprocessamento pode tornar o item unsupported. A opção Custom on fail permite descartar valor, definir valor customizado ou mensagem de erro dependendo da transformação. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/preprocessing
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/preprocessing

#### 19. Trigger: tempo vs quantidade de valores

- **Tipo:** `multipla`
- **Pergunta:** Em uma função de trigger, qual é a diferença conceitual entre usar `10m` e `#10` como parâmetro?
- **Conceito/cenário:** Leia o símbolo antes do número. Em expressões de trigger, sufixo de tempo e cardinalidade de valores não são a mesma coisa.
- **Resposta correta:** 10m é janela de tempo; #10 é quantidade de valores
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: parâmetros como 10m indicam janela de tempo; parâmetros com # indicam quantidade de valores. Essa diferença é importante em funções como sum, avg, min e também no comportamento de last com valores anteriores. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/triggers/expression
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/triggers/expression

#### 20. Trigger: problem e recovery expression

- **Tipo:** `multipla`
- **Pergunta:** Quando uma trigger possui problem expression e recovery expression, como a recuperação é avaliada?
- **Conceito/cenário:** Foque no estado de recuperação: não basta apenas a condição de problema deixar de ser verdadeira quando há expressão de recuperação adicional.
- **Resposta correta:** Problem falsa e recovery verdadeira
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: com recovery expression, a resolução exige que a problem expression seja falsa e que a recovery expression seja verdadeira. Isso permite hysteresis e reduz flapping. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/triggers/expression
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/triggers/expression

#### 21. Dependent item e master item

- **Tipo:** `multipla`
- **Pergunta:** Qual é a relação correta entre dependent item e master item?
- **Conceito/cenário:** Pense em coleta única, múltiplas métricas derivadas. O dependent item não coleta diretamente do alvo como um agent/SNMP comum.
- **Resposta correta:** Usa o valor de um master item
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: um dependent item recebe valor a partir de um master item e aplica preprocessamento para derivar uma métrica. Isso reduz coletas redundantes quando uma chamada retorna múltiplos dados. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/dependent_items
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/dependent_items

### Fase 3 — ZCP: Fase 3: ZCP - Automação e Escala

#### 1. Macro LLD

- **Tipo:** `texto`
- **Pergunta:** Qual macro LLD comum identifica o nome de um filesystem descoberto?
- **Conceito/cenário:** Discovery automatiza a criação de entidades repetitivas, como discos, interfaces e serviços. Macros LLD carregam valores descobertos para protótipos.
- **Resposta correta:** {#FSNAME}
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** {#FSNAME} é uma macro LLD comum para nomes de filesystem. Macros de usuário como {$FS} são parametrização manual, não resultado da descoberta.

#### 2. Item dependente

- **Tipo:** `multipla`
- **Pergunta:** Quando várias métricas vêm de um JSON mestre, qual item reduz coleta duplicada?
- **Conceito/cenário:** Itens dependentes reutilizam dados de um item mestre. Eles são úteis quando uma única chamada retorna JSON/XML com várias métricas.
- **Resposta correta:** Dependent item
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Item dependent reutiliza o valor do item mestre e aplica preprocessamento. Isso reduz chamadas externas e melhora performance.

#### 3. Preprocessamento JSONPath

- **Tipo:** `formulario`
- **Pergunta:** Extraia o campo status de um JSON como {"status":"ok"}.
- **Conceito/cenário:** Em preprocessamento, a prova geralmente testa a capacidade de escolher a técnica certa para o formato recebido. Para JSON, pense em uma expressão que selecione o campo desejado, sem recorrer a parsing manual desnecessário.
- **Resposta correta:** JSONPath: $.status
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** $.status seleciona diretamente o campo status. Regex funcionaria em alguns casos, mas JSONPath é o método semântico correto para JSON.

#### 4. Proxy em ambiente distribuído

- **Tipo:** `multipla`
- **Pergunta:** Qual componente coleta em filial remota e envia dados ao servidor central?
- **Conceito/cenário:** Zabbix Proxy permite coleta distribuída e buffer local em redes remotas, reduzindo dependência de conexão direta contínua com o Server.
- **Resposta correta:** Zabbix Proxy
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Zabbix Proxy coleta e armazena localmente dados temporários para enviar ao Server. Frontend apenas apresenta a interface.

#### 5. Correlação de eventos

- **Tipo:** `multipla`
- **Pergunta:** Qual objetivo principal da correlação de eventos?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Reduzir ruído e relacionar eventos
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Correlação reduz ruído fechando/suprimindo eventos relacionados. Não substitui banco, não altera porta e não coleta métrica.

#### 6. Auto-registration

- **Tipo:** `multipla`
- **Pergunta:** Qual recurso cadastra hosts automaticamente quando agentes ativos se apresentam ao servidor?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Auto-registration
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Auto-registration usa agentes ativos e ações para cadastrar/configurar hosts. Network discovery varre rede; LLD descobre entidades dentro do host.

#### 7. History vs Trends

- **Tipo:** `multipla`
- **Pergunta:** Para consultas históricas longas com menor granularidade, qual estrutura é mais adequada?
- **Conceito/cenário:** Ambientes grandes precisam equilibrar histórico detalhado, trends agregadas, retenção e performance do banco de dados.
- **Resposta correta:** Trends
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Trends consolidam dados para períodos longos. History guarda dados brutos mais granulares e tende a crescer mais rapidamente.

#### 8. LLD: prototypes

- **Tipo:** `multiselect`
- **Pergunta:** Em LLD, quais objetos podem ser criados automaticamente por prototypes comuns?
- **Conceito/cenário:** Quando a pergunta fala em criar objetos repetitivos para interfaces e filesystems, pense em prototypes gerados a partir da descoberta.
- **Resposta correta:** Item prototypes; Trigger prototypes; Graph prototypes
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: LLD usa discovery rules e prototypes, como item prototypes, trigger prototypes e graph prototypes, para criar objetos por entidade descoberta. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery

#### 9. LLD: formato de dados

- **Tipo:** `multipla`
- **Pergunta:** Qual formato uma discovery rule de LLD normalmente retorna para representar entidades descobertas?
- **Conceito/cenário:** Observe a relação entre descoberta e macros LLD. A entrada da criação automática é um conjunto de entidades descobertas.
- **Resposta correta:** JSON com objetos de entidades e macros LLD
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: a regra de descoberta retorna JSON descrevendo entidades, normalmente com macros no formato {#MACRO}, que serão usadas nos prototypes. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery

#### 10. LLD: lost resources

- **Tipo:** `multipla`
- **Pergunta:** Por que usar “Delete lost resources: Immediately” tende a ser arriscado?
- **Conceito/cenário:** Em prova avançada, preserve dados e evite decisões irreversíveis quando discovery pode mudar por erro de filtro.
- **Resposta correta:** Pode remover entidades/histórico por erro de filtro
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: remover imediatamente entidades não descobertas pode apagar objetos e histórico se um filtro for configurado incorretamente. Em ambientes reais, disable/delete com atraso reduz risco. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery

#### 11. Preprocessing: discard unchanged

- **Tipo:** `multipla`
- **Pergunta:** Qual é o objetivo de usar “Discard unchanged” ou “Discard unchanged with heartbeat”?
- **Conceito/cenário:** Quando a questão fala em muitos valores repetidos, pense em reduzir escrita no banco sem perder visibilidade mínima.
- **Resposta correta:** Reduzir armazenamento de valores repetidos
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: throttling em preprocessamento ajuda a reduzir armazenamento descartando valores repetidos, com heartbeat garantindo atualização periódica mesmo sem mudança. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/preprocessing
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/preprocessing

#### 12. Correlação avançada

- **Tipo:** `multipla`
- **Pergunta:** Em um cenário com múltiplos eventos derivados da mesma causa raiz, qual objetivo de correlação é mais adequado?
- **Conceito/cenário:** Perguntas de correlação costumam envolver ruído operacional e relação entre eventos, não criação de métricas.
- **Resposta correta:** Fechar/suprimir eventos relacionados
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: correlação busca reduzir ruído e tratar eventos relacionados, por exemplo fechando ou suprimindo eventos dependentes quando uma causa raiz é identificada. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/event_correlation
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/event_correlation

#### 13. Proxy ativo em filial

- **Tipo:** `multipla`
- **Pergunta:** Em uma filial atrás de NAT, qual modo de proxy tende a simplificar a comunicação com o servidor central?
- **Conceito/cenário:** Observe quem consegue iniciar conexão. Em redes com NAT/firewall, modo ativo costuma facilitar o fluxo de saída.
- **Resposta correta:** Active proxy
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: em proxy ativo, o proxy se conecta ao server para buscar configuração e enviar dados, o que costuma ser mais simples em redes onde o server não consegue iniciar conexão até a filial. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/distributed_monitoring/proxies
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/distributed_monitoring/proxies

#### 14. LLD: filtro de filesystems

- **Tipo:** `multipla`
- **Pergunta:** Um template descobre filesystems temporários e gera alertas inúteis para tmpfs. Qual recurso da regra LLD deve ser usado para impedir a criação desses protótipos?
- **Conceito/cenário:** Cenário real: após aplicar um template Linux, o NOC passou a receber alertas de filesystems efêmeros. A solução deve agir antes da criação dos prototypes, não depois do alerta disparar.
- **Resposta correta:** Filters da discovery rule
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: filtros de LLD permitem gerar itens, triggers e gráficos apenas para entidades descobertas que correspondem a critérios definidos. Isso evita criar objetos para filesystems temporários ou irrelevantes. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery

#### 15. LLD: overrides

- **Tipo:** `multipla`
- **Pergunta:** Uma regra LLD deve manter triggers de disco para volumes de dados, mas desabilitar triggers para volumes de backup descobertos. Qual recurso é mais adequado?
- **Conceito/cenário:** Cenário real: nem toda entidade descoberta deve ter exatamente o mesmo tratamento. Procure o recurso que altera propriedades dos prototypes com base nas características descobertas.
- **Resposta correta:** Overrides da LLD
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: overrides de LLD permitem modificar itens, triggers, gráficos ou host prototypes quando determinadas condições de descoberta são atendidas. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery

#### 16. LLD: macro customizada via JSONPath

- **Tipo:** `multipla`
- **Pergunta:** Uma discovery rule retorna JSON com o campo `mountpoint`, mas não retorna `{#FSNAME}`. Como mapear esse valor para uso nos prototypes?
- **Conceito/cenário:** Cenário real: integrações customizadas nem sempre retornam macros LLD nativas. A solução é mapear campos do JSON para macros de descoberta.
- **Resposta correta:** Criar macro LLD customizada e mapear com JSONPath
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a aba LLD macros permite definir macros customizadas no formato {#MACRO} e extrair valores por JSONPath quando o JSON não traz macros prontas. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery

#### 17. LLD: discovery rule dependente

- **Tipo:** `multipla`
- **Pergunta:** Uma chamada HTTP retorna um JSON grande com discos, interfaces e serviços. Você quer extrair discovery de discos sem fazer nova chamada externa. Qual abordagem é mais eficiente?
- **Conceito/cenário:** Cenário real: APIs externas têm limite de requisições. Reaproveitar uma chamada mestre reduz custo e carga.
- **Resposta correta:** Discovery rule dependente de master item
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: uma discovery rule pode ser dependent item baseada em master item existente, evitando chamadas externas repetidas e usando preprocessamento para extrair a parte necessária. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery

#### 18. LLD: disable vs delete lost resources

- **Tipo:** `multipla`
- **Pergunta:** Um volume pode desaparecer temporariamente durante manutenção. Qual estratégia reduz risco de perda de histórico?
- **Conceito/cenário:** Cenário real: storage, volumes e interfaces podem sumir temporariamente. Em prova, preserve histórico e evite exclusão imediata.
- **Resposta correta:** Desabilitar com atraso e deletar somente após período seguro
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: campos Disable lost resources e Delete lost resources controlam o tratamento de entidades não descobertas. Desabilitar com atraso antes de deletar reduz risco de apagar histórico por ausência temporária ou filtro incorreto. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/discovery/low_level_discovery

### Fase 4 — ZCE: Fase 4: ZCE - Expertise, Performance e Segurança

#### 1. Queue alta no NOC

- **Tipo:** `multipla`
- **Pergunta:** Queue alta e pollers ocupados em 96%. Qual ajuste inicial faz sentido?
- **Conceito/cenário:** Queue alta indica atraso no processamento/coleta. Antes de alterar parâmetros, observe quais processos estão ocupados e se há pressão de cache ou banco. Dashboard: Queue 18.742, NVPS 1.280, Poller busy 96%.
- **Resposta correta:** StartPollers; CacheSize
- **Pista ao errar:** Queue alta com poller busy sugere investigar capacidade de polling e cache, não porta de escuta nem nome do banco.
- **Explicação:** Comentário: Queue alta com pollers ocupados indica gargalo de coleta/processamento. StartPollers aumenta capacidade de polling; CacheSize pode ajudar quando há pressão no cache de configuração/dados. ListenPort altera porta de escuta e DBName altera nome do banco, portanto não atacam o gargalo descrito.

#### 2. Alta disponibilidade

- **Tipo:** `multipla`
- **Pergunta:** Em HA do Zabbix Server, qual conceito identifica o nó que está processando ativamente?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Nó ativo
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** O nó ativo executa processamento. Nós standby aguardam failover. Banco e frontend não determinam sozinhos o nó ativo.

#### 3. Criptografia entre componentes

- **Tipo:** `multipla`
- **Pergunta:** Qual configuração é apropriada para criptografar comunicação entre componentes?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** TLS PSK/Certificate
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** TLS com PSK ou certificado protege comunicação. SNMP community não criptografa Zabbix interno; DBName e ListenPort não são segurança.

#### 4. Banco e performance

- **Tipo:** `multipla`
- **Pergunta:** Qual prática ajuda performance em grandes ambientes?
- **Conceito/cenário:** Ambientes grandes precisam equilibrar histórico detalhado, trends agregadas, retenção e performance do banco de dados.
- **Resposta correta:** Particionar/otimizar tabelas de histórico
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Particionamento/housekeeping bem dimensionado e índices adequados ajudam retenção e consultas. Aumentar só frontend não resolve escrita massiva no banco.

#### 5. Automação via API

- **Tipo:** `texto`
- **Pergunta:** Qual método da API é usado para criar host?
- **Conceito/cenário:** A API do Zabbix usa JSON-RPC sobre HTTP no frontend. Scripts devem autenticar com segurança, consultar estado atual e aplicar mudanças de forma rastreável.
- **Resposta correta:** host.create
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** host.create é o método de criação de host. item.create cria item; trigger.create cria trigger; user.login é autenticação legada.

#### 6. Segredos sensíveis

- **Tipo:** `multipla`
- **Pergunta:** Para gestão corporativa de segredos, qual abordagem é mais adequada?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Vault externo
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Vault externo como HashiCorp/CyberArk reduz exposição de credenciais. Guardar senha em comentário ou macro visível aumenta risco.

#### 7. Processos internos

- **Tipo:** `multipla`
- **Pergunta:** Qual processo está associado à execução de checks simples/agente/SNMP em paralelo?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Poller
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Pollers executam coletas. Escalators lidam com escalonamento, alerters com envio, housekeeper com limpeza.

#### 8. API: JSON-RPC

- **Tipo:** `multipla`
- **Pergunta:** Qual afirmação descreve corretamente a API do Zabbix?
- **Conceito/cenário:** Em questões de API, procure protocolo, endpoint e estrutura do objeto de requisição.
- **Resposta correta:** HTTP com JSON-RPC 2.0
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: a API é baseada em HTTP e usa JSON-RPC 2.0. Métodos como host.get, host.create e item.update são chamados via api_jsonrpc.php. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/api
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/api

#### 9. API: estrutura da requisição

- **Tipo:** `multiselect`
- **Pergunta:** Quais propriedades fazem parte de uma requisição JSON-RPC típica ao Zabbix?
- **Conceito/cenário:** Separe estrutura JSON-RPC de credenciais, URL e parâmetros de transporte.
- **Resposta correta:** jsonrpc; method; params; id
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: uma chamada JSON-RPC típica contém jsonrpc, method, params e id. Autenticação pode ser feita por API token ou token de login, mas esses quatro campos formam a estrutura da chamada. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/api
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/api

#### 10. Encryption: limitação importante

- **Tipo:** `multipla`
- **Pergunta:** Qual comunicação NÃO é protegida automaticamente pela criptografia interna entre componentes do Zabbix?
- **Conceito/cenário:** A questão diferencia TLS entre componentes Zabbix de HTTPS do frontend para usuários humanos.
- **Resposta correta:** Navegador do usuário ↔ web server do frontend
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: a criptografia interna do Zabbix não protege automaticamente o trecho navegador ↔ servidor web do frontend; para isso é necessário HTTPS no web server/reverso. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/encryption
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/encryption

#### 11. Encryption: firewall

- **Tipo:** `multipla`
- **Pergunta:** Ao habilitar TLS entre componentes Zabbix, o que acontece com as portas de escuta dos daemons?
- **Conceito/cenário:** Não confunda criptografia de transporte com criação automática de uma porta nova.
- **Resposta correta:** A mesma porta pode aceitar conexões criptografadas/não criptografadas conforme configuração
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: componentes Zabbix usam a mesma porta de escuta para conexões criptografadas e não criptografadas; adicionar criptografia não exige abrir novas portas apenas por causa do TLS. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/encryption
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/encryption

#### 12. API: autenticação

- **Tipo:** `multipla`
- **Pergunta:** Qual opção representa uma forma suportada de autenticação para acessar dados via API do Zabbix?
- **Conceito/cenário:** Procure a opção que representa autenticação da API, não credencial de SNMP ou senha exposta em código.
- **Resposta correta:** API token
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: a API pode usar API token criado no frontend ou Token API, ou token obtido via user.login. Para automação, API token com escopo adequado é preferível a senha hardcoded. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/api
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/api

### Missão extra — Monitoring: Monitoring: Sala de Problemas

#### 1. Achar problema crítico

- **Tipo:** `multipla`
- **Pergunta:** Qual tela é mais direta para operação diária de incidentes?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Problems
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Problems centraliza eventos ativos e ações de reconhecimento.

#### 2. Latest data

- **Tipo:** `multipla`
- **Pergunta:** Onde conferir último valor coletado de um item?
- **Conceito/cenário:** A operação diária depende de telas de observabilidade, como Problems, Latest data, Dashboards e Maps. Cada tela responde a uma pergunta operacional diferente.
- **Resposta correta:** Latest data
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Latest data mostra valores recentes por host/item.

#### 3. Maps

- **Tipo:** `multipla`
- **Pergunta:** Qual recurso é útil para topologia visual?
- **Conceito/cenário:** A operação diária depende de telas de observabilidade, como Problems, Latest data, Dashboards e Maps. Cada tela responde a uma pergunta operacional diferente.
- **Resposta correta:** Maps
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Maps mostra relações visuais e estado de elementos.

### Missão extra — Services: Services: SLA e Impacto

#### 1. SLA

- **Tipo:** `multipla`
- **Pergunta:** Qual conceito mede cumprimento do serviço ao longo do tempo?
- **Conceito/cenário:** Services conectam problemas técnicos a impacto de negócio, permitindo analisar disponibilidade, SLA e dependências entre serviços.
- **Resposta correta:** SLA
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** SLA mede disponibilidade/objetivo de serviço.

#### 2. Causa raiz

- **Tipo:** `multipla`
- **Pergunta:** Em árvore de serviço, dependências ajudam a identificar o quê?
- **Conceito/cenário:** Services conectam problemas técnicos a impacto de negócio, permitindo analisar disponibilidade, SLA e dependências entre serviços.
- **Resposta correta:** Impacto e propagação
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Dependências ajudam a calcular impacto e causa raiz.

#### 3. Tags em serviços

- **Tipo:** `multipla`
- **Pergunta:** Tags em serviços ajudam principalmente em:
- **Conceito/cenário:** Services conectam problemas técnicos a impacto de negócio, permitindo analisar disponibilidade, SLA e dependências entre serviços.
- **Resposta correta:** Filtro e classificação
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Tags facilitam filtragem, roteamento e relatórios.

### Missão extra — Inventory: Inventory: CMDB Operacional

#### 1. Inventário automático

- **Tipo:** `multipla`
- **Pergunta:** Qual modo preenche inventário a partir de itens?
- **Conceito/cenário:** Inventário ajuda a transformar hosts monitorados em ativos organizados, enriquecendo busca, CMDB e governança operacional.
- **Resposta correta:** Automatic
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Automático usa dados coletados para preencher campos.

#### 2. Campo de ativo

- **Tipo:** `multipla`
- **Pergunta:** Qual informação faz sentido no inventário?
- **Conceito/cenário:** Inventário ajuda a transformar hosts monitorados em ativos organizados, enriquecendo busca, CMDB e governança operacional.
- **Resposta correta:** Serial number
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Número de série é dado típico de ativo.

#### 3. Consulta CMDB

- **Tipo:** `multipla`
- **Pergunta:** Inventário é mais útil quando combinado com:
- **Conceito/cenário:** Inventário ajuda a transformar hosts monitorados em ativos organizados, enriquecendo busca, CMDB e governança operacional.
- **Resposta correta:** Host groups e tags
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Grupos e tags melhoram classificação e busca.

### Missão extra — Reports: Reports: Evidências e Capacidade

#### 1. Disponibilidade

- **Tipo:** `multipla`
- **Pergunta:** Qual relatório ajuda a observar disponibilidade de triggers/serviços?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Availability report
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Availability report agrega estado/disponibilidade.

#### 2. Capacidade

- **Tipo:** `multipla`
- **Pergunta:** Para planejamento de capacidade, qual dado consolidado é útil?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Trends
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Trends facilita análise de longo prazo.

#### 3. Auditoria

- **Tipo:** `multipla`
- **Pergunta:** Para descobrir quem alterou uma configuração, use:
- **Conceito/cenário:** Administração envolve saúde interna da plataforma: limpeza, auditoria, filas, proxies, configurações globais e governança.
- **Resposta correta:** Audit log
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Audit log registra alterações administrativas.

### Missão extra — Data collection: Data Collection: Laboratório de Coleta

#### 1. HTTP agent

- **Tipo:** `multipla`
- **Pergunta:** Para consultar endpoint REST sem agente local, use:
- **Conceito/cenário:** Itens são a base da coleta no Zabbix. Cada item precisa ter tipo de coleta, key ou identificador, tipo de informação, intervalo e retenção coerentes com a métrica.
- **Resposta correta:** HTTP agent
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** HTTP agent coleta dados via HTTP/HTTPS.

#### 2. Preprocessamento

- **Tipo:** `multipla`
- **Pergunta:** Para converter texto/JSON/XML antes de armazenar, use:
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Preprocessing
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Preprocessing transforma/valida valores antes do armazenamento.

#### 3. Master item

- **Tipo:** `multipla`
- **Pergunta:** Master + dependent items serve para:
- **Conceito/cenário:** Itens são a base da coleta no Zabbix. Cada item precisa ter tipo de coleta, key ou identificador, tipo de informação, intervalo e retenção coerentes com a métrica.
- **Resposta correta:** Reduzir chamadas externas
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Reduz chamadas e deriva várias métricas de uma coleta.

#### 4. HTTP agent e autenticação de API externa

- **Tipo:** `multipla`
- **Pergunta:** Um item HTTP agent consulta API de terceiros que exige bearer token. Esse token é o mesmo API token do Zabbix?
- **Conceito/cenário:** Cenário real: o Zabbix coleta dados de uma API externa. A autenticação da fonte monitorada é diferente da autenticação para administrar o Zabbix.
- **Resposta correta:** Não; a API externa usa segredo próprio
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: API token do Zabbix autentica chamadas contra a API do Zabbix. Uma API externa possui credencial própria; em cenários reais, armazene esse segredo separadamente e com escopo mínimo. Referência oficial Zabbix API: https://www.zabbix.com/documentation/7.0/en/manual/api
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/api

### Missão extra — Alerts: Alerts: Centro de Notificações

#### 1. Media type

- **Tipo:** `multipla`
- **Pergunta:** E-mail, webhook e SMS são exemplos de:
- **Conceito/cenário:** Alertas dependem de conditions, operations e media types. Uma boa configuração envia a mensagem certa para o destino certo, no momento certo.
- **Resposta correta:** Media type
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Media type define canal de envio.

#### 2. Escalonamento

- **Tipo:** `multipla`
- **Pergunta:** Enviar alerta para outro grupo após 15 minutos é:
- **Conceito/cenário:** Alertas dependem de conditions, operations e media types. Uma boa configuração envia a mensagem certa para o destino certo, no momento certo.
- **Resposta correta:** Escalation
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Escalation define passos e tempos de operação.

#### 3. Supressão

- **Tipo:** `multipla`
- **Pergunta:** Durante manutenção planejada, a melhor forma de evitar ruído é:
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Maintenance
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Maintenance é o mecanismo próprio para janelas planejadas.

#### 4. Alertas + SSO + grupos

- **Tipo:** `multipla`
- **Pergunta:** Um alerta de banco deve abrir chamado no ITSM e notificar somente o grupo DBA autenticado via SAML. Qual desenho é mais coerente?
- **Conceito/cenário:** Cenário real: identidade, autorização e roteamento de alerta são camadas diferentes.
- **Resposta correta:** Tags/user groups/actions para roteamento, SAML para login
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: autenticação SAML cuida do login; user groups/permissions controlam acesso; tags e actions podem rotear eventos para canais ou integrações. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication e https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

### Missão extra — Users: Users: Permissões e Papéis

#### 1. Permissões por grupo

- **Tipo:** `multipla`
- **Pergunta:** Permissões de host geralmente são atribuídas a:
- **Conceito/cenário:** Usuários, grupos e roles controlam quem pode ver ou alterar objetos. Em produção, prefira menor privilégio e rastreabilidade.
- **Resposta correta:** User group
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** User groups recebem permissões sobre host groups.

#### 2. Roles

- **Tipo:** `multipla`
- **Pergunta:** Roles controlam principalmente:
- **Conceito/cenário:** Usuários, grupos e roles controlam quem pode ver ou alterar objetos. Em produção, prefira menor privilégio e rastreabilidade.
- **Resposta correta:** Permissões de interface/funções
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Roles controlam acesso a funcionalidades da UI/API conforme perfil.

#### 3. MFA

- **Tipo:** `multipla`
- **Pergunta:** MFA aumenta:
- **Conceito/cenário:** Segurança em Zabbix combina criptografia, autenticação forte, segregação de permissões, proteção de segredos e auditoria das ações administrativas.
- **Resposta correta:** Segurança de autenticação
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Autenticação multifator aumenta segurança de login.

### Missão extra — Administration: Administration: Operações Avançadas

#### 1. Housekeeper

- **Tipo:** `multipla`
- **Pergunta:** Housekeeper é responsável por:
- **Conceito/cenário:** Administração envolve saúde interna da plataforma: limpeza, auditoria, filas, proxies, configurações globais e governança.
- **Resposta correta:** Limpeza de dados antigos
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Housekeeper remove dados antigos conforme retenção.

#### 2. Queue interna

- **Tipo:** `multipla`
- **Pergunta:** Queue alta sugere investigar:
- **Conceito/cenário:** Administração envolve saúde interna da plataforma: limpeza, auditoria, filas, proxies, configurações globais e governança.
- **Resposta correta:** Pollers/cache/banco
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Pollers, cache, banco e tipos de item podem causar atraso.

#### 3. Audit log

- **Tipo:** `multipla`
- **Pergunta:** Audit log ajuda em:
- **Conceito/cenário:** Administração envolve saúde interna da plataforma: limpeza, auditoria, filas, proxies, configurações globais e governança.
- **Resposta correta:** Rastrear mudanças
- **Pista ao errar:** Revise o conceito e compare com o objetivo da tela simulada.
- **Explicação:** Audit log rastreia alterações e ações administrativas.

### Missão extra — Automação API: Fase extra: Automação via API

#### 1. Endpoint da API JSON-RPC

- **Tipo:** `multipla`
- **Pergunta:** Você vai criar um script Python para falar com o Zabbix. Qual endpoint do frontend deve receber o POST JSON-RPC?
- **Conceito/cenário:** A API do Zabbix usa JSON-RPC sobre HTTP no frontend. Scripts devem autenticar com segurança, consultar estado atual e aplicar mudanças de forma rastreável.
- **Resposta correta:** https://zabbix.exemplo/zabbix/api_jsonrpc.php
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** O endpoint padrão da API é api_jsonrpc.php no frontend do Zabbix. A API usa HTTP POST com payload JSON-RPC. A página index.php é interface humana, e zabbix_server.conf não recebe chamadas HTTP.

#### 2. Token e autenticação segura

- **Tipo:** `multipla`
- **Pergunta:** Qual prática é mais adequada para um robô de automação chamar a API do Zabbix em produção?
- **Conceito/cenário:** Segurança em Zabbix combina criptografia, autenticação forte, segregação de permissões, proteção de segredos e auditoria das ações administrativas.
- **Resposta correta:** Usar API token armazenado em variável de ambiente/segredo
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** Usar token de API com escopo/role apropriado e armazenado como segredo é mais seguro e auditável do que gravar senha de Admin no código. O token deve ter menor privilégio possível.

#### 3. Criar host por API

- **Tipo:** `texto`
- **Pergunta:** Digite o método JSON-RPC usado para criar um host no Zabbix.
- **Conceito/cenário:** A API do Zabbix usa JSON-RPC sobre HTTP no frontend. Scripts devem autenticar com segurança, consultar estado atual e aplicar mudanças de forma rastreável.
- **Resposta correta:** host.create
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** host.create é o método da API de Host para criação. host.get consulta, host.update altera, item.create cria item e não host.

#### 4. Payload mínimo para onboarding

- **Tipo:** `multiselect`
- **Pergunta:** Para criar um host por API de forma útil, quais blocos normalmente precisam ir no params?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** host; groups; interfaces; templates
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** Um onboarding útil precisa do nome técnico do host, grupo, interface e template associado. Sem grupo/interface/template, o host pode ficar sem coleta ou sem organização operacional.

#### 5. Montar chamada Python segura

- **Tipo:** `formulario`
- **Pergunta:** Complete os elementos fundamentais de uma chamada Python para a API: método para listar hosts e cabeçalho Content-Type.
- **Conceito/cenário:** Em automação via API, perguntas de prova costumam avaliar método, endpoint, cabeçalho e payload. Para consultar recursos, diferencie métodos de leitura de métodos de criação ou alteração.
- **Resposta correta:** Método para listar hosts: host.get | Content-Type: application/json-rpc ou application/json
- **Pista ao errar:** Pista: para listar/consultar objetos, use método de leitura. Para o cabeçalho, escolha um tipo compatível com payload JSON/JSON-RPC.
- **Explicação:** host.get lista/consulta hosts. O cabeçalho deve declarar JSON ou JSON-RPC para o frontend interpretar a chamada corretamente. host.create criaria host e text/plain não representa o payload correto.

#### 6. Manutenção automatizada

- **Tipo:** `multipla`
- **Pergunta:** Um pipeline de deploy precisa silenciar alertas de um grupo por 30 minutos antes da mudança. Qual objeto da API deve ser automatizado?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação. Cenário: deploy de aplicação crítica às 22h, com rollback previsto e janela curta.
- **Resposta correta:** maintenance.create / maintenance.update
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** Maintenance é o objeto correto para janelas planejadas. Desabilitar triggers perde cobertura, acknowledge não evita novas ações automaticamente, e mudar severidade altera semântica do monitoramento.

#### 7. Ansible e idempotência

- **Tipo:** `multipla`
- **Pergunta:** Ao automatizar Zabbix com Ansible, qual princípio evita recriar hosts ou templates a cada execução?
- **Conceito/cenário:** Automação com Ansible deve ser declarativa e idempotente: o playbook descreve o estado desejado e pode ser executado várias vezes sem duplicar recursos.
- **Resposta correta:** Idempotência
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** Idempotência garante que executar o playbook várias vezes leve ao mesmo estado desejado, sem duplicar objetos. Isso é essencial para automação confiável.

#### 8. Webhook para ITSM

- **Tipo:** `multipla`
- **Pergunta:** Você precisa abrir ticket automaticamente quando uma trigger Disaster dispara. Qual integração faz mais sentido?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** Media type Webhook + Action
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** Webhook/media type permite enviar payload para ITSM, Teams, Jira, GLPI ou outro sistema externo quando uma action é executada. Item dependente e LLD não enviam notificação.

#### 9. Sincronização com CMDB

- **Tipo:** `multipla`
- **Pergunta:** Um script compara a CMDB com o Zabbix. Qual sequência é mais segura para onboarding automático?
- **Conceito/cenário:** Antes de responder, identifique o objetivo operacional do recurso e diferencie coleta, processamento, visualização, alerta, segurança e automação.
- **Resposta correta:** host.get, comparar, depois host.create/host.update
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** Primeiro consultar o estado atual evita duplicidade. Depois criar ausentes e atualizar divergentes preserva idempotência e rastreabilidade.

#### 10. Robô responsável em larga escala

- **Tipo:** `multipla`
- **Pergunta:** O script precisa atualizar 5.000 hosts. Qual cuidado operacional é mais adequado?
- **Conceito/cenário:** Alertas dependem de conditions, operations e media types. Uma boa configuração envia a mensagem certa para o destino certo, no momento certo.
- **Resposta correta:** Executar em lotes com logs, retry e backoff
- **Pista ao errar:** Revise o fluxo de automação do Zabbix e identifique o método/objeto correto.
- **Explicação:** Processar em lotes, registrar logs, tratar erro e aplicar backoff evita sobrecarregar frontend, banco e server. Um loop agressivo sem controle pode gerar instabilidade.

### Missão extra — Segurança: Fase extra: Segurança e Hardening

#### 1. TLS entre componentes

- **Tipo:** `multipla`
- **Pergunta:** Qual tecnologia o Zabbix usa para criptografar comunicação entre server, proxy, agent e utilitários?
- **Conceito/cenário:** Segurança no Zabbix envolve proteger comunicação entre componentes e também o acesso humano ao frontend. TLS pode usar certificados ou PSK entre componentes.
- **Resposta correta:** TLS com certificado ou PSK
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Comentário: o Zabbix suporta criptografia TLS entre componentes usando certificados ou PSK. A questão não pede segmentação de rede nem firewall; esses controles podem complementar segurança, mas não substituem criptografia da comunicação entre Server, Proxy e Agent.

#### 2. TLSConnect e TLSAccept

- **Tipo:** `multiselect`
- **Pergunta:** Quais parâmetros controlam saída e entrada criptografada no agent/proxy?
- **Conceito/cenário:** Segurança em Zabbix combina criptografia, autenticação forte, segregação de permissões, proteção de segredos e auditoria das ações administrativas.
- **Resposta correta:** TLSConnect; TLSAccept
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** TLSConnect define o tipo de criptografia para conexões de saída; TLSAccept define quais conexões de entrada serão aceitas.

#### 3. Risco de PSK

- **Tipo:** `multipla`
- **Pergunta:** Qual cuidado é correto ao usar PSK?
- **Conceito/cenário:** Segurança em Zabbix combina criptografia, autenticação forte, segregação de permissões, proteção de segredos e auditoria das ações administrativas.
- **Resposta correta:** Proteger e restringir acesso ao segredo
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** PSKs e chaves privadas devem ser protegidas, rotacionadas e acessíveis apenas ao serviço necessário. Expor PSK em repositório compromete a comunicação.

#### 4. Métodos de autenticação

- **Tipo:** `multiselect`
- **Pergunta:** Quais métodos fazem parte do desenho de autenticação do Zabbix?
- **Conceito/cenário:** Segurança em Zabbix combina criptografia, autenticação forte, segregação de permissões, proteção de segredos e auditoria das ações administrativas.
- **Resposta correta:** Internal; LDAP; SAML; MFA
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Zabbix oferece autenticação interna e integrações como LDAP, SAML e MFA. SNMP community não autentica usuário da interface web.

#### 5. Menor privilégio

- **Tipo:** `multipla`
- **Pergunta:** Um operador do NOC só deve reconhecer problemas de Linux. O que configurar?
- **Conceito/cenário:** Segurança em Zabbix combina criptografia, autenticação forte, segregação de permissões, proteção de segredos e auditoria das ações administrativas.
- **Resposta correta:** Role + user group + permissões por host group
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Use user group, role e permissões por host group para limitar escopo. Super admin para todos viola menor privilégio.

#### 6. API token seguro

- **Tipo:** `multipla`
- **Pergunta:** Para automação, qual prática é mais segura?
- **Conceito/cenário:** A API do Zabbix usa JSON-RPC sobre HTTP no frontend. Scripts devem autenticar com segurança, consultar estado atual e aplicar mudanças de forma rastreável.
- **Resposta correta:** Token escopado em segredo/cofre
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Token escopado, armazenado em cofre/variável segura e com rotação reduz impacto de vazamento. Senha Admin em texto puro é risco alto.

#### 7. Frontend HTTPS

- **Tipo:** `multipla`
- **Pergunta:** O TLS interno do Zabbix protege automaticamente navegador ↔ frontend?
- **Conceito/cenário:** Segurança em Zabbix combina criptografia, autenticação forte, segregação de permissões, proteção de segredos e auditoria das ações administrativas.
- **Resposta correta:** Não; configure HTTPS no web server/reverso
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** A criptografia entre componentes não substitui HTTPS no web server do frontend. É necessário configurar HTTPS no servidor web/reverso para proteger usuários.

#### 8. Auditoria

- **Tipo:** `multipla`
- **Pergunta:** Para investigar quem alterou uma trigger crítica, qual recurso consultar?
- **Conceito/cenário:** Segurança em Zabbix combina criptografia, autenticação forte, segregação de permissões, proteção de segredos e auditoria das ações administrativas.
- **Resposta correta:** Audit log
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Audit log registra alterações administrativas e ajuda rastreabilidade. Latest data mostra valores; Problems mostra eventos; Maps mostra topologia.

#### 9. PSK e Perfect Forward Secrecy

- **Tipo:** `multipla`
- **Pergunta:** Ao planejar PSK em componentes Zabbix, qual cuidado com biblioteca criptográfica é relevante?
- **Conceito/cenário:** Em segurança, detalhe de versão de biblioteca pode afetar propriedades criptográficas reais.
- **Resposta correta:** Usar biblioteca moderna com suporte adequado a PSK/PFS
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: a documentação alerta que GnuTLS e OpenSSL 1.1.0 ou superior dão suporte a PSK ciphersuites com Perfect Forward Secrecy; versões antigas podem não oferecer essa propriedade. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/encryption
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/encryption

#### 10. Migração TLS com rollback

- **Tipo:** `multipla`
- **Pergunta:** Para migrar agent de comunicação sem criptografia para certificado com menor risco, qual abordagem é mais segura?
- **Conceito/cenário:** Questões de migração segura valorizam rollback e validação antes de bloquear o modo antigo.
- **Resposta correta:** Aceitar ambos temporariamente, testar certificado e depois restringir
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: durante migração, aceitar temporariamente unencrypted e cert permite testar conexão certificada antes de restringir para cert apenas. Isso reduz risco de indisponibilidade. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/encryption
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/encryption

#### 11. JIT provisioning

- **Tipo:** `multipla`
- **Pergunta:** Em autenticação LDAP/SAML, para que serve JIT provisioning?
- **Conceito/cenário:** Identifique o momento da criação da conta: no primeiro login vindo de autenticação externa.
- **Resposta correta:** Criar/provisionar usuário no primeiro login externo
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: JIT provisioning permite criar/provisionar contas no Zabbix no primeiro login via provedor externo, conforme configuração. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 12. Segredos separados por sistema

- **Tipo:** `multipla`
- **Pergunta:** Um cofre guarda API token Zabbix, AWS secret key, Azure client secret e senha de banco. Qual prática é mais segura?
- **Conceito/cenário:** Cenário real: um vazamento parcial não deve permitir acesso total a todas as plataformas.
- **Resposta correta:** Segredos separados, escopados e rotacionáveis por sistema
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: cada sistema possui segredo e escopo próprios; API tokens herdam permissões do usuário Zabbix, AWS usa IAM/access key, Azure usa app secret e ODBC usa credencial de banco. Segredos devem ser separados, escopados e rotacionáveis. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens, https://www.zabbix.com/integrations/aws, https://www.zabbix.com/integrations/azure e https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens,
  - https://www.zabbix.com/integrations/aws,
  - https://www.zabbix.com/integrations/azure

#### 13. Fronteiras de identidade

- **Tipo:** `multiselect`
- **Pergunta:** Em um ambiente com SAML, Zabbix API, AWS, Azure e ODBC, quais separações estão corretas?
- **Conceito/cenário:** Cenário real: uma arquitetura segura evita reutilizar uma única credencial para todas as plataformas.
- **Resposta correta:** SAML para login humano no frontend; API token para automação Zabbix; IAM/access key/assume role para AWS; Service principal para Azure; Credencial/DSN ODBC para banco
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: SAML autentica usuários do frontend; API token autentica chamadas à API Zabbix; AWS by HTTP usa IAM/access key/assume role; Azure by HTTP usa service principal; Database monitor usa ODBC/DSN/credencial do banco. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication, https://www.zabbix.com/documentation/7.0/en/manual/api, https://www.zabbix.com/integrations/aws, https://www.zabbix.com/integrations/azure e https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/api,
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication,
  - https://www.zabbix.com/integrations/aws,
  - https://www.zabbix.com/integrations/azure

### Missão extra — Ansible: Fase extra: Automação com Ansible

#### 1. Collection community.zabbix

- **Tipo:** `multipla`
- **Pergunta:** Qual collection fornece módulos para gerenciar recursos do Zabbix com Ansible?
- **Conceito/cenário:** Automação com Ansible usa collections para fornecer módulos declarativos. Com Zabbix, a collection community.zabbix encapsula chamadas de API em módulos idempotentes.
- **Resposta correta:** community.zabbix
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Comentário: a collection community.zabbix fornece módulos próprios para gerenciar objetos do Zabbix via Ansible. Usar apenas módulos genéricos pode funcionar para arquivos ou comandos, mas perde idempotência e semântica específica dos objetos do Zabbix.

#### 2. Criar host com Ansible

- **Tipo:** `multipla`
- **Pergunta:** Qual módulo da collection é adequado para criar/atualizar hosts?
- **Conceito/cenário:** Automação com Ansible deve ser declarativa e idempotente: o playbook descreve o estado desejado e pode ser executado várias vezes sem duplicar recursos.
- **Resposta correta:** community.zabbix.zabbix_host
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** zabbix_host gerencia hosts no Zabbix. zabbix_item cria itens; zabbix_action gerencia ações; file gerencia arquivos locais.

#### 3. Idempotência

- **Tipo:** `multipla`
- **Pergunta:** Qual comportamento você espera de um playbook idempotente?
- **Conceito/cenário:** Automação com Ansible deve ser declarativa e idempotente: o playbook descreve o estado desejado e pode ser executado várias vezes sem duplicar recursos.
- **Resposta correta:** Mesmo estado final sem duplicidade
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Executar repetidamente deve convergir para o mesmo estado, sem duplicar hosts, itens ou macros. Isso permite automação segura e repetível.

#### 4. Proteção de segredos

- **Tipo:** `multipla`
- **Pergunta:** Onde armazenar senhas/tokens usados pelo playbook?
- **Conceito/cenário:** Automação com Ansible deve ser declarativa e idempotente: o playbook descreve o estado desejado e pode ser executado várias vezes sem duplicar recursos.
- **Resposta correta:** Ansible Vault/cofre
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Ansible Vault ou cofre corporativo evita segredos em texto puro. Variáveis públicas no repositório expõem credenciais.

#### 5. Inventory de automação

- **Tipo:** `multipla`
- **Pergunta:** Qual arquivo/conceito define os hosts-alvo onde o Ansible executa tarefas?
- **Conceito/cenário:** Automação com Ansible deve ser declarativa e idempotente: o playbook descreve o estado desejado e pode ser executado várias vezes sem duplicar recursos.
- **Resposta correta:** Inventory
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Inventory define grupos e hosts-alvo do Ansible. Templates Zabbix são objetos de monitoramento, não lista de execução do Ansible.

#### 6. Instalar agent em escala

- **Tipo:** `multipla`
- **Pergunta:** Para instalar e configurar Agent/Agent2 em vários Linux, o que é mais reutilizável?
- **Conceito/cenário:** Automação com Ansible deve ser declarativa e idempotente: o playbook descreve o estado desejado e pode ser executado várias vezes sem duplicar recursos.
- **Resposta correta:** Role Ansible
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Role separa tasks, handlers, templates e vars, permitindo padronizar instalação e configuração do agente em muitos hosts.

#### 7. Manutenção via playbook

- **Tipo:** `multipla`
- **Pergunta:** Antes de reiniciar 100 servidores, qual módulo/objeto deve ser usado para evitar ruído?
- **Conceito/cenário:** Automação com Ansible deve ser declarativa e idempotente: o playbook descreve o estado desejado e pode ser executado várias vezes sem duplicar recursos.
- **Resposta correta:** zabbix_maintenance
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Criar maintenance window pelo playbook suprime alertas planejados sem desabilitar monitoramento permanentemente.

#### 8. Pipeline seguro

- **Tipo:** `multipla`
- **Pergunta:** Qual prática melhora um pipeline que altera Zabbix via Ansible?
- **Conceito/cenário:** Automação com Ansible deve ser declarativa e idempotente: o playbook descreve o estado desejado e pode ser executado várias vezes sem duplicar recursos.
- **Resposta correta:** check mode/diff, revisão e rollout em lotes
- **Pista ao errar:** Revise o conceito e compare com a documentação oficial recomendada para esta fase.
- **Explicação:** Check mode/diff, revisão, logs e rollout em lotes reduzem risco. Aplicar em produção sem validação aumenta chance de impacto amplo.

#### 9. Módulo para itens

- **Tipo:** `multipla`
- **Pergunta:** Qual módulo da collection community.zabbix é voltado para criar ou remover itens?
- **Conceito/cenário:** Leia o substantivo do objeto que será gerenciado. A collection possui módulos específicos por recurso Zabbix.
- **Resposta correta:** community.zabbix.zabbix_item
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: community.zabbix.zabbix_item é o módulo para itens; zabbix_host gerencia hosts, zabbix_trigger gerencia triggers e zabbix_maintenance cria janelas de manutenção. Referência oficial: https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/index.html
- **Links oficiais citados:**
  - https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/index.html

#### 10. Módulo para templates

- **Tipo:** `multipla`
- **Pergunta:** Qual módulo é adequado para criar, atualizar ou deletar templates do Zabbix?
- **Conceito/cenário:** Associe o recurso Zabbix ao módulo correspondente da collection.
- **Resposta correta:** community.zabbix.zabbix_template
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: community.zabbix.zabbix_template gerencia templates. Isso é mais declarativo e rastreável do que cliques manuais quando o objetivo é padronizar configuração. Referência oficial: https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/index.html
- **Links oficiais citados:**
  - https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/index.html

#### 11. Automatização de tokens

- **Tipo:** `multipla`
- **Pergunta:** Qual módulo da collection indica suporte para criar, atualizar, gerar ou deletar tokens Zabbix?
- **Conceito/cenário:** Em automação segura, tokens são recursos próprios e devem ser tratados como segredos, não como texto solto no playbook.
- **Resposta correta:** community.zabbix.zabbix_token
- **Pista ao errar:** Pista: leia o cenário como uma questão de prova. Identifique primeiro o objetivo operacional e depois elimine opções que pertencem a outro fluxo do Zabbix.
- **Explicação:** Comentário: community.zabbix.zabbix_token aparece na documentação da collection como módulo para Create/Update/Generate/Delete Zabbix token. Referência oficial: https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/index.html
- **Links oficiais citados:**
  - https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/index.html

### Missão extra — AWS: Fase extra: Integração de Monitoramento com AWS

#### 1. AWS by HTTP: abordagem

- **Tipo:** `multipla`
- **Pergunta:** A equipe quer monitorar AWS sem instalar scripts externos no servidor Zabbix. Qual abordagem dos templates oficiais atende melhor ao cenário?
- **Conceito/cenário:** Cenário real: a equipe de segurança restringiu scripts customizados no servidor. A solução deve usar template oficial via HTTP.
- **Resposta correta:** AWS by HTTP
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: o template AWS by HTTP foi projetado para monitoramento via HTTP sem scripts externos e inclui descoberta de recursos como EC2, RDS, ECS, ELB, Lambda, S3 e backup vaults. Referência oficial: https://www.zabbix.com/integrations/aws
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/aws

#### 2. AWS: permissões IAM

- **Tipo:** `multipla`
- **Pergunta:** A coleta AWS falha com AccessDenied ao descobrir EC2 e RDS. Qual é a causa mais provável?
- **Conceito/cenário:** Cenário real: o template está vinculado e as macros existem, mas a API AWS nega as chamadas. Pense em autorização no provedor cloud.
- **Resposta correta:** Policy IAM sem permissões necessárias
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: antes de usar o template, a documentação orienta criar uma policy IAM com permissões necessárias, como ações de CloudWatch, EC2, RDS, ECS, S3, ELB, Lambda e Backup. Referência oficial: https://www.zabbix.com/integrations/aws
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/aws

#### 3. AWS: macros de credenciais

- **Tipo:** `multiselect`
- **Pergunta:** Usando Access Key Authorization, quais macros são necessárias para as credenciais?
- **Conceito/cenário:** Cenário real: o host de integração foi criado, mas as macros de autenticação estão vazias. Identifique as macros de credencial, não filtros de descoberta.
- **Resposta correta:** {$AWS.ACCESS.KEY.ID}; {$AWS.SECRET.ACCESS.KEY}
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a integração AWS by HTTP define macros como {$AWS.ACCESS.KEY.ID} e {$AWS.SECRET.ACCESS.KEY} para access key authorization. Referência oficial: https://www.zabbix.com/integrations/aws
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/aws

#### 4. AWS: descoberta de RDS

- **Tipo:** `multipla`
- **Pergunta:** O time quer descobrir automaticamente bancos RDS para monitoramento padronizado. Qual capacidade do template AWS by HTTP é relevante?
- **Conceito/cenário:** Cenário real: a empresa cria RDS sob demanda. A solução deve evitar cadastro manual de cada instância.
- **Resposta correta:** Descoberta de RDS instances
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a integração AWS by HTTP informa suporte à descoberta de EC2 e RDS, além de outros serviços. Para bancos gerenciados na AWS, RDS discovery é o recurso alinhado ao cenário. Referência oficial: https://www.zabbix.com/integrations/aws
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/aws

#### 5. AWS: custos

- **Tipo:** `multipla`
- **Pergunta:** A diretoria quer visibilidade de custo cloud no Zabbix. Qual solução oficial citada atende esse objetivo?
- **Conceito/cenário:** Cenário real: além de disponibilidade, o NOC precisa acompanhar consumo financeiro da nuvem.
- **Resposta correta:** AWS Cost Explorer by HTTP
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a página de integração AWS lista AWS Cost Explorer by HTTP como solução disponível para monitoramento relacionado a custos. Referência oficial: https://www.zabbix.com/integrations/aws
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/aws

#### 6. AWS: CloudWatch

- **Tipo:** `multipla`
- **Pergunta:** Qual permissão aparece como base para coletar métricas agregadas de serviços AWS no template?
- **Conceito/cenário:** Cenário real: a integração autentica, mas não traz métricas. Pense na API que fornece séries temporais da AWS.
- **Resposta correta:** cloudwatch:GetMetricData
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a policy de exemplo da integração inclui cloudwatch:GetMetricData e cloudwatch:DescribeAlarms, pois métricas e alarmes AWS são obtidos por APIs CloudWatch. Referência oficial: https://www.zabbix.com/integrations/aws
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/aws

#### 7. AWS: Zabbix token vs IAM

- **Tipo:** `multipla`
- **Pergunta:** A equipe criou um API token no Zabbix, mas a coleta AWS continua com AccessDenied. Por quê?
- **Conceito/cenário:** Cenário real: autenticar no Zabbix não concede permissão automaticamente dentro da AWS.
- **Resposta correta:** Token Zabbix não substitui permissões IAM AWS
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: API token autentica chamadas à API do Zabbix; a coleta AWS by HTTP exige autorização AWS por IAM/access key/assume role e permissões como CloudWatch/EC2/RDS. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens e https://www.zabbix.com/integrations/aws
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
  - https://www.zabbix.com/integrations/aws

#### 8. AWS Assume Role e trust

- **Tipo:** `multipla`
- **Pergunta:** A integração AWS usa assume role, mas falha mesmo com permissões de leitura. Qual elemento de confiança também precisa estar correto?
- **Conceito/cenário:** Cenário real: permissões de leitura existem, mas a entidade que chama não está autorizada a assumir a role.
- **Resposta correta:** Trust relationship permitindo sts:AssumeRole
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: a documentação AWS by HTTP mostra assume role authorization e trust relationships para permitir sts:AssumeRole ao principal correto. Referência oficial: https://www.zabbix.com/integrations/aws
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/aws

### Missão extra — Bancos de Dados: Fase extra: Monitoramento de Banco de Dados

#### 1. Database monitor: tipo de item

- **Tipo:** `multipla`
- **Pergunta:** Você precisa consultar uma fila de processamento diretamente em um banco via SQL. Qual tipo de item do Zabbix é apropriado?
- **Conceito/cenário:** Cenário real: a aplicação não expõe métrica HTTP, mas a fila está em tabela SQL. A coleta deve consultar o SGBD via driver.
- **Resposta correta:** Database monitor
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: o item type Database monitor é usado para ODBC monitoring/ODBC checks, permitindo consultar bancos suportados por ODBC. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks

#### 2. ODBC: camada de acesso

- **Tipo:** `multipla`
- **Pergunta:** Segundo a documentação, o Zabbix conecta diretamente no banco ou usa uma camada intermediária?
- **Conceito/cenário:** Cenário real: a query está correta, mas o item não coleta. Antes de culpar o SQL, verifique DSN, driver e unixODBC.
- **Resposta correta:** Usa interface ODBC e drivers configurados
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: o Zabbix não conecta diretamente no banco nesse tipo de item; ele usa a interface ODBC e drivers configurados no sistema. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks

#### 3. unixODBC

- **Tipo:** `multipla`
- **Pergunta:** Em Linux, qual componente é comumente necessário para Database monitor funcionar com ODBC?
- **Conceito/cenário:** Cenário real: o Zabbix foi compilado sem suporte ODBC e a equipe quer checks SQL. Identifique o componente base.
- **Resposta correta:** unixODBC e driver do banco
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a documentação informa suporte a unixODBC e orienta instalar unixODBC/unixODBC-devel ou unixodbc-dev conforme a distribuição. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks

#### 4. Compilação com ODBC

- **Tipo:** `multipla`
- **Pergunta:** Qual opção de configuração habilita suporte ODBC ao compilar Zabbix?
- **Conceito/cenário:** Cenário real: o binário do Zabbix não reconhece checks ODBC. Pense na opção de build indicada pela documentação.
- **Resposta correta:** --with-unixodbc
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a documentação indica a opção --with-unixodbc[=ARG] para usar driver ODBC contra unixODBC. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks

#### 5. ODBC: arquivos de configuração

- **Tipo:** `multiselect`
- **Pergunta:** Quais arquivos são usados para configurar drivers e data sources no unixODBC?
- **Conceito/cenário:** Cenário real: o DSN funciona em um servidor, mas não no Zabbix. Compare driver e data source nos arquivos corretos.
- **Resposta correta:** odbcinst.ini; odbc.ini
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: unixODBC usa odbcinst.ini para drivers instalados e odbc.ini para data sources/DSN. A documentação sugere verificar caminhos com odbcinst -j. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks

#### 6. Banco: menor privilégio

- **Tipo:** `multipla`
- **Pergunta:** Qual boa prática é mais adequada para o usuário de banco usado por checks ODBC?
- **Conceito/cenário:** Cenário real: a equipe de DBA pediu justificativa de segurança para liberar monitoramento SQL.
- **Resposta correta:** Usuário dedicado com leitura mínima necessária
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: embora a página de ODBC foque a configuração técnica, em cenários reais o usuário de monitoramento deve ter privilégio mínimo, normalmente leitura somente das views/tabelas necessárias. Referência oficial do tipo de item: https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks

#### 7. Banco: credencial ODBC vs usuário Zabbix

- **Tipo:** `multipla`
- **Pergunta:** Um usuário Admin do Zabbix criou um item Database monitor, mas a query falha por login denied no banco. Qual camada precisa ajuste?
- **Conceito/cenário:** Cenário real: conseguir criar o item no Zabbix não implica que o banco aceite a conexão usada pela query.
- **Resposta correta:** Credenciais/permissões do banco no DSN/query
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: permissões do usuário Zabbix controlam configuração na interface/API; a execução de query Database monitor depende de DSN/driver/credencial do banco via ODBC. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions e https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions

#### 8. LDAP user não é DB user

- **Tipo:** `multipla`
- **Pergunta:** O operador LDAP consegue entrar no Zabbix, mas uma query ODBC falha por senha do banco. Qual afirmação é correta?
- **Conceito/cenário:** Cenário real: o status do item não depende da senha interativa do operador, mas da configuração de conexão usada pelo check.
- **Resposta correta:** Login Zabbix e login do banco são camadas separadas
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: autenticação LDAP é do frontend Zabbix; Database monitor usa ODBC e credencial/DSN do banco. São camadas distintas. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication e https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

### Missão extra — Azure: Fase extra: Integração de Monitoramento com Azure

#### 1. Azure by HTTP: abordagem

- **Tipo:** `multipla`
- **Pergunta:** A equipe quer monitorar Azure sem scripts externos. Qual integração oficial atende esse modelo?
- **Conceito/cenário:** Cenário real: política interna proíbe scripts locais customizados, mas permite templates oficiais por HTTP.
- **Resposta correta:** Microsoft Azure by HTTP
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: Azure by HTTP foi projetado para monitorar Microsoft Azure por HTTP, usa script item e não requer scripts externos. Referência oficial: https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/azure

#### 2. Azure: service principal

- **Tipo:** `multipla`
- **Pergunta:** O setup oficial orienta criar qual identidade para permitir que o Zabbix consulte a subscription Azure?
- **Conceito/cenário:** Cenário real: a integração precisa chamar APIs Azure sem usar conta pessoal de operador.
- **Resposta correta:** Service principal
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a integração Azure by HTTP orienta criar um Azure service principal via Azure CLI para a subscription, normalmente com role reader no escopo adequado. Referência oficial: https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/azure

#### 3. Azure: macros obrigatórias

- **Tipo:** `multiselect`
- **Pergunta:** Quais macros são usadas para autenticação/escopo principal no Azure by HTTP?
- **Conceito/cenário:** Cenário real: a integração está vinculada ao host, mas a autenticação falha. Verifique macros de app, segredo, tenant e subscription.
- **Resposta correta:** {$AZURE.APP.ID}; {$AZURE.PASSWORD}; {$AZURE.TENANT.ID}; {$AZURE.SUBSCRIPTION.ID}
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a página da integração lista macros como {$AZURE.APP.ID}, {$AZURE.PASSWORD}, {$AZURE.TENANT.ID} e {$AZURE.SUBSCRIPTION.ID}. Referência oficial: https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/azure

#### 4. Azure: recursos suportados

- **Tipo:** `multipla`
- **Pergunta:** A empresa quer monitorar automaticamente VMs e bancos Azure gerenciados. Qual afirmação condiz com a integração Azure by HTTP?
- **Conceito/cenário:** Cenário real: a plataforma Azure cresce por autoscaling e serviços gerenciados. A solução deve incluir descoberta automática.
- **Resposta correta:** Suporta descoberta de VMs e vários serviços de banco gerenciados
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a integração Azure by HTTP informa suporte à descoberta de VMs, VM scale sets, Cosmos DB for MongoDB, storage accounts, Microsoft SQL, MySQL e PostgreSQL, entre outros. Referência oficial: https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/azure

#### 5. Azure: permissão mínima

- **Tipo:** `multipla`
- **Pergunta:** No setup citado, qual papel é usado no exemplo de criação do service principal?
- **Conceito/cenário:** Cenário real: segurança exige que a integração leia recursos sem permissão de alteração.
- **Resposta correta:** Reader
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: o exemplo de setup usa Azure CLI com --role reader no escopo da subscription, refletindo menor privilégio para leitura de métricas/recursos. Referência oficial: https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/azure

#### 6. Azure: custos

- **Tipo:** `multipla`
- **Pergunta:** Qual template disponível é indicado quando o objetivo é acompanhar custos Azure?
- **Conceito/cenário:** Cenário real: FinOps quer que o NOC enxergue custo junto com disponibilidade.
- **Resposta correta:** Azure Cost Management by HTTP
- **Pista ao errar:** Pista: leia o cenário, identifique o tipo de monitoramento e elimine opções que pertencem a outro domínio.
- **Explicação:** Comentário: a integração Azure lista Azure Cost Management by HTTP entre os templates incluídos. Referência oficial: https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/azure

#### 7. Azure: usuário Zabbix vs service principal

- **Tipo:** `multipla`
- **Pergunta:** Um usuário consegue logar no Zabbix via LDAP, mas o template Azure by HTTP falha na autenticação. Qual credencial deve ser revisada?
- **Conceito/cenário:** Cenário real: o operador estar autenticado no Zabbix não significa que o host/template tenha credenciais válidas no Azure.
- **Resposta correta:** Macros do service principal Azure
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: login do usuário no Zabbix é separado da autenticação Azure; Azure by HTTP usa service principal e macros como AZURE.APP.ID, AZURE.PASSWORD, AZURE.TENANT.ID e AZURE.SUBSCRIPTION.ID. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication e https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
  - https://www.zabbix.com/integrations/azure

#### 8. Azure service principal e rotação

- **Tipo:** `multipla`
- **Pergunta:** A senha do service principal Azure foi rotacionada no Entra ID. O que precisa ser atualizado no Zabbix?
- **Conceito/cenário:** Cenário real: a identidade Azure continua a mesma, mas o segredo mudou.
- **Resposta correta:** Macro {$AZURE.PASSWORD} / segredo do client secret
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: Azure by HTTP usa macros do service principal, incluindo {$AZURE.PASSWORD} como client secret. Após rotação, a macro/segredo correspondente precisa ser atualizado. Referência oficial: https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/integrations/azure

### Missão extra — Autenticação: Fase extra: Autenticação, SSO e Identidades

#### 1. Métodos de autenticação suportados

- **Tipo:** `multiselect`
- **Pergunta:** Uma empresa quer comparar alternativas de login para o frontend Zabbix. Quais métodos fazem parte das opções de autenticação citadas oficialmente?
- **Conceito/cenário:** Cenário real: o time de segurança está desenhando login único para operadores, mas precisa manter contas locais de emergência.
- **Resposta correta:** Internal; HTTP; LDAP; SAML; MFA
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: a documentação de Authentication cita autenticação interna, HTTP, LDAP, SAML e MFA. Essa questão separa login de usuários no frontend de credenciais de banco, SNMP ou IAM cloud. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 2. LDAP global com exceção interna

- **Tipo:** `multipla`
- **Pergunta:** A empresa definiu LDAP como autenticação padrão, mas quer que um grupo de break-glass continue usando autenticação interna. Onde essa exceção é ajustada?
- **Conceito/cenário:** Cenário real: SSO/LDAP pode ficar indisponível. Contas de emergência precisam autenticar localmente sem alterar o modelo global.
- **Resposta correta:** Frontend access do user group
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: mesmo com LDAP global, a documentação informa que o método pode ser refinado no nível de user group, usando frontend access como Internal para grupos específicos. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 3. JIT provisioning e deprovisioning

- **Tipo:** `multipla`
- **Pergunta:** Após SAML JIT criar usuários automaticamente, usuários desligados precisam ser movidos para grupo sem acesso. Qual configuração é relevante?
- **Conceito/cenário:** Cenário real: RH removeu uma pessoa no provedor de identidade, mas auditoria exige que a conta Zabbix seja desativada de modo rastreável.
- **Resposta correta:** Deprovisioned users group
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: a tela Authentication inclui configuração de Deprovisioned users group para JIT provisioning de LDAP/SAML. Esse grupo deve ser desabilitado para usuários que não devem mais ser provisionados. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 4. API token herda permissões

- **Tipo:** `multipla`
- **Pergunta:** Um robô com API token consegue ler hosts de Produção, mas não de Financeiro. Qual é a explicação mais provável?
- **Conceito/cenário:** Cenário real: a automação usa token correto, mas recebe permissão negada em parte do inventário. O problema está em autorização, não no endpoint.
- **Resposta correta:** O token herda role e permissões do usuário associado
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: API tokens são atribuídos a um único usuário e as requisições autenticadas pelo token são autorizadas conforme role e permissões desse usuário. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens

#### 5. Valor do API token

- **Tipo:** `multipla`
- **Pergunta:** Ao criar um API token, quando o valor secreto deve ser copiado e salvo com segurança?
- **Conceito/cenário:** Cenário real: um pipeline foi configurado, mas ninguém salvou o token após criá-lo. O time quer recuperar o valor pela UI.
- **Resposta correta:** Imediatamente após criar, antes de fechar a tela
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: a documentação informa que o valor Auth token só é exibido logo após a criação e não pode ser visualizado novamente. Se perdido, é necessário regenerar o token. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens

#### 6. Token exposto em repositório

- **Tipo:** `multipla`
- **Pergunta:** Um token de API foi publicado acidentalmente em um repositório. Qual ação é mais correta?
- **Conceito/cenário:** Cenário real: o scanner de segurança encontrou um token Zabbix em um commit. A ação deve invalidar o segredo vazado.
- **Resposta correta:** Desabilitar/regenerar o token e atualizar o segredo seguro
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: a documentação permite desabilitar tokens e regenerar o valor quando perdido ou exposto; regenerar invalida o token anterior. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens

#### 7. Roles e métodos de API

- **Tipo:** `multipla`
- **Pergunta:** Um usuário Admin acessa a interface, mas não deve executar determinados métodos de API. Qual recurso permite ajustar esse tipo de acesso?
- **Conceito/cenário:** Cenário real: uma equipe deve criar dashboards, mas não deve chamar métodos de automação sensíveis via API.
- **Resposta correta:** User roles
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: user roles podem ajustar acesso a menu sections, services, modules, API methods e ações do frontend, dentro dos limites do user type. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions

#### 8. Acesso a hosts por grupos

- **Tipo:** `multipla`
- **Pergunta:** Um operador precisa ver apenas hosts do grupo Linux/Produção. Como o acesso a hosts é concedido no Zabbix?
- **Conceito/cenário:** Cenário real: o NOC tem times por domínio. O acesso deve ser por grupo e host group, não diretamente host por host.
- **Resposta correta:** User group com permissão no host group
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: acesso a hosts/templates é concedido a user groups no nível de host/template groups; um usuário recebe acesso por pertencer a um user group autorizado. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions

#### 9. Zabbix + SAML + ITSM

- **Tipo:** `multipla`
- **Pergunta:** Zabbix usa SAML para login humano e webhook para abrir chamado no ITSM. Qual separação de responsabilidades está correta?
- **Conceito/cenário:** Cenário real com múltiplos sistemas: IdP autentica operadores; Zabbix autoriza ações; ITSM recebe incidentes por integração. Não misture login com notificação.
- **Resposta correta:** SAML autentica usuários; action/webhook integra incidentes com ITSM
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: autenticação SAML trata login de usuários; integrações de alerta/webhook tratam envio de eventos a sistemas externos. A documentação separa autenticação do frontend e permissões de API/ações. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication e https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 10. Zabbix API + AWS + Azure

- **Tipo:** `multipla`
- **Pergunta:** Um portal interno usa Zabbix API para criar hosts, AWS IAM para coletar CloudWatch e Azure service principal para coletar Azure. Qual afirmação é correta?
- **Conceito/cenário:** Cenário real com múltiplos sistemas: cada plataforma tem seu modelo de identidade. Um token Zabbix não substitui IAM AWS nem service principal Azure.
- **Resposta correta:** Cada sistema exige identidade/autorização própria
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: Zabbix API autentica por API token ou user.login; AWS by HTTP usa IAM/access key/assume role; Azure by HTTP usa service principal e macros de app/tenant/subscription. São identidades e autorizações diferentes por sistema. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/api, https://www.zabbix.com/integrations/aws e https://www.zabbix.com/integrations/azure
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/api,
  - https://www.zabbix.com/integrations/aws
  - https://www.zabbix.com/integrations/azure

#### 11. Zabbix + Banco + LDAP

- **Tipo:** `multipla`
- **Pergunta:** Zabbix autentica operadores via LDAP, mas um item Database monitor consulta uma fila no PostgreSQL. Qual credencial deve ser usada para a query ODBC?
- **Conceito/cenário:** Cenário real com múltiplos sistemas: não use credenciais pessoais de login Zabbix para consulta SQL operacional.
- **Resposta correta:** Usuário de serviço do banco com leitura mínima
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: LDAP/SAML autentica usuários do frontend; Database monitor usa ODBC e driver/DSN para consultar o banco. O ideal é usar usuário dedicado de banco com mínimo privilégio para a query. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication e https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 12. MFA para contas privilegiadas

- **Tipo:** `multipla`
- **Pergunta:** A auditoria exige reforçar acesso de Super admins ao frontend Zabbix. Qual método citado oficialmente atende esse objetivo?
- **Conceito/cenário:** Cenário real: contas com amplo acesso precisam de controle extra além de senha.
- **Resposta correta:** MFA authentication
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: a documentação lista MFA entre os métodos de autenticação disponíveis em Zabbix. Para contas privilegiadas, MFA reduz risco de acesso indevido caso a senha seja comprometida. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 13. Política de senha interna

- **Tipo:** `multiselect`
- **Pergunta:** Se usuários internos ainda existem, quais configurações de senha podem ser reforçadas na tela Authentication?
- **Conceito/cenário:** Cenário real: mesmo com SSO, contas internas de emergência precisam política forte.
- **Resposta correta:** Minimum password length; Password must contain caracteres exigidos; Avoid easy-to-guess passwords
- **Pista ao errar:** Pista: identifique quem autentica, quem autoriza e qual sistema é a fonte de identidade. Não confunda autenticação de usuário, token de API, IAM cloud e credencial de banco.
- **Explicação:** Comentário: a tela Authentication permite configurar comprimento mínimo, exigência de maiúsculas/minúsculas, dígito, caractere especial e evitar senhas fáceis de adivinhar. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 14. User type: Super admin

- **Tipo:** `multipla`
- **Pergunta:** Uma equipe tentou negar acesso de um Super admin a um host group específico. Qual é o comportamento esperado?
- **Conceito/cenário:** Cenário real: uma empresa quer aplicar segregação fina até para contas máximas. Em prova, reconheça que Super admin é exceção de privilégio amplo.
- **Resposta correta:** Não é possível revogar permissões por grupo de um Super admin
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: a documentação de permissões informa que Super admin tem acesso a todas as seções e read-write em todos os host/template groups; permissões não podem ser revogadas negando grupos específicos. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions

#### 15. Admin sem acesso por padrão

- **Tipo:** `multipla`
- **Pergunta:** Um usuário Admin foi criado, mas não enxerga hosts. Qual é a causa mais provável?
- **Conceito/cenário:** Cenário real: o usuário consegue acessar menus administrativos, mas não vê dados de monitoramento. Separe menu access de acesso a host groups.
- **Resposta correta:** Faltam permissões no host group via user group
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: usuários do tipo Admin não têm acesso a host groups por padrão; permissões a host/template groups precisam ser concedidas explicitamente via user groups. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions

#### 16. Menu access vs dados

- **Tipo:** `multipla`
- **Pergunta:** Restringir uma seção de menu em uma role garante, sozinho, que o usuário não acesse os dados subjacentes por outros caminhos?
- **Conceito/cenário:** Cenário real: auditoria exige que operadores não vejam certos hosts. Bloquear apenas uma tela não substitui permissão de dados.
- **Resposta correta:** Não; menu access sozinho não substitui permissões de dados
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: a documentação alerta que restringir UI/menu impede abrir a página, mas não remove necessariamente acesso a dados subjacentes em outras partes da interface. Controle de dados deve considerar permissões de host/template groups e roles. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions

#### 17. Token desabilitado

- **Tipo:** `multipla`
- **Pergunta:** Um robô passa a receber falha de autenticação após auditoria desabilitar o token na lista de API tokens. Qual é a explicação?
- **Conceito/cenário:** Cenário real: o segredo continua no cofre e o endpoint está correto, mas o status do token foi alterado pela equipe de segurança.
- **Resposta correta:** O status Enabled/Disabled do token afeta seu uso
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: a tela API tokens permite habilitar/desabilitar tokens; tokens desabilitados não devem autenticar chamadas. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens

#### 18. Token e usuário associado

- **Tipo:** `multipla`
- **Pergunta:** Depois de criar um API token para um usuário, o time quer mudar o usuário associado ao token existente. O que a documentação indica?
- **Conceito/cenário:** Cenário real: o robô mudou de time e o token precisa seguir novo modelo de permissão. Trocar ownership do token não é o caminho.
- **Resposta correta:** Não é possível mudar o usuário associado ao token existente
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: a documentação de API tokens informa que não é possível alterar o usuário ao qual o token está atribuído; deve-se criar outro token para outro usuário. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens

#### 19. Expiração de token

- **Tipo:** `multipla`
- **Pergunta:** Um token usado por pipeline parou de funcionar exatamente na data planejada. Qual campo da configuração provavelmente explica isso?
- **Conceito/cenário:** Cenário real: a automação falhou após rotação programada. Verifique ciclo de vida do token antes de culpar rede ou API.
- **Resposta correta:** Expiry date do API token
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: API tokens podem ter data/hora de expiração configurada em Set expiration date and time / Expiry date. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens

#### 20. Role não excede user type

- **Tipo:** `multipla`
- **Pergunta:** Uma role customizada foi criada para usuário do tipo User com tentativa de dar acesso equivalente a Super admin. Isso funciona?
- **Conceito/cenário:** Cenário real: o time quer resolver tudo com role customizada, mas esquece que user type define o teto de permissão.
- **Resposta correta:** Não; role não pode exceder o user type
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: user roles permitem revogar/ajustar permissões dentro dos limites do user type; não adicionam permissões que excedem o tipo base do usuário. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions

#### 21. API: autenticação e autorização

- **Tipo:** `multipla`
- **Pergunta:** Uma aplicação externa chama `host.get` no Zabbix. Onde a autenticação da API deve estar representada de forma adequada?
- **Conceito/cenário:** Cenário real: o JSON-RPC está bem formado, mas a chamada falha por autenticação. Diferencie estrutura da requisição e credencial/authorization.
- **Resposta correta:** API token ou token de login associado a usuário autorizado
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: a documentação da API informa que o acesso exige API token existente ou token obtido via user.login; a autorização depende do user type, role e user groups. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/api
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/api

#### 22. HTTP authentication vs API token

- **Tipo:** `multipla`
- **Pergunta:** A organização usa HTTP authentication no frontend, mas um script precisa chamar a API. Qual afirmação está correta?
- **Conceito/cenário:** Cenário real: login via proxy/reverso funciona para humanos, mas automação JSON-RPC precisa credencial apropriada para API.
- **Resposta correta:** A API ainda precisa de API token ou token de login
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: HTTP authentication é método de autenticação do frontend. Chamadas à API continuam precisando de autenticação de API, como API token ou token obtido por user.login. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication e https://www.zabbix.com/documentation/7.0/en/manual/api
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/api
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 23. SAML JIT + RBAC

- **Tipo:** `multipla`
- **Pergunta:** Usuários são criados via SAML JIT, mas precisam receber acesso apenas ao host group da sua área. Qual camada deve ser planejada além do login?
- **Conceito/cenário:** Cenário real: autenticar não é autorizar. O IdP prova quem a pessoa é; o Zabbix ainda precisa mapear acesso operacional.
- **Resposta correta:** User groups, roles e permissões por host/template group
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: JIT pode criar/provisionar usuários via SAML/LDAP, mas acesso a hosts/templates depende de user groups e permissões sobre host/template groups. Referências oficiais: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication e https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 24. Break-glass e MFA

- **Tipo:** `multipla`
- **Pergunta:** Contas break-glass internas devem continuar disponíveis se SSO falhar, mas com alto controle. Qual desenho é mais coerente?
- **Conceito/cenário:** Cenário real: falha do IdP não pode impedir totalmente o acesso emergencial, mas contas locais não devem ser fracas.
- **Resposta correta:** Grupo interno restrito com senha forte/MFA e auditoria
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: a autenticação pode ser afinada por user group, e MFA/política de senha podem reforçar contas internas. Esse desenho preserva acesso emergencial sem depender só do provedor externo. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication

#### 25. MSP multi-cliente

- **Tipo:** `multipla`
- **Pergunta:** Uma empresa MSP monitora clientes A, B e C no mesmo Zabbix. Como evitar que operadores do cliente A vejam hosts do cliente B?
- **Conceito/cenário:** Cenário real com múltiplos sistemas/clientes: isolamento lógico precisa estar no modelo de grupos e permissões, não apenas em dashboards.
- **Resposta correta:** Host groups por cliente + user groups com permissões específicas
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: acesso a hosts é concedido por user groups no nível de host groups. Para multi-tenant, separe host groups por cliente e associe user groups/roles adequados. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/config/users_and_usergroups/permissions

#### 26. Offboarding de automação

- **Tipo:** `multipla`
- **Pergunta:** Um funcionário dono de tokens saiu da empresa. Qual ação reduz risco em automações associadas?
- **Conceito/cenário:** Cenário real: tokens pessoais em pipelines criam risco no desligamento de pessoas.
- **Resposta correta:** Migrar para conta de serviço escopada e revogar/regenerar tokens antigos
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: API tokens são atribuídos a usuários e herdam suas permissões. Em automação, prefira contas de serviço com escopo controlado, expiração/rotação e remoção de tokens pessoais. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens

#### 27. Auditoria de token

- **Tipo:** `multipla`
- **Pergunta:** A auditoria pergunta quem criou e a qual usuário um token pertence. A tela API tokens permite filtrar/visualizar quais metadados?
- **Conceito/cenário:** Cenário real: investigação de automações exige rastrear ownership e ciclo de vida dos tokens.
- **Resposta correta:** Nome, usuário atribuído, expiração, criador e status
- **Pista ao errar:** Pista: identifique a fronteira entre autenticação, autorização e integração. Em cenários multi-sistema, cada sistema costuma ter identidade e escopo próprios.
- **Explicação:** Comentário: a documentação cita filtros por nome, usuários aos quais tokens estão atribuídos, data de expiração, usuários que criaram tokens e status enabled/disabled. Referência oficial: https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens
- **Links oficiais citados:**
  - https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/api_tokens

## Checklist de validação

- [x] Projeto Django com `manage.py`.
- [x] Banco SQLite populado com fases, missões e desafios.
- [x] Eixo principal com ZCU, ZCS, ZCP e ZCE.
- [x] Missões extras no menu lateral.
- [x] Explicações pós-resposta.
- [x] Links oficiais clicáveis no feedback.
- [x] Dashboard com progresso geral de preparação.
- [x] Gabarito completo incluído neste README.

## Roadmap sugerido

- Criar modo simulado cronometrado por certificação.
- Criar banco de questões embaralhado por tópico.
- Criar pontuação por domínio de conhecimento.
- Criar relatório final por gaps de estudo.
- Criar exportação do desempenho em CSV/JSON.
- Criar modo administrador para cadastrar novos desafios pela interface.

## 📄 Licença

Este projeto pode ser distribuído sob a licença **MIT**.

Sugestão: adicione um arquivo `LICENSE` na raiz do projeto com o texto da licença MIT.

---

## 👨‍💻 Autor

Desenvolvido por **Leonardo Azevedo** como material de apoio para preparação para certificações zabbix em formato interativo.

---

## ⭐ Apoie o projeto

Se este projeto ajudou em estudos, meetups ou treinamentos internos, considere deixar uma estrela no repositório.

```text
⭐ Star no GitHub ajuda outras pessoas a encontrarem o projeto.
```
