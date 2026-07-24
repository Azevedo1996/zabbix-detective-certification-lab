from django.shortcuts import get_object_or_404, redirect, render

from .models import Desafio, Fase, Missao


DOCS = {
    'trilha-zcu': {
        'titulo': 'Zabbix 7.0 Manual - operação, GUI e conceitos',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual',
    },
    'trilha-zcs': {
        'titulo': 'Items e Triggers - configuração oficial',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual/config/items/item',
    },
    'trilha-zcp': {
        'titulo': 'Triggers, LLD, history/trends e escala',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual/config/triggers/expression',
    },
    'trilha-zce': {
        'titulo': 'Encryption, API, HA, performance e segurança',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual/encryption',
    },
    'security-lab': {
        'titulo': 'Encryption, Authentication, LDAP/SAML/MFA e hardening',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual/encryption',
    },
    'ansible-automation-lab': {
        'titulo': 'Ansible community.zabbix collection',
        'url': 'https://docs.ansible.com/projects/ansible/latest/collections/community/zabbix/index.html',
    },
    'trilha-automacao': {
        'titulo': 'Zabbix API JSON-RPC',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual/api',
    },
    'aws-monitoring-lab': {
        'titulo': 'Zabbix AWS by HTTP integration',
        'url': 'https://www.zabbix.com/integrations/aws',
    },
    'database-monitoring-lab': {
        'titulo': 'Zabbix Database monitor / ODBC checks',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual/config/items/itemtypes/odbc_checks',
    },
    'azure-monitoring-lab': {
        'titulo': 'Zabbix Microsoft Azure by HTTP integration',
        'url': 'https://www.zabbix.com/integrations/azure',
    },
    'authentication-sso-lab': {
        'titulo': 'Zabbix Authentication, API tokens and permissions',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/authentication',
    },
}


def normalizar_sem_espaco(valor):
    return ''.join(str(valor or '').strip().lower().split())


def get_concluidos(request):
    return set(request.session.get('desafios_concluidos', []))


def get_fase_atual(request):
    return int(request.session.get('fase_atual', 1))


def nav_missoes():
    return Missao.objects.exclude(categoria=Missao.Categoria.PRINCIPAL).order_by('ordem')


def doc_para(missao):
    return DOCS.get(missao.slug, {
        'titulo': 'Zabbix 7.0 Documentation',
        'url': 'https://www.zabbix.com/documentation/7.0/en/manual',
    })


def progresso_missao(missao, concluidos):
    total = missao.desafios.count()
    done = missao.desafios.filter(slug__in=concluidos).count()
    percent = int((done / total) * 100) if total else 0
    return {'total': total, 'done': done, 'percent': percent}


def missao_liberada(request, missao):
    if not missao.is_principal:
        return True
    return missao.fase and missao.fase.ordem <= get_fase_atual(request)


def marcar_concluido(request, desafio):
    concluidos = get_concluidos(request)
    concluidos.add(desafio.slug)
    request.session['desafios_concluidos'] = sorted(concluidos)
    missao = desafio.missao
    if missao.is_principal and missao.desafios.exclude(slug__in=concluidos).count() == 0:
        proxima = missao.fase.ordem + 1
        if Fase.objects.filter(ordem=proxima).exists():
            request.session['fase_atual'] = max(get_fase_atual(request), proxima)
    request.session.modified = True


def validar(desafio, post):
    resposta = desafio.resposta or {}
    if desafio.tipo == Desafio.Tipo.TEXTO:
        enviado = normalizar_sem_espaco(post.get('answer'))
        aceitas = [normalizar_sem_espaco(v) for v in resposta.get('accepted', [])]
        return enviado in aceitas
    if desafio.tipo == Desafio.Tipo.MULTIPLA:
        return post.get('answer') in resposta.get('accepted', [])
    if desafio.tipo == Desafio.Tipo.MULTISELECT:
        return set(post.getlist('answer')) == set(resposta.get('accepted', []))
    if desafio.tipo == Desafio.Tipo.FORMULARIO:
        for field, expected in resposta.get('fields', {}).items():
            if normalizar_sem_espaco(post.get(field)) not in [normalizar_sem_espaco(v) for v in expected]:
                return False
        return True
    return False


def index(request):
    concluidos = get_concluidos(request)
    principais = Missao.objects.filter(categoria=Missao.Categoria.PRINCIPAL).select_related('fase').order_by('ordem')
    principais_info = []
    total_principal = 0
    done_principal = 0
    for missao in principais:
        prog = progresso_missao(missao, concluidos)
        total_principal += prog['total']
        done_principal += prog['done']
        principais_info.append({
            'missao': missao,
            'progresso': prog,
            'doc': doc_para(missao),
            'liberada': missao_liberada(request, missao),
        })
    overall = int((done_principal / total_principal) * 100) if total_principal else 0
    return render(request, 'game/index.html', {
        'principais_info': principais_info,
        'fase_atual': get_fase_atual(request),
        'overall': overall,
        'done_principal': done_principal,
        'total_principal': total_principal,
        'concluidos': concluidos,
        'nav_missoes': nav_missoes(),
    })


def missao_detail(request, slug):
    missao = get_object_or_404(Missao.objects.select_related('fase'), slug=slug)
    if not missao_liberada(request, missao):
        return redirect('game:index')
    concluidos = get_concluidos(request)
    desafios = missao.desafios.all()
    return render(request, 'game/missao.html', {
        'missao': missao,
        'desafios': desafios,
        'concluidos': concluidos,
        'progresso': progresso_missao(missao, concluidos),
        'doc': doc_para(missao),
        'nav_missoes': nav_missoes(),
    })


def desafio_detail(request, slug):
    desafio = get_object_or_404(Desafio.objects.select_related('missao__fase'), slug=slug)
    if not missao_liberada(request, desafio.missao):
        return redirect('game:index')
    sucesso = False
    feedback = None
    explicacao = None
    if request.method == 'POST':
        sucesso = validar(desafio, request.POST)
        if sucesso:
            marcar_concluido(request, desafio)
            feedback = 'Correto. Missão registrada no dossiê.'
            explicacao = desafio.explicacao_correta
        else:
            feedback = 'Ainda não. Veja a explicação e tente novamente.'
            explicacao = desafio.explicacoes_incorretas.get(request.POST.get('answer'), desafio.dica or desafio.contexto)
    proximo = desafio.missao.desafios.filter(ordem__gt=desafio.ordem).first()
    return render(request, desafio.template_name, {
        'desafio': desafio,
        'missao': desafio.missao,
        'sucesso': sucesso,
        'feedback': feedback,
        'explicacao': explicacao,
        'proximo': proximo,
        'doc': doc_para(desafio.missao),
        'nav_missoes': nav_missoes(),
    })


def reiniciar(request):
    request.session.flush()
    return redirect('game:index')
