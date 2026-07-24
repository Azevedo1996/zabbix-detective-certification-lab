from pathlib import Path
import html

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Mission, Challenge, ChallengeOption, ChallengeAttempt, PlayerProgress
from .study_resources import STUDY_RESOURCES, get_study_resource, cert_payload, CERT_ORDER

CERTS = [
    {
        'code': 'ZCU',
        'phase': 'Fase 1',
        'level': 'Básico',
        'title': 'ZCU - Fundamentos e Operação Visual',
        'summary': 'Preparação para Zabbix Certified User: GUI, arquitetura, problemas, filtros, dashboards e conceitos essenciais.',
        'doc_label': 'Zabbix manual - operação, GUI e conceitos',
        'doc_url': 'https://www.zabbix.com/documentation/current/en/manual/web_interface',
    },
    {
        'code': 'ZCS',
        'phase': 'Fase 2',
        'level': 'Intermediário',
        'title': 'ZCS - Implantação e Configuração',
        'summary': 'Preparação para Zabbix Certified Specialist: instalação, hosts, itens, triggers, templates, ações, macros, SNMP e LLD básico.',
        'doc_label': 'Itens, triggers e templates - configuração oficial',
        'doc_url': 'https://www.zabbix.com/documentation/current/en/manual/config',
    },
    {
        'code': 'ZCP',
        'phase': 'Fase 3',
        'level': 'Avançado',
        'title': 'ZCP - Automação e Escala',
        'summary': 'Preparação para Zabbix Certified Professional: proxy, LLD avançado, preprocessing, correlação, discovery e ambientes distribuídos.',
        'doc_label': 'Proxy, LLD, preprocessing e escala',
        'doc_url': 'https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring',
    },
    {
        'code': 'ZCE',
        'phase': 'Fase 4',
        'level': 'Expert',
        'title': 'ZCE - Expertise, Performance e Segurança',
        'summary': 'Preparação para Zabbix Certified Expert: tuning, HA, segurança, API, processos internos, bancos e troubleshooting avançado.',
        'doc_label': 'Performance, segurança, API e HA',
        'doc_url': 'https://www.zabbix.com/documentation/current/en/manual/appendix/performance_tuning',
    },
]
CERT_MAP = {c['code']: c for c in CERTS}


def demo_user(request):
    if request.user.is_authenticated:
        return request.user
    user, _ = User.objects.get_or_create(username='aluno-demo', defaults={'email': 'aluno@example.com'})
    return user


def all_extra_missions():
    return Mission.objects.filter(active=True, track=Mission.TRACK_EXTRA).order_by('order', 'title')


def all_main_phases():
    return Mission.objects.filter(active=True, track=Mission.TRACK_MAIN).order_by('order', 'title')


def missions_for_cert(cert):
    return Mission.objects.filter(active=True, track=Mission.TRACK_MAIN, certification=cert).order_by('order', 'title')


def _progress_for_mission(user, mission):
    total = mission.challenges.filter(active=True).count()
    done = ChallengeAttempt.objects.filter(user=user, challenge__mission=mission, status='concluido').values('challenge_id').distinct().count()
    percent = round(done * 100 / total, 1) if total else 0
    return {'mission': mission, 'total': total, 'done': done, 'percent': percent}


def _progress_for_cert(user, cert):
    meta = CERT_MAP[cert]
    missions = missions_for_cert(cert)
    total = Challenge.objects.filter(active=True, mission__in=missions).count()
    done = ChallengeAttempt.objects.filter(user=user, challenge__mission__in=missions, status='concluido').values('challenge_id').distinct().count()
    percent = round(done * 100 / total, 1) if total else 0
    return {
        **meta,
        'missions': missions,
        'total': total,
        'done': done,
        'percent': percent,
        'mission_rows': [_progress_for_mission(user, m) for m in missions],
    }


def _certification_progress(user):
    return [_progress_for_cert(user, cert['code']) for cert in CERTS]


