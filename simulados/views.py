from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .models import CertificationLevel, Simulation, SimulationAttempt, AttemptAnswer, UserProgress

def user_for(request):
    if request.user.is_authenticated: return request.user
    user,_ = User.objects.get_or_create(username='aluno-demo', defaults={'email':'aluno@example.com'})
    return user

def dashboard(request):
    user = user_for(request)
    cards=[]
    for level in CertificationLevel.objects.all():
        cards.append({
            'level': level,
            'progress': UserProgress.objects.filter(user=user, certification=level).first(),
            'simulations': Simulation.objects.filter(certification=level, active=True).order_by('simulation_type'),
            'running': SimulationAttempt.objects.filter(user=user, simulation__certification=level, status=SimulationAttempt.IN_PROGRESS).order_by('-started_at').first(),
        })
    return render(request, 'simulados/dashboard.html', {'cards': cards})

def start_attempt(request, simulation_id):
    user = user_for(request)
    sim = get_object_or_404(Simulation, id=simulation_id, active=True)
    running = SimulationAttempt.objects.filter(user=user, simulation=sim, status=SimulationAttempt.IN_PROGRESS).first()
    if running: return redirect('simulados:attempt', attempt_id=running.id)
    attempt = SimulationAttempt.objects.create(user=user, simulation=sim, duration_minutes=sim.duration_minutes)
    questions = list(sim.question_queryset(user=user))
    if not questions:
        messages.warning(request, 'Nenhuma questão disponível. Execute python manage.py seed_simulados.')
        attempt.delete(); return redirect('simulados:dashboard')
    for q in questions: AttemptAnswer.objects.create(attempt=attempt, question=q)
    return redirect('simulados:attempt', attempt_id=attempt.id)

def attempt_view(request, attempt_id):
    user = user_for(request)
    attempt = get_object_or_404(SimulationAttempt, id=attempt_id, user=user)
    answers = list(attempt.answers.select_related('question','selected_option','question__topic').prefetch_related('question__options'))
    current = max(1, min(int(request.GET.get('q', 1)), len(answers) or 1))
    if request.method == 'POST' and attempt.status == SimulationAttempt.IN_PROGRESS:
        action = request.POST.get('action')
        if action == 'finish':
            attempt.finish(); return redirect('simulados:result', attempt_id=attempt.id)
        ans = get_object_or_404(AttemptAnswer, id=request.POST.get('answer_id'), attempt=attempt)
        ans.answer(option_id=request.POST.get('option'), marked=('mark' in request.POST))
        if action == 'next': current = min(len(answers), current + 1)
        if action == 'prev': current = max(1, current - 1)
        return redirect(f'{request.path}?q={current}')
    stats = {'total': len(answers), 'answered': sum(bool(a.selected_option_id) for a in answers), 'marked': sum(a.marked_for_review for a in answers)}
    return render(request, 'simulados/attempt.html', {'attempt': attempt, 'answers': answers, 'selected': answers[current-1] if answers else None, 'current': current, 'stats': stats, 'end_at_iso': attempt.end_at.isoformat()})

def result(request, attempt_id):
    user = user_for(request)
    attempt = get_object_or_404(SimulationAttempt, id=attempt_id, user=user)
    if attempt.status != SimulationAttempt.FINISHED: attempt.finish()
    wrong = attempt.answers.filter(is_correct=False).select_related('question','selected_option').prefetch_related('question__options')
    perf = attempt.performance_by_topic()
    return render(request, 'simulados/result.html', {'attempt': attempt, 'wrong': wrong, 'performance': perf, 'weak': [p for p in perf if p['percent'] < 70]})

def history(request, code=None):
    user = user_for(request)
    qs = SimulationAttempt.objects.filter(user=user).select_related('simulation','simulation__certification').order_by('-started_at')
    if code: qs = qs.filter(simulation__certification__code=code)
    rows = []
    for a in qs:
        rows.append({'id': a.id, 'started': a.started_at.strftime('%d/%m/%Y %H:%M'), 'cert': a.simulation.certification.code, 'title': a.simulation.title, 'status': a.get_status_display(), 'score': a.score_percent})
    return render(request, 'simulados/history.html', {'attempts': rows})
