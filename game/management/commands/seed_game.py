from django.core.management.base import BaseCommand
from django.utils.text import slugify
from game.models import Mission, Challenge, ChallengeOption

MAIN = [
 ('M01','Primeiros passos no Frontend','zcu','ZCU','Navegação por Problems, Latest data, hosts e dashboards.'),
 ('M02','Operação de problemas','zcu-operacao','ZCU','Acknowledge, tags, severidade, eventos e maintenance.'),
 ('M03','Coleta básica','zcs-coleta','ZCS','Criar e validar itens, interfaces e intervalos.'),
 ('M04','Triggers confiáveis','zcs-triggers','ZCS','Montar expressões, recovery e reduzir falso positivo.'),
 ('M05','Templates e herança','zcs-templates','ZCS','Vincular templates, macros e entender herança.'),
 ('M06','Actions e notificações','zcs-actions','ZCS','Configurar media types, condições e escalonamento.'),
 ('M07','Preprocessing e dependent items','zcp-preprocessing','ZCP','Transformar dados e criar itens dependentes.'),
 ('M08','Discovery e LLD','zcp-lld','ZCP','Criar regras LLD, filtros, protótipos e overrides.'),
 ('M09','Proxy distribuído','zcp-proxy','ZCP','Operar proxy, fila e sincronização.'),
 ('M10','API e automação','zcp-api','ZCP','Usar JSON-RPC de forma segura e idempotente.'),
 ('M11','Segurança avançada','zce-seguranca','ZCE','Roles, tokens, grupos, hardening e auditoria.'),
 ('M12','Performance e banco','zce-performance','ZCE','Caches, pollers, history/trends, housekeeping e DB.'),
]

EXTRA = [
 ('X01','Monitoring','monitoring','Treine investigação de incidentes usando Problems, Latest data, gráficos, mapas, eventos, reconhecimento e análise de impacto.'),
 ('X02','Services','services','Modele serviços, SLA, dependências e impacto de negócio para transformar eventos técnicos em leitura operacional.'),
 ('X03','Inventory','inventory','Use inventário manual e automático para enriquecer hosts, localizar ativos e apoiar auditoria operacional.'),
 ('X04','Reports','reports','Construa relatórios de disponibilidade, top triggers, auditoria e leituras executivas com período e filtro corretos.'),
 ('X05','Data collection','data-collection','Pratique hosts, interfaces, itens, tipos de informação, preprocessing, dependent items e retenção.'),
 ('X06','Alerts','alerts','Configure actions, media types, escalonamento, mensagens, destinatários e janelas operacionais.'),
 ('X07','Users','users','Gerencie usuários, grupos, roles e permissões por escopo com princípio do menor privilégio.'),
 ('X08','Administration','administration','Explore housekeeping, audit, frontend, proxies, filas, autenticação e parâmetros administrativos.'),
 ('X09','Automação API','automacao-api','Automatize operações com JSON-RPC, tokens, consultas idempotentes e criação segura de objetos.'),
 ('X10','Segurança','seguranca','Pratique hardening, tokens, roles, TLS, segregação, auditoria e controle de acesso.'),
 ('X11','Ansible','ansible','Automatize criação de hosts, templates, macros e padronização de inventário com playbooks.'),
 ('X12','AWS','aws','Integre monitoramento cloud, discovery, tags, métricas e credenciais de forma segura.'),
 ('X13','Bancos de Dados','bancos-de-dados','Monitore PostgreSQL/MySQL, locks, conexões, crescimento, queries lentas e impacto no Zabbix.'),
 ('X14','Zabbix Proxy','zabbix-proxy','Aprofunde proxy ativo/passivo, sincronização, last seen, buffer offline, fila, TLS/PSK, hosts atribuídos e troubleshooting.'),
]

DOC_URLS = {
 'Monitoring':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems',
 'Latest data':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data',
 'Services':'https://www.zabbix.com/documentation/current/en/manual/it_services',
 'Inventory':'https://www.zabbix.com/documentation/current/en/manual/config/hosts/inventory',
 'Reports':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/reports',
 'Items':'https://www.zabbix.com/documentation/current/en/manual/config/items/item',
 'Preprocessing':'https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing',
 'Actions':'https://www.zabbix.com/documentation/current/en/manual/config/notifications/action',
 'Users':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/user_list',
 'Roles':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/user_roles',
 'Administration':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration',
 'API':'https://www.zabbix.com/documentation/current/en/manual/api',
 'Security':'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/permissions',
 'Proxy':'https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies',
 'Ansible':'https://www.zabbix.com/integrations/ansible',
 'AWS':'https://www.zabbix.com/integrations/aws',
 'Database':'https://www.zabbix.com/integrations/postgresql',
 'ZCU':'https://www.zabbix.com/documentation/current/en/manual',
 'ZCS':'https://www.zabbix.com/documentation/current/en/manual/config',
 'ZCP':'https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring',
 'ZCE':'https://www.zabbix.com/documentation/current/en/manual/appendix/performance_tuning',
}

def doc_ref(topic):
    return f'{topic} - documentação oficial|{DOC_URLS.get(topic, "https://www.zabbix.com/documentation/current/en/manual")}'

