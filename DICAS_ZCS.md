# Dicas Específicas para ZCS — Zabbix Certified Specialist

A certificação ZCS exige domínio prático de configuração. O foco não é apenas saber o nome dos recursos, mas saber quando usar cada recurso em um cenário real.

## Foco principal do ZCS

- Arquitetura básica e fluxo de dados.
- Instalação e configuração inicial.
- Host groups, hosts, interfaces e templates.
- Itens, item types, keys e tipos de informação.
- Zabbix agent e agent 2.
- Active checks e passive checks.
- SNMP, HTTP agent, simple checks e Database monitor.
- History, trends e retenção.
- Preprocessing e tratamento de erro.
- Triggers, events, problems e actions.
- Notifications, media types e escalations.
- Maintenance windows.
- User roles e permissões básicas.

## Dicas de prova para ZCS

### 1. Leia o cenário antes da alternativa

Muitas questões descrevem uma necessidade operacional. Identifique primeiro se o problema é:

- coleta;
- armazenamento;
- detecção;
- notificação;
- permissão;
- visualização;
- manutenção.

### 2. Para item, pense em seis campos

```text
Tipo de item -> Interface -> Key/OID/URL -> Tipo de informação -> Intervalo -> Retenção
```

Se qualquer um desses pontos estiver errado, a coleta pode falhar ou armazenar dado incorreto.

### 3. Para trigger, pense em cinco partes

```text
Função -> item /host/key -> período ou #N -> operador -> limite
```

Exemplo mental:

```text
last(/Host/system.cpu.util)>90
```

### 4. Não confunda trigger, event, problem e action

- **Trigger:** regra lógica.
- **Event:** ocorrência gerada pela mudança de estado.
- **Problem:** evento de problema visível operacionalmente.
- **Action:** regra de automação/notificação baseada em condições.

### 5. Saiba quando usar `nodata()`

Use `nodata()` quando o problema for ausência de coleta, não valor alto ou baixo.

### 6. Entenda active vs passive checks

- **Passive:** server/proxy solicita dado ao agent.
- **Active:** agent solicita lista de checks e envia dados ao server/proxy.

### 7. SNMP não usa key de agent

SNMP usa OID. Não confunda `system.cpu.util` com OID SNMP.

### 8. Preprocessing é pipeline

As etapas rodam na ordem configurada. Uma etapa pode preparar o valor para a próxima.

### 9. Dependent item reduz coleta duplicada

Use dependent items quando uma chamada retorna vários dados e você quer derivar múltiplos itens.

### 10. Maintenance não é acknowledge

- **Maintenance:** janela planejada.
- **Acknowledge:** reconhecimento de evento já existente.

## Mini-simulado ZCS recomendado

Faça este bloco no projeto:

1. ZCS Core completo.
2. Data Collection.
3. Alerts.
4. Users.
5. Administration.
6. Automação API, somente questões básicas de API.

Critério recomendado:

```text
50 questões em 60 minutos
Meta mínima: 80%
Meta ideal: 90%+
```

## Checklist ZCS antes do exame

- [ ] Sei criar e explicar um item.
- [ ] Sei escolher o item type correto.
- [ ] Sei configurar uma trigger simples.
- [ ] Sei explicar `nodata()`, `last()`, `avg()` e `min()`.
- [ ] Sei diferenciar active e passive checks.
- [ ] Sei diferenciar history e trends.
- [ ] Sei configurar uma action conceitualmente.
- [ ] Sei explicar maintenance.
- [ ] Sei explicar preprocessing.
- [ ] Sei explicar dependent item.
- [ ] Sei diferenciar host, host group e template.
- [ ] Sei interpretar Problems e Latest data.
