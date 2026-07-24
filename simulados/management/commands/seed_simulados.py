from django.core.management.base import BaseCommand
from django.utils.text import slugify

from simulados.models import CertificationLevel, Topic, Question, AnswerOption, Simulation

TOPICS = [
    'Itens', 'Triggers', 'Templates', 'Discovery/LLD', 'Actions', 'Proxy',
    'API', 'Segurança', 'Performance', 'Banco de dados', 'Troubleshooting',
    'Frontend', 'Latest data', 'Problems', 'Preprocessing', 'Macros',
]

CERTS = [
    ('ZCU', 'Zabbix Certified User', 'Operação, leitura de problemas, dashboards e dados recentes.'),
    ('ZCS', 'Zabbix Certified Specialist', 'Configuração de coleta, triggers, templates, alertas e preprocessing.'),
    ('ZCP', 'Zabbix Certified Professional', 'Escala, LLD, proxy, automação, correlação e integração.'),
    ('ZCE', 'Zabbix Certified Expert', 'Arquitetura, performance, segurança, banco de dados e troubleshooting avançado.'),
]

SCENARIOS = [
    ('Um host parou de coletar dados e o operador precisa confirmar se há valores recentes.', 'Abrir Latest data do host e validar timestamp, item, valor mais recente e status do item.', 'Latest data'),
    ('Uma trigger dispara falso positivo após picos curtos de CPU.', 'Ajustar a expressão com função e janela temporal coerentes, além de recovery quando necessário.', 'Triggers'),
    ('Um item dependent não recebe dados mesmo com item master coletando JSON.', 'Validar item master, preprocessing, JSONPath, tipo de informação e erro de processamento.', 'Preprocessing'),
    ('Uma regra LLD criou protótipos incorretos para interfaces ignoradas.', 'Revisar filtros, macros LLD e overrides antes de alterar prototypes.', 'Discovery/LLD'),
    ('Uma action não enviou alerta apesar do problema ativo.', 'Verificar condições, operações, media type, período ativo, severidade e usuário/grupo destinatário.', 'Actions'),
    ('Um proxy está atrasando coleta em uma unidade remota.', 'Analisar queue, logs, conectividade, processos e sincronização do proxy.', 'Proxy'),
    ('A API retorna erro de permissão ao listar hosts.', 'Validar token, role, método usado e permissão nos grupos de hosts.', 'API'),
    ('O banco cresceu rapidamente após mudança de intervalo de coleta.', 'Rever retenção de history/trends, itens volumosos, housekeeping e intervalo de coleta.', 'Banco de dados'),
    ('O frontend está lento ao abrir Problems.', 'Investigar volume de eventos, filtros, banco, índices, caches e housekeeping.', 'Performance'),
    ('Um usuário precisa permissão limitada apenas para leitura.', 'Aplicar menor privilégio com role e permissão por grupo de hosts.', 'Segurança'),
    ('Um template foi associado ao host errado.', 'Corrigir vínculo e revisar herança de itens, triggers, discovery e macros.', 'Templates'),
    ('Uma macro de template não está sendo aplicada ao host.', 'Verificar precedência de macro global, template e host, além de nome e contexto da macro.', 'Macros'),
    ('Uma web scenario falha, mas a aplicação responde no navegador.', 'Validar URL, proxy, TLS, códigos HTTP esperados, autenticação e tempo de resposta.', 'Itens'),
    ('Um problema aparece em Problems, mas não dispara notificação.', 'Diferenciar geração de evento de envio de notificação e revisar action, media e período.', 'Problems'),
    ('Um item SNMP retorna no console, mas não coleta no Zabbix.', 'Validar interface SNMP, comunidade/credenciais, OID, timeout e tipo do item.', 'Itens'),
    ('Uma trigger com nodata() gerou alerta fora do horário esperado.', 'Confirmar intervalo de coleta, schedules, manutenção, proxy e função nodata().', 'Triggers'),
    ('O gráfico não mostra dados embora o item tenha valores.', 'Verificar histórico, tipo de item, período selecionado e widget/gráfico configurado.', 'Frontend'),
    ('O Zabbix agent ativo não aparece como disponível.', 'Conferir ServerActive, Hostname, logs do agent e conectividade com o server/proxy.', 'Troubleshooting'),
    ('Uma discovery de rede encontrou hosts demais.', 'Ajustar ranges, checks, critérios de uniqueness e ações de discovery.', 'Discovery/LLD'),
    ('Uma correlação deveria fechar eventos duplicados.', 'Revisar tags, condições de correlação e regras de fechamento.', 'Triggers'),
    ('O cache do server fica constantemente acima do limite.', 'Analisar métricas internas, caches, processos e ajuste de parâmetros do server.', 'Performance'),
    ('A retenção de trends não atende ao relatório mensal.', 'Configurar período de trends e entender diferença entre history e trends.', 'Banco de dados'),
    ('Um token de API foi criado, mas integração falha em produção.', 'Validar expiração, escopo, usuário dono, permissões e endpoint correto.', 'API'),
    ('Uma manutenção não suprimiu alertas como esperado.', 'Revisar tipo de manutenção, período ativo, hosts incluídos e comportamento com dados coletados.', 'Actions'),
    ('Um template importado criou conflito de UUID ou nome.', 'Revisar opções de importação, update existing e dependências do template.', 'Templates'),
    ('Um item de log coleta dados demais e afeta performance.', 'Ajustar key, filtro, intervalo, retenção e triggers associadas.', 'Itens'),
    ('A fila de coleta cresce em horários específicos.', 'Relacionar carga, pollers, unreachable pollers, proxy e quantidade de itens.', 'Performance'),
    ('A descoberta de filesystem cria alerta para mounts temporários.', 'Usar filtros LLD, macros e overrides para excluir mounts não relevantes.', 'Discovery/LLD'),
    ('O usuário vê hosts, mas não consegue executar ação esperada.', 'Verificar role, permissões por grupo, acesso ao módulo e restrições do frontend.', 'Segurança'),
    ('Uma trigger deveria recuperar, mas permanece em problema.', 'Validar recovery expression, último valor, janela de tempo e nova coleta.', 'Triggers'),
    ('O histórico de item some antes do esperado.', 'Revisar configuração de history no item/template, housekeeping e overrides.', 'Banco de dados'),
    ('Um dependent item transforma valor errado do master item.', 'Revisar ordem de preprocessing, JSONPath, regex e tipo de saída.', 'Preprocessing'),
    ('Um dashboard operacional está poluído e pouco útil.', 'Selecionar widgets por objetivo, filtros, Problems, Latest data e mapas necessários.', 'Frontend'),
    ('Uma integração via webhook não recebe parâmetros corretos.', 'Revisar media type, script, macros disponíveis e logs de action.', 'Actions'),
    ('Um proxy novo não recebe configuração.', 'Validar nome do proxy, PSK/certificado, logs, conectividade e modo ativo/passivo.', 'Proxy'),
    ('Uma consulta API lista hosts, mas não retorna interfaces.', 'Usar selectInterfaces/output adequado e validar permissão no objeto.', 'API'),
    ('A autenticação de usuários precisa ser endurecida.', 'Revisar roles, MFA/SSO quando disponível, grupos e princípio do menor privilégio.', 'Segurança'),
    ('Um template deve ser reutilizável entre ambientes.', 'Usar macros, tags, nomes padronizados, dependências e herança limpa.', 'Templates'),
    ('Um problema crítico precisa ser documentado para auditoria.', 'Registrar evidência, timestamps, valores, tela Problems e decisão operacional.', 'Problems'),
    ('O item não suportado precisa ser investigado.', 'Abrir detalhes do item, erro de coleta, logs, key, credenciais e interface.', 'Troubleshooting'),
    ('O intervalo de coleta alterado causou ruído nas triggers.', 'Reavaliar janelas de trigger considerando novo intervalo e estabilidade do dado.', 'Triggers'),
    ('Uma métrica deve ser calculada a partir de outras.', 'Usar calculated item quando fizer sentido e validar expressão/frequência.', 'Itens'),
    ('Um item HTTP agent retorna JSON complexo.', 'Configurar HTTP agent, headers, autenticação e preprocessing JSONPath.', 'Preprocessing'),
    ('Um ambiente grande precisa reduzir carga no server central.', 'Distribuir coleta com proxy e ajustar processos/caches conforme métricas internas.', 'Proxy'),
    ('Uma pergunta pede diferença entre problema e evento.', 'Explicar que eventos são ocorrências geradas e problema é o estado problemático visível em Problems.', 'Problems'),
    ('Um operador precisa confirmar se problema é atual ou histórico.', 'Usar Problems, Latest data, período, reconhecimento e atualização do item.', 'Latest data'),
    ('Uma trigger depende de outra infraestrutura comum.', 'Configurar dependência para reduzir alertas derivados e preservar causa raiz.', 'Triggers'),
    ('Uma regra de escalonamento deve avisar equipes diferentes.', 'Configurar steps, condições, operações e media por equipe/tempo.', 'Actions'),
    ('O banco apresenta consultas lentas em tabelas de histórico.', 'Revisar volume, retenção, particionamento quando aplicável, índices e housekeeping.', 'Banco de dados'),
    ('Um incidente exige troubleshooting completo.', 'Seguir evidência: logs, latest data, queue, events, configuração e documentação oficial.', 'Troubleshooting'),
]