def home(request):
    user = demo_user(request)
    main = list(all_main_phases())
    extra = list(all_extra_missions())
    total_challenges = Challenge.objects.filter(active=True).count()
    solved = ChallengeAttempt.objects.filter(user=user, status='concluido').values('challenge_id').distinct().count()
    total_percent = round(solved * 100 / total_challenges, 1) if total_challenges else 0
    cert_progress = _certification_progress(user)
    phase_progress = [_progress_for_mission(user, m) for m in main]
    extra_progress = [_progress_for_mission(user, m) for m in extra]
    return render(request, 'game/home.html', {
        'main_missions': main,
        'extra_missions': extra,
        'total_challenges': total_challenges,
        'solved': solved,
        'total_percent': total_percent,
        'cert_progress': cert_progress,
        'phase_progress': phase_progress,
        'extra_progress': extra_progress,
    })


def case_center(request):
    user = demo_user(request)
    cert_rows = _certification_progress(user)
    return render(request, 'game/case_center.html', {'cert_rows': cert_rows})


def certification_detail(request, cert):
    code = cert.upper()
    if code not in CERT_MAP:
        raise Http404('Certificação não encontrada')
    user = demo_user(request)
    row = _progress_for_cert(user, code)
    return render(request, 'game/certification_detail.html', {'cert': row})


def mission_detail(request, mission_id):
    user = demo_user(request)
    mission = get_object_or_404(Mission, id=mission_id, active=True)
    done = set(ChallengeAttempt.objects.filter(user=user, challenge__mission=mission, status='concluido').values_list('challenge_id', flat=True))
    return render(request, 'game/mission_detail.html', {'mission': mission, 'done_ids': done})


def challenge_detail(request, challenge_id):
    user = demo_user(request)
    challenge = get_object_or_404(Challenge, id=challenge_id, active=True)
    attempt = ChallengeAttempt.objects.filter(user=user, challenge=challenge).first()
    if request.method == 'POST':
        status = request.POST.get('status', 'iniciado')
        notes = request.POST.get('notes', '')
        selected_option = None
        option_id = request.POST.get('selected_option')
        if option_id:
            selected_option = get_object_or_404(ChallengeOption, id=option_id, challenge=challenge)
        attempt, _ = ChallengeAttempt.objects.update_or_create(
            user=user,
            challenge=challenge,
            defaults={'status': status, 'notes': notes, 'selected_option': selected_option},
        )
        PlayerProgress.refresh(user, challenge.mission)
        if selected_option:
            messages.success(request, 'Resposta salva. Confira o feedback abaixo.')
        else:
            messages.success(request, 'Progresso do laboratório salvo.')
        return redirect('game:challenge_detail', challenge_id=challenge.id)
    return render(request, 'game/challenge_detail.html', {'challenge': challenge, 'attempt': attempt, **_doc_context(challenge)})


def mission_detail_slug(request, slug):
    user = demo_user(request)
    mission = get_object_or_404(Mission, slug=slug, active=True)
    done = set(ChallengeAttempt.objects.filter(user=user, challenge__mission=mission, status='concluido').values_list('challenge_id', flat=True))
    return render(request, 'game/mission_detail.html', {'mission': mission, 'done_ids': done})


def challenge_detail_slug(request, slug):
    user = demo_user(request)
    challenge = get_object_or_404(Challenge, slug=slug, active=True)
    attempt = ChallengeAttempt.objects.filter(user=user, challenge=challenge).first()
    if request.method == 'POST':
        status = request.POST.get('status', 'iniciado')
        notes = request.POST.get('notes', '')
        selected_option = None
        option_id = request.POST.get('selected_option')
        if option_id:
            selected_option = get_object_or_404(ChallengeOption, id=option_id, challenge=challenge)
        attempt, _ = ChallengeAttempt.objects.update_or_create(
            user=user,
            challenge=challenge,
            defaults={'status': status, 'notes': notes, 'selected_option': selected_option},
        )
        PlayerProgress.refresh(user, challenge.mission)
        if selected_option:
            messages.success(request, 'Resposta salva. Confira o feedback abaixo.')
        else:
            messages.success(request, 'Progresso do laboratório salvo.')
        return redirect('game:challenge_detail_slug', slug=challenge.slug)
    return render(request, 'game/challenge_detail.html', {'challenge': challenge, 'attempt': attempt, **_doc_context(challenge)})


