CERT_ORDER = ['ZCU', 'ZCS', 'ZCP', 'ZCE']

CERT_META = {
    'ZCU': {'title': 'ZCU - Zabbix Certified User', 'summary': 'Fundamentos de navegação, operação visual, problemas, dados recentes e dashboards.'},
    'ZCS': {'title': 'ZCS - Zabbix Certified Specialist', 'summary': 'Configuração de hosts, itens, triggers, templates, actions, discovery, SNMP e coleta.'},
    'ZCP': {'title': 'ZCP - Zabbix Certified Professional', 'summary': 'Escala, proxy, LLD avançado, preprocessing, API, automação e ambiente distribuído.'},
    'ZCE': {'title': 'ZCE - Zabbix Certified Expert', 'summary': 'Performance, segurança, HA, banco, auditoria e troubleshooting avançado.'},
}

STUDY_GUIDES = {
    'ZCU': [
        {'topic':'Visão geral do Zabbix','why':'Entender arquitetura e conceitos antes de operar o frontend.','url':'https://www.zabbix.com/documentation/current/en/manual/introduction/overview'},
        {'topic':'Frontend e navegação','why':'Saber onde ficam Monitoring, Data collection, Reports e Administration.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface'},
        {'topic':'Problems','why':'Operar incidentes, severidade, tags e reconhecimento de problema.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems'},
        {'topic':'Latest data','why':'Validar último valor, item, timestamp, filtro e comportamento da métrica.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data'},
        {'topic':'Dashboards','why':'Montar visões operacionais para acompanhamento diário.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/dashboard'},
        {'topic':'Maps','why':'Ler impacto visual e topologia de incidentes.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/maps'},
    ],
    'ZCS': [
        {'topic':'Hosts','why':'Configurar entidades monitoradas, interfaces, grupos e templates.','url':'https://www.zabbix.com/documentation/current/en/manual/config/hosts/host'},
        {'topic':'Items','why':'Definir coleta, key, intervalos, informação e histórico.','url':'https://www.zabbix.com/documentation/current/en/manual/config/items/item'},
        {'topic':'Preprocessing','why':'Transformar valores antes de armazenar e criar itens dependentes.','url':'https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing'},
        {'topic':'Triggers','why':'Criar expressões confiáveis para alertas.','url':'https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger'},
        {'topic':'Templates','why':'Padronizar coleta, triggers, gráficos, discovery e macros.','url':'https://www.zabbix.com/documentation/current/en/manual/config/templates/template'},
        {'topic':'Actions e notificações','why':'Configurar condições, operações, escalações e media types.','url':'https://www.zabbix.com/documentation/current/en/manual/config/notifications/action'},
        {'topic':'Low-level discovery','why':'Descobrir filesystems, interfaces e entidades repetíveis automaticamente.','url':'https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery'},
        {'topic':'SNMP','why':'Monitorar dispositivos de rede e equipamentos via OID/MIB.','url':'https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/snmp'},
    ],
    'ZCP': [
        {'topic':'Zabbix proxy','why':'Distribuir coleta e monitorar ambientes remotos/segmentados.','url':'https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies'},
        {'topic':'Proxy setup','why':'Entender modos, sincronização, last seen e operação de proxy.','url':'https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies/proxy'},
        {'topic':'LLD avançado','why':'Usar filtros, prototypes e overrides para escala.','url':'https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery'},
        {'topic':'Dependent items','why':'Reaproveitar payloads mestre e reduzir coleta repetida.','url':'https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/dependent_items'},
        {'topic':'HTTP agent','why':'Coletar APIs e endpoints HTTP.','url':'https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/http'},
        {'topic':'Zabbix API','why':'Automatizar criação, leitura e manutenção do ambiente.','url':'https://www.zabbix.com/documentation/current/en/manual/api'},
        {'topic':'Event correlation','why':'Reduzir ruído e correlacionar eventos em ambientes grandes.','url':'https://www.zabbix.com/documentation/current/en/manual/config/event_correlation'},
    ],
    'ZCE': [
        {'topic':'Performance tuning','why':'Ajustar caches, pollers, workers e gargalos do server.','url':'https://www.zabbix.com/documentation/current/en/manual/appendix/performance_tuning'},
        {'topic':'Housekeeping','why':'Controlar retenção de history, trends e eventos.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/housekeeping'},
        {'topic':'History and trends','why':'Entender armazenamento e impacto no banco.','url':'https://www.zabbix.com/documentation/current/en/manual/config/items/history_and_trends'},
        {'topic':'High availability','why':'Projetar Zabbix server em HA.','url':'https://www.zabbix.com/documentation/current/en/manual/concepts/server/ha'},
        {'topic':'Permissions','why':'Segregar acesso por grupos e permissões.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/permissions'},
        {'topic':'User roles','why':'Controlar acesso funcional por perfil.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles'},
        {'topic':'Encryption','why':'Proteger comunicação entre componentes.','url':'https://www.zabbix.com/documentation/current/en/manual/encryption'},
        {'topic':'Audit log','why':'Rastrear alterações para segurança e troubleshooting.','url':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/reports/audit'},
    ],
}

REVISION_PLANS = {cert: [
    {'day':'Segunda-feira','focus':'Ler documentação oficial dos 2 primeiros tópicos e anotar conceitos-chave.'},
    {'day':'Terça-feira','focus':'Executar 1 laboratório prático ligado aos tópicos lidos.'},
    {'day':'Quarta-feira','focus':'Revisar erros, refazer checklist e registrar evidência.'},
    {'day':'Quinta-feira','focus':'Ler os próximos tópicos da documentação oficial.'},
    {'day':'Sexta-feira','focus':'Executar simulado curto e revisar perguntas erradas.'},
    {'day':'Sábado','focus':'Consolidar anotações e criar resumo de telas/comandos.'},
    {'day':'Domingo','focus':'Revisão leve: flashcards, checklist e planejamento da semana.'},
] for cert in CERT_ORDER}

TIPS = {
    'ZCU':['Diferencie Problems de Latest data.','Treine filtros por severidade, host, tags e período.','Quando a pergunta falar em incidente, pense primeiro em Monitoring > Problems.'],
    'ZCS':['Conecte item, trigger, action e media type.','Valide preprocessing antes de culpar a trigger.','Use templates e macros para padronização.'],
    'ZCP':['Pense em escala: proxy, LLD, dependent items e API.','Teste filtros e prototypes antes de aplicar em massa.','Automação precisa ser repetível e segura.'],
    'ZCE':['Performance exige leitura de queue, cache, pollers e banco.','Segurança combina roles, permissões, tokens e criptografia.','Troubleshooting exige logs, métricas internas e evidência objetiva.'],
}

STUDY_RESOURCES = [
    {'slug':'simulados-md','title':'Links e simulados','file':'SIMULADOS.md','description':'Links, orientações e simulados.'},
    {'slug':'foruns-estudo','title':'Fóruns de estudo','file':'FORUNS_ESTUDO.md','description':'Comunidades e fóruns para tirar dúvidas.'},
    {'slug':'triggers-complexas','title':'Triggers complexas','file':'TRIGGERS_COMPLEXAS.md','description':'Estudo focado em triggers avançadas.'},
]

def get_study_resource(slug):
    for item in STUDY_RESOURCES:
        if item['slug'] == slug:
            return item
    return None

def cert_payload(cert):
    code = cert.upper()
    if code not in CERT_META:
        return None
    return {'code': code, **CERT_META[code], 'topics': STUDY_GUIDES[code], 'revision': REVISION_PLANS[code], 'tips': TIPS[code]}