MAIN_TASKS = [
 ('Validar tela correta','Abra a tela indicada, identifique objetivo e registre evidência.', 'A prática reforça navegação, leitura de contexto e raciocínio antes de alterar configuração.'),
 ('Executar ajuste controlado','Faça a mudança em ambiente de teste e valide efeito.', 'Mudança controlada reduz risco operacional e permite reverter se a validação falhar.'),
 ('Documentar diagnóstico','Registre sintoma, causa provável, evidência e ação.', 'Documentação torna troubleshooting repetível e melhora comunicação com outros times.'),
]

EXTRA_TOPICS = {
 'monitoring': ['Problems críticos','Latest data atrasado','Gráfico de tendência','Reconhecimento de problema','Filtros por tags','Eventos recentes','Mapas operacionais','Correlação visual','Problema histórico','Evidência do incidente'],
 'services': ['Serviço de negócio','SLA mensal','Dependência entre serviços','Propagação de impacto','Tags de serviço','Janela de SLA','Causa raiz de serviço','Serviço pai e filho','Relatório de SLA','Impacto executivo'],
 'inventory': ['Inventário automático','Campo manual','Filtro por localidade','Inventário por SO','Patrimônio do host','Owner operacional','Inventário e auditoria','Inventário por grupo','Dados coletados','Governança do inventário'],
 'reports': ['Availability report','Top triggers','Audit report','Relatório executivo','Período correto','Filtro de grupos','Relatório de problemas','SLA report','Resumo mensal','Evidência para auditoria'],
 'data-collection': ['Tipo de item','Key correta','Interface do host','Preprocessing JSON','Dependent item','History e trends','Intervalo de coleta','Item não suportado','HTTP agent','SNMP item'],
 'alerts': ['Action por severidade','Media type','Escalonamento','Período ativo','Usuário destinatário','Mensagem com macros','Teste de envio','Acknowledge','Condição por tag','Ruído de alerta'],
 'users': ['Grupo de usuários','Role customizada','Permissão por host group','Usuário somente leitura','Auditoria de acesso','Menor privilégio','Acesso ao frontend','Time por ambiente','Restrição de módulo','Teste de permissão'],
 'administration': ['Housekeeping','Audit log','Proxy status','Frontend settings','Authentication','Queue','Internal checks','Maintenance','Global scripts','Parâmetros do server'],
 'automacao-api': ['Token de API','host.get','host.create','template massadd','Idempotência','Erro de permissão','selectInterfaces','Macros via API','Tratamento de erro','Automação segura'],
 'seguranca': ['Token mínimo','TLS/PSK','Roles','Permissões','Auditoria','Segregação por ambiente','Usuário de integração','Hardening frontend','Rotação de segredo','Privilégio mínimo'],
 'ansible': ['Inventário Ansible','Variáveis por grupo','Playbook idempotente','Templates via API','Macros via Ansible','Vault','Rollback','Validação pós-playbook','Separação por ambiente','Reuso de role'],
 'aws': ['Métrica CloudWatch','Tags AWS','IAM mínimo','Discovery AWS','Intervalo e custo','Região','Credencial segura','Filtro por ambiente','Templates AWS','Limite de API'],
 'bancos-de-dados': ['Conexões','Locks','Queries lentas','Tamanho de history','Trends','Housekeeping DB','Índices','Backup','Crescimento de tabela','Impacto no frontend'],
 'zabbix-proxy': ['Proxy ativo','Proxy passivo','Last seen','Hosts atribuídos','Buffer offline','Fila do proxy','TLS/PSK','Sincronização config','Logs do proxy','Sizing do proxy'],
}

TOPIC_KIND = {
 'monitoring':'Monitoring','services':'Services','inventory':'Inventory','reports':'Reports','data-collection':'Items','alerts':'Actions','users':'Users','administration':'Administration','automacao-api':'API','seguranca':'Security','ansible':'Ansible','aws':'AWS','bancos-de-dados':'Database','zabbix-proxy':'Proxy'
}

WRONGS = [
 'Reiniciar serviços, limpar dados ou desabilitar alertas antes de confirmar a causa raiz.',
 'Alterar thresholds de forma ampla sem revisar documentação, histórico e impacto.',
 'Ignorar permissões, logs, período, tags e evidências porque o sintoma parece simples.',
 'Remover objetos ou histórico para esconder ruído operacional sem corrigir configuração.',
]

def detailed_explanation(mission_title, topic, correct):
    return (
        f'Esta missão extra aprofunda o tema {mission_title} usando uma situação prática de {topic}. '
        f'Antes de responder, pense no fluxo completo: qual dado o Zabbix coleta, como esse dado é processado, onde a informação aparece no frontend e qual decisão operacional deve ser tomada.\n\n'
        f'O ponto central é evitar resposta decorada. Em ambiente real, uma ação apressada pode mascarar incidente, reduzir evidência ou criar ruído. A resposta correta é a alternativa que preserva diagnóstico, valida o estado real do recurso e usa o componente certo do Zabbix.\n\n'
        f'Para este caso, o caminho esperado é: {correct} Depois disso, compare o resultado com a documentação oficial e registre evidência objetiva: tela acessada, filtro usado, host/grupo afetado, horário, valor observado e decisão tomada.'
    )