def _doc_context(challenge):
    ref = challenge.official_reference or ''
    if '|' in ref:
        label, url = ref.split('|', 1)
        return {'doc_label': label.strip(), 'doc_url': url.strip()}
    if ref.startswith('http'):
        return {'doc_label': 'Documentação oficial Zabbix', 'doc_url': ref}
    return {'doc_label': ref or 'Documentação oficial Zabbix', 'doc_url': 'https://www.zabbix.com/documentation/current/en/manual'}


def _markdown_to_html(text):
    lines = text.splitlines()
    html_lines = []
    in_list = False
    in_code = False
    code_lines = []
    for raw in lines:
        line = raw.rstrip()
        if line.strip().startswith('```'):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                html_lines.append('<pre><code>' + html.escape('\n'.join(code_lines)) + '</code></pre>')
                in_code = False
            continue
        if in_code:
            code_lines.append(line)
            continue
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            continue
        if stripped.startswith('# '):
            if in_list:
                html_lines.append('</ul>'); in_list = False
            html_lines.append('<h1>' + html.escape(stripped[2:]) + '</h1>')
        elif stripped.startswith('## '):
            if in_list:
                html_lines.append('</ul>'); in_list = False
            html_lines.append('<h2>' + html.escape(stripped[3:]) + '</h2>')
        elif stripped.startswith('### '):
            if in_list:
                html_lines.append('</ul>'); in_list = False
            html_lines.append('<h3>' + html.escape(stripped[4:]) + '</h3>')
        elif stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append('<li>' + html.escape(stripped[2:]) + '</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('<p>' + html.escape(stripped) + '</p>')
    if in_list:
        html_lines.append('</ul>')
    if in_code:
        html_lines.append('<pre><code>' + html.escape('\n'.join(code_lines)) + '</code></pre>')
    return '\n'.join(html_lines)


def study_resources_index(request):
    return render(request, 'game/study_resources.html', {'resources': STUDY_RESOURCES})


def study_resource_detail(request, slug):
    if slug == 'simulados-md':
        return links_simulados_page(request)
    if slug == 'foruns-estudo':
        return forums_page(request)
    if slug == 'triggers-complexas':
        return triggers_complexas_page(request)
    resource = get_study_resource(slug)
    if not resource:
        raise Http404('Material de estudo não encontrado')
    path = Path(settings.BASE_DIR) / resource['file']
    if path.exists():
        content = path.read_text(encoding='utf-8', errors='ignore')
    else:
        content = '# ' + resource['title'] + '\n\nMaterial ainda não encontrado no repositório.'
    return render(request, 'game/study_resource_detail.html', {'resource': resource, 'content_html': _markdown_to_html(content)})


def study_guide_cert(request, cert):
    data = cert_payload(cert)
    if not data:
        raise Http404('Certificação não encontrada')
    return render(request, 'game/cert_study_guide.html', {'cert': data, 'mode': 'guide'})

def revision_plan_cert(request, cert):
    data = cert_payload(cert)
    if not data:
        raise Http404('Certificação não encontrada')
    return render(request, 'game/cert_revision_plan.html', {'cert': data})

def tips_cert(request, cert):
    data = cert_payload(cert)
    if not data:
        raise Http404('Certificação não encontrada')
    return render(request, 'game/cert_tips.html', {'cert': data})


def checklist_preparacao(request):
    checklist = [
        {'section': 'Ambiente', 'items': [
            'Docker Desktop aberto e com engine Linux iniciada.',
            'Projeto iniciado pelo iniciar.bat sem erro no PowerShell.',
            'Zabbix Detective acessível em http://localhost:8989.',
            'Zabbix Lab acessível em http://localhost:4000.',
            'Containers principais em execução: django, zabbix-web, zabbix-server, zabbix-db e zabbix-agent.',
        ]},
        {'section': 'Antes de estudar', 'items': [
            'Escolher apenas uma certificação ou missão extra por bloco de estudo.',
            'Abrir o Guia / Plano de estudo da certificação correspondente.',
            'Ler a documentação oficial do tópico antes de responder.',
            'Anotar objetivo, tela do Zabbix usada e recurso configurado.',
        ]},
        {'section': 'Durante o laboratório', 'items': [
            'Ler o cenário completo antes de clicar em concluir.',
            'Executar o passo a passo no Zabbix Lab quando aplicável.',
            'Validar resultado esperado com evidência: tela, item, trigger, problema, ação ou dado coletado.',
            'Registrar observações no campo de anotações do laboratório.',
        ]},
        {'section': 'Antes de conferir o gabarito', 'items': [
            'Responder com base no raciocínio técnico e não apenas memorizar tela.',
            'Comparar sua resposta com a explicação do laboratório.',
            'Reabrir a documentação oficial do tópico em caso de dúvida.',
            'Marcar como concluído somente após validar todos os itens do checklist do desafio.',
        ]},
        {'section': 'Revisão semanal', 'items': [
            'Revisar desafios errados ou incompletos.',
            'Refazer pelo menos um laboratório por certificação estudada.',
            'Ler novamente os tópicos oficiais com maior erro.',
            'Consultar o gabarito por certificação ou por missão extra para consolidar respostas.',
        ]},
    ]
    return render(request, 'game/checklist_preparacao.html', {'checklist': checklist})


def answer_key_index(request):
    certs = []
    for cert in CERTS:
        missions = missions_for_cert(cert['code'])
        total = Challenge.objects.filter(active=True, mission__in=missions).count()
        certs.append({**cert, 'total': total})
    extras = all_extra_missions()
    return render(request, 'game/answer_key_index.html', {'certs': certs, 'extras': extras})


def answer_key_cases_cert(request, cert):
    code = cert.upper()
    if code not in CERT_MAP:
        raise Http404('Certificação não encontrada')
    missions = missions_for_cert(code).prefetch_related('challenges')
    challenges = Challenge.objects.filter(active=True, mission__in=missions).select_related('mission').order_by('mission__order', 'order', 'title')
    return render(request, 'game/answer_key_detail.html', {
        'title': f'Gabarito · Central de Casos · {code}',
        'subtitle': CERT_MAP[code]['title'],
        'challenges': challenges,
        'scope': 'casos',
    })


def answer_key_extra_mission(request, slug):
    mission = get_object_or_404(Mission, slug=slug, active=True, track=Mission.TRACK_EXTRA)
    challenges = Challenge.objects.filter(active=True, mission=mission).select_related('mission').order_by('order', 'title')
    return render(request, 'game/answer_key_detail.html', {
        'title': f'Gabarito · Missões extras · {mission.title}',
        'subtitle': mission.summary,
        'challenges': challenges,
        'scope': 'extra',
    })


def _links_simulados_data():
    docs = [
        {'theme': 'Documentação oficial / Manual', 'url': 'https://www.zabbix.com/documentation/current/en/manual', 'note': 'Ponto inicial para qualquer tópico oficial.'},
        {'theme': 'Overview e arquitetura', 'url': 'https://www.zabbix.com/documentation/current/en/manual/introduction/overview', 'note': 'Base conceitual para ZCU e ZCS.'},
        {'theme': 'Frontend e navegação', 'url': 'https://www.zabbix.com/documentation/current/en/manual/web_interface', 'note': 'GUI, menus e operação visual.'},
        {'theme': 'Problems', 'url': 'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems', 'note': 'Incidentes, severidade, reconhecimento e filtros.'},
        {'theme': 'Latest data', 'url': 'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data', 'note': 'Validação de coleta, último valor e filtros.'},
        {'theme': 'Hosts', 'url': 'https://www.zabbix.com/documentation/current/en/manual/config/hosts/host', 'note': 'Cadastro de hosts, interfaces e grupos.'},
        {'theme': 'Items', 'url': 'https://www.zabbix.com/documentation/current/en/manual/config/items/item', 'note': 'Coleta, key, intervalos e tipos de informação.'},
        {'theme': 'Triggers', 'url': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger', 'note': 'Expressões, severidade, recuperação e geração de eventos.'},
        {'theme': 'Funções de trigger', 'url': 'https://www.zabbix.com/documentation/current/en/manual/appendix/functions', 'note': 'last, min, max, avg, count, nodata, trendavg e outras funções.'},
        {'theme': 'Templates', 'url': 'https://www.zabbix.com/documentation/current/en/manual/config/templates/template', 'note': 'Padronização e herança.'},
        {'theme': 'Preprocessing', 'url': 'https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing', 'note': 'Tratamento de dados antes do armazenamento.'},
        {'theme': 'Dependent items', 'url': 'https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/dependent_items', 'note': 'Reaproveitamento de payload mestre.'},
        {'theme': 'Low-level discovery', 'url': 'https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery', 'note': 'Descoberta dinâmica e prototypes.'},
        {'theme': 'Actions e notificações', 'url': 'https://www.zabbix.com/documentation/current/en/manual/config/notifications/action', 'note': 'Condições, operações, escalonamento e mensagens.'},
        {'theme': 'Zabbix Proxy', 'url': 'https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies', 'note': 'Coleta distribuída e ambientes remotos.'},
        {'theme': 'Zabbix API', 'url': 'https://www.zabbix.com/documentation/current/en/manual/api', 'note': 'Automação e integração.'},
        {'theme': 'Performance tuning', 'url': 'https://www.zabbix.com/documentation/current/en/manual/appendix/performance_tuning', 'note': 'Performance, cache, pollers e tuning.'},
        {'theme': 'Permissions e roles', 'url': 'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/permissions', 'note': 'Controle de acesso para ZCE.'},
    ]
    practice = [
        {'name': 'ExamTopics - discussões gerais', 'url': 'https://www.examtopics.com/discussions/', 'note': 'Não encontrei categoria Zabbix dedicada; usar a busca do site por Zabbix se disponível.'},
        {'name': 'GitHub - Zabbix Questions Repository', 'url': 'https://github.com/sk3pp3r/zabbix-interview-questions-and-answers', 'note': 'Questões comunitárias por nível: beginner, intermediate e expert.'},
        {'name': 'Zabbix official training', 'url': 'https://www.zabbix.com/training', 'note': 'Material oficial de treinamento e certificação.'},
        {'name': 'Zabbix manual como simulado ativo', 'url': 'https://www.zabbix.com/documentation/current/en/manual', 'note': 'Transforme cada tópico em perguntas: conceito, tela, configuração, erro comum e validação.'},
    ]
    return docs, practice


def _forums_data():
    return [
        {'name': 'Zabbix Forum - geral', 'url': 'https://www.zabbix.com/forum/', 'note': 'Diretório oficial de fóruns Zabbix.'},
        {'name': 'Zabbix Help', 'url': 'https://www.zabbix.com/forum/zabbix-help', 'note': 'Perguntas de uso, configuração e dúvidas gerais.'},
        {'name': 'Troubleshooting and Problems', 'url': 'https://www.zabbix.com/forum/zabbix-troubleshooting-and-problems', 'note': 'Erros, problemas operacionais e bugs.'},
        {'name': 'Zabbix Cookbook', 'url': 'https://www.zabbix.com/forum/zabbix-cookbook', 'note': 'Templates, experiências e casos de monitoramento.'},
        {'name': 'Large Environments', 'url': 'https://www.zabbix.com/forum/zabbix-for-large-environments', 'note': 'Escala, performance, HA e manutenção de ambientes grandes.'},
        {'name': 'Português / Español', 'url': 'https://www.zabbix.com/forum/em-portugues-y-en-espanol', 'note': 'Discussões sobre Zabbix em português e espanhol.'},
        {'name': 'Zabbix Support Issues', 'url': 'https://support.zabbix.com/', 'note': 'Issue tracker oficial para bugs e melhorias.'},
        {'name': 'GitHub questions repository', 'url': 'https://github.com/sk3pp3r/zabbix-interview-questions-and-answers', 'note': 'Repositório comunitário de perguntas para revisão.'},
    ]


def _trigger_complex_topics():
    return [
        {'title': '1. O que é uma trigger', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger', 'text': 'Trigger é a regra que transforma dados coletados em estado operacional. Item coleta valor; trigger avalia expressão; evento/problema nasce quando a expressão fica verdadeira.'},
        {'title': '2. Anatomia da expressão', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/expression', 'text': 'Uma expressão combina item, função, operador e limite. Exemplo conceitual: último valor de disponibilidade igual a indisponível por determinado período.'},
        {'title': '3. Funções essenciais', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/appendix/functions', 'text': 'Use last() para último valor, min()/max() para janela, avg() para média, count() para contagem, nodata() para ausência de dado e funções trend* para análise histórica agregada.'},
        {'title': '4. Janela de tempo', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/appendix/functions', 'text': 'Triggers confiáveis evitam falso positivo usando janelas como 5m, 10m ou 1h. Quanto menor a janela, maior a sensibilidade; quanto maior a janela, maior a estabilidade.'},
        {'title': '5. Severidade', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/severity', 'text': 'Severidade não mede dificuldade técnica; mede impacto operacional. Use Information, Warning, Average, High e Disaster de forma consistente.'},
        {'title': '6. Recovery expression', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger', 'text': 'Recovery expression separa a condição de problema da condição de recuperação. Isso evita oscilação quando o valor fica próximo do limite.'},
        {'title': '7. Histerese', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger', 'text': 'Histerese usa limite de entrada e limite de saída diferentes. Exemplo: problema acima de 90%, recuperação abaixo de 80%.'},
        {'title': '8. Dependências', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/dependencies', 'text': 'Dependências reduzem ruído. Se o roteador caiu, triggers dos hosts atrás dele podem ficar suprimidas para evitar tempestade de alertas.'},
        {'title': '9. Tags de problema', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/event_correlation/trigger-event-generation', 'text': 'Tags permitem filtrar, correlacionar e rotear eventos. Use tags como service, role, location, impact e team.'},
        {'title': '10. Multiple problem events', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger', 'text': 'Algumas triggers podem gerar múltiplos eventos quando faz sentido operacional, mas isso precisa ser usado com critério para não criar ruído.'},
        {'title': '11. Triggers com LLD', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery', 'text': 'Trigger prototypes criam triggers dinamicamente para filesystems, interfaces e recursos descobertos. O desafio é filtrar corretamente o que deve ou não gerar alerta.'},
        {'title': '12. Erros comuns', 'doc': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger', 'text': 'Erros comuns: usar last() sozinho em métrica instável, ignorar nodata(), não separar severidade por impacto, esquecer dependências e criar thresholds sem contexto.'},
    ]


def links_simulados_page(request):
    docs, practice = _links_simulados_data()
    return render(request, 'game/links_simulados.html', {'docs': docs, 'practice': practice})


def forums_page(request):
    return render(request, 'game/forums_study.html', {'forums': _forums_data()})


def triggers_complexas_page(request):
    return render(request, 'game/triggers_complexas.html', {'topics': _trigger_complex_topics()})