QUESTION_TEMPLATES = [
    'Qual é a ação mais adequada neste cenário de administração Zabbix?',
    'Qual verificação deve ser feita primeiro para evitar diagnóstico incorreto?',
    'Qual alternativa representa a melhor prática para resolver o problema?',
    'Qual caminho reduz risco e preserva evidências operacionais?',
    'Qual resposta demonstra entendimento correto do recurso do Zabbix?',
]

WRONG_OPTIONS = [
    'Reiniciar todos os serviços sem consultar logs, dados recentes ou configuração.',
    'Desabilitar alertas para reduzir ruído sem investigar a causa raiz.',
    'Apagar histórico, eventos ou templates antes de confirmar o impacto.',
    'Alterar thresholds de forma ampla sem validar o comportamento da métrica.',
    'Ignorar permissões, logs e evidências porque o problema parece visual.',
]

REFERENCE_BY_TOPIC = {
    'Itens': 'https://www.zabbix.com/documentation/current/en/manual/config/items/item',
    'Triggers': 'https://www.zabbix.com/documentation/current/en/manual/config/triggers/trigger',
    'Templates': 'https://www.zabbix.com/documentation/current/en/manual/config/templates/template',
    'Discovery/LLD': 'https://www.zabbix.com/documentation/current/en/manual/discovery/low_level_discovery',
    'Actions': 'https://www.zabbix.com/documentation/current/en/manual/config/notifications/action',
    'Proxy': 'https://www.zabbix.com/documentation/current/en/manual/distributed_monitoring/proxies',
    'API': 'https://www.zabbix.com/documentation/current/en/manual/api',
    'Segurança': 'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/permissions',
    'Performance': 'https://www.zabbix.com/documentation/current/en/manual/appendix/performance_tuning',
    'Banco de dados': 'https://www.zabbix.com/documentation/current/en/manual/config/items/history_and_trends',
    'Troubleshooting': 'https://www.zabbix.com/documentation/current/en/manual',
    'Frontend': 'https://www.zabbix.com/documentation/current/en/manual/web_interface',
    'Latest data': 'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/latest_data',
    'Problems': 'https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/monitoring/problems',
    'Preprocessing': 'https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing',
    'Macros': 'https://www.zabbix.com/documentation/current/en/manual/config/macros',
}

