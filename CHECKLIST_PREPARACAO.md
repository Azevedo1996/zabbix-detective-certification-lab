# Checklist de Preparação para Certificações — Zabbix Detective

Use este checklist antes de agendar ou realizar qualquer exame. O objetivo é confirmar que você domina conceitos, prática e leitura de cenários.

## Checklist geral

- [ ] Li o README completo do projeto.
- [ ] Segui o GUIA_ESTUDO.md ou adaptei um cronograma próprio.
- [ ] Fiz todos os desafios da certificação alvo sem consultar gabarito.
- [ ] Refiz todos os erros pelo menos uma vez.
- [ ] Abri os links oficiais das questões erradas.
- [ ] Fiz pelo menos um simulado cronometrado.
- [ ] Tenho resumo próprio dos tópicos mais difíceis.
- [ ] Consigo explicar as respostas sem decorar frases.
- [ ] Consigo diferenciar coleta, detecção, notificação, autenticação, autorização e integração.

## Checklist ZCU

- [ ] Sei o papel de Server, Proxy, Database, Frontend e Agent.
- [ ] Sei as portas padrão Server/Agent.
- [ ] Sei navegar por Problems, Latest data, Dashboards e Maps.
- [ ] Sei interpretar severidade, tags e maintenance.
- [ ] Sei diferenciar host, host group, template e item.
- [ ] Fiz simulado de 20 questões em até 30 minutos.

## Checklist ZCS

- [ ] Sei configurar item type, key, interface e tipo de informação.
- [ ] Sei diferenciar Zabbix agent, SNMP agent, HTTP agent, dependent item e Database monitor.
- [ ] Sei diferenciar active e passive checks.
- [ ] Sei explicar history e trends.
- [ ] Sei criar uma trigger simples e explicar cada parte.
- [ ] Sei usar `nodata()`, recovery expression e hysteresis.
- [ ] Sei explicar templates, actions, media types e maintenance.
- [ ] Sei explicar preprocessing e itens unsupported.
- [ ] Fiz simulado de 50 questões em até 60 minutos.

## Checklist ZCP

- [ ] Sei explicar LLD rule, macro, prototype, filter, override e lost resources.
- [ ] Sei diferenciar proxy ativo e passivo.
- [ ] Sei explicar auto-registration e network discovery conceitualmente.
- [ ] Sei interpretar cenários de escala, NAT e filial.
- [ ] Sei planejar automação idempotente usando API ou Ansible.
- [ ] Sei explicar dependent discovery e preprocessamento em escala.
- [ ] Fiz simulado de 75 questões em até 90 minutos.

## Checklist ZCE

- [ ] Sei diagnosticar queue alta com hipóteses técnicas.
- [ ] Sei diferenciar pollers, trappers, preprocessors, cache e gargalos de banco.
- [ ] Sei explicar TLS, PSK, certificados, `TLSConnect` e `TLSAccept`.
- [ ] Sei separar HTTPS do frontend e TLS entre componentes.
- [ ] Sei explicar API tokens, roles, user groups e user types.
- [ ] Sei explicar autenticação LDAP, SAML, MFA e contas break-glass.
- [ ] Sei separar credenciais Zabbix, AWS, Azure, banco e ITSM.
- [ ] Sei raciocinar sobre HA, upgrade, performance e troubleshooting enterprise.

## Critério de prontidão

```text
Abaixo de 70%  -> continuar estudando
70% a 84%      -> revisar lacunas fortes
85% a 94%      -> pronto para simulado final
95% ou mais    -> pronto para revisão leve e prova
```

## Checklist 24 horas antes do exame

- [ ] Revise apenas resumos e erros recorrentes.
- [ ] Não tente aprender assunto novo pesado.
- [ ] Faça um simulado curto.
- [ ] Durma bem.
- [ ] Separe documentos, acesso e ambiente para prova online, se aplicável.
- [ ] Revise diferença entre conceitos parecidos: action vs trigger, maintenance vs acknowledge, API token vs IAM, LDAP/SAML vs ODBC.