def make_challenge(mission, slug, title, idx):
    kind = TOPIC_KIND[slug]
    correct = f'Validar {title.lower()} no Zabbix usando a tela ou recurso apropriado, conferir evidências, consultar a documentação oficial e só então aplicar ajuste controlado.'
    task = f'Qual alternativa representa a melhor ação para o cenário "{title}" dentro da missão {mission.title}?'
    steps = (
        'Abra o Zabbix Lab pelo botão desta página.\n'
        f'Localize o recurso relacionado a {title}.\n'
        'Compare o que a tela mostra com o objetivo da pergunta.\n'
        'Consulte a documentação indicada antes de concluir.\n'
        'Registre evidência e responda a alternativa de múltipla escolha.'
    )
    checks = (
        'Identifiquei a tela/recurso correto no Zabbix.\n'
        'Comparei dado, evento, permissão ou configuração com o cenário.\n'
        'Consultei a documentação oficial indicada.\n'
        'Escolhi a alternativa com menor risco operacional.\n'
        'Registrei evidência nas anotações.'
    )
    ch = Challenge.objects.create(
        mission=mission,
        slug=f'{slug}-{slugify(title)}-{idx}',
        title=title,
        study_topic=kind,
        scenario=f'Cenário guiado de {mission.title}: {title}. O objetivo é transformar teoria em decisão operacional segura.',
        task=task,
        step_by_step=steps,
        explanation=detailed_explanation(mission.title, title, correct),
        expected_result='Resposta de múltipla escolha salva, evidência validada no Zabbix Lab e checklist concluído.',
        checklist=checks,
        official_reference=doc_ref(kind),
        difficulty=['facil','media','dificil'][idx % 3],
        order=idx,
        active=True,
    )
    options = [
        (correct, True, 'Correta: a alternativa valida evidências, usa o recurso certo do Zabbix e evita alterações sem diagnóstico.'),
        (WRONGS[(idx + 0) % len(WRONGS)], False, 'Incorreta: a alternativa pula validação e pode ocultar evidências importantes.'),
        (WRONGS[(idx + 1) % len(WRONGS)], False, 'Incorreta: a alternativa altera ambiente sem confirmar causa raiz.'),
        (WRONGS[(idx + 2) % len(WRONGS)], False, 'Incorreta: a alternativa não usa documentação nem validação prática.'),
    ]
    for order, (text, ok, explanation) in enumerate(options, 1):
        ChallengeOption.objects.create(challenge=ch, text=text, is_correct=ok, explanation=explanation, order=order)
    return ch

class Command(BaseCommand):
    help='Popula dashboard, missões principais e missões extras com múltipla escolha.'

    def handle(self, *args, **kwargs):
        Mission.objects.all().delete()
        for idx,(code,title,slug,cert,summary) in enumerate(MAIN,1):
            mission = Mission.objects.create(
                code=code, title=title, slug=slug, certification=cert, track=Mission.TRACK_MAIN,
                summary=summary,
                objective='Aprender como fazer no Zabbix com cenário, execução prática, explicação e checklist. A Central de Casos mantém foco em laboratório guiado e evidência operacional.',
                order=idx, unlocked_by_default=True, active=True,
            )
            for n in range(1,9):
                base = MAIN_TASKS[(n+idx)%len(MAIN_TASKS)]
                Challenge.objects.create(
                    mission=mission, slug=f'{slug}-lab-{n}', title=f'{base[0]} #{n}', study_topic=cert,
                    scenario=f'Cenário: {summary}', task=base[0], step_by_step=base[1].replace('. ','.\n'),
                    explanation=base[2], expected_result='Laboratório validado e evidência registrada.',
                    checklist='Abriu tela correta\nValidou evidência\nRegistrou conclusão', official_reference=doc_ref(cert),
                    difficulty=['facil','media','dificil'][n%3], order=n, active=True,
                )
        offset = 100
        for idx,(code,title,slug,summary) in enumerate(EXTRA,1):
            mission = Mission.objects.create(
                code=code, title=title, slug=slug, certification='', track=Mission.TRACK_EXTRA,
                summary=summary,
                objective=(
                    'Missão extra com pelo menos 10 perguntas de múltipla escolha. Cada pergunta traz explicação detalhada, execução prática no Zabbix Lab, documentação oficial e checklist. '
                    'Use a missão para treinar raciocínio: entender o cenário, escolher a alternativa correta, abrir o laboratório, validar evidência e registrar conclusão.'
                ),
                order=offset+idx, unlocked_by_default=True, active=True,
            )
            for order, challenge_title in enumerate(EXTRA_TOPICS[slug], 1):
                make_challenge(mission, slug, challenge_title, order)
        self.stdout.write(self.style.SUCCESS(
            f'Missões recriadas. Principais: {len(MAIN)} | Extras: {len(EXTRA)} | Desafios: {Challenge.objects.count()} | Opções: {ChallengeOption.objects.count()}'
        ))