class Command(BaseCommand):
    help = 'Popula simulados completos com 50 perguntas por certificação e banco autoral suficiente.'

    def handle(self, *args, **opts):
        certs = {}
        for i, (code, name, desc) in enumerate(CERTS, 1):
            certs[code], _ = CertificationLevel.objects.update_or_create(
                code=code,
                defaults={'name': name, 'description': desc, 'order': i},
            )

        topics = {}
        for topic_name in TOPICS:
            topics[topic_name], _ = Topic.objects.update_or_create(
                slug=slugify(topic_name),
                defaults={'name': topic_name, 'description': f'Tópico: {topic_name}'},
            )

        for code, cert in certs.items():
            definitions = [
                (Simulation.QUICK, 'Simulado rápido', 10, 15),
                (Simulation.FULL, 'Simulado completo', 50, 120),
                (Simulation.LAB, 'Laboratório Zabbix', 10, 40),
                (Simulation.REVIEW, 'Revisão de erros', 20, 30),
            ]
            for sim_type, title, count, duration in definitions:
                sim, _ = Simulation.objects.update_or_create(
                    title=f'{code} - {title}',
                    defaults={
                        'certification': cert,
                        'simulation_type': sim_type,
                        'question_count': count,
                        'duration_minutes': duration,
                        'description': f'{title} - {count} perguntas',
                        'active': True,
                    },
                )
                if sim_type in [Simulation.LAB, Simulation.REVIEW]:
                    sim.topics.set(topics.values())

        created = 0
        for code, cert in certs.items():
            for n in range(50):
                scenario, correct, topic_name = SCENARIOS[n % len(SCENARIOS)]
                template = QUESTION_TEMPLATES[n % len(QUESTION_TEMPLATES)]
                topic = topics[topic_name]
                statement = f'[{code}] {scenario} {template} Questão completa {n + 1:02d}/50.'
                q, was_created = Question.objects.update_or_create(
                    statement=statement,
                    defaults={
                        'certification': cert,
                        'topic': topic,
                        'difficulty': ['facil', 'media', 'dificil'][n % 3],
                        'correct_explanation': f'A alternativa correta preserva evidências, valida o recurso no Zabbix e segue a documentação oficial. Caminho esperado: {correct}',
                        'wrong_explanation': 'As alternativas incorretas pulam diagnóstico, mascaram o problema, removem evidências ou mudam configuração sem validação.',
                        'reference': REFERENCE_BY_TOPIC.get(topic_name, 'https://www.zabbix.com/documentation/current/en/manual'),
                        'requires_lab': n % 5 == 0,
                        'active': True,
                    },
                )
                if was_created:
                    created += 1
                AnswerOption.objects.filter(question=q).delete()
                wrong_pool = [w for w in WRONG_OPTIONS if w != correct]
                options = [correct] + wrong_pool[:3]
                for order, text in enumerate(options, 1):
                    AnswerOption.objects.create(
                        question=q,
                        text=text,
                        is_correct=(order == 1),
                        order=order,
                        explanation='Correta: esta opção valida causa raiz e usa o recurso adequado.' if order == 1 else 'Incorreta: esta opção não confirma causa raiz ou pode ocultar evidências.',
                    )

        total = Question.objects.count()
        totals_by_cert = ', '.join(f'{code}: {Question.objects.filter(certification=certs[code]).count()}' for code in certs)
        self.stdout.write(self.style.SUCCESS(f'Seed simulados concluído. Novas: {created}. Total: {total}. Por certificação: {totals_by_cert}.'))
