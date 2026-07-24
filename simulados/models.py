from django.conf import settings
from django.db import models
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta

class CertificationLevel(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    class Meta: ordering = ['order']
    def __str__(self): return self.code

class Topic(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True)
    description = models.TextField(blank=True)
    class Meta: ordering = ['name']
    def __str__(self): return self.name

class Question(models.Model):
    DIFFICULTY_CHOICES = [('facil','Fácil'),('media','Média'),('dificil','Difícil')]
    statement = models.TextField(unique=True)
    certification = models.ForeignKey(CertificationLevel, on_delete=models.PROTECT, related_name='questions')
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, related_name='questions')
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES, default='media')
    correct_explanation = models.TextField()
    wrong_explanation = models.TextField()
    reference = models.CharField(max_length=255, blank=True)
    requires_lab = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    def __str__(self): return self.statement[:80]
    @property
    def correct_option(self): return self.options.filter(is_correct=True).first()

class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    explanation = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    class Meta: ordering = ['order','id']
    def __str__(self): return self.text[:60]

class Simulation(models.Model):
    QUICK, FULL, TOPIC, REVIEW, LAB = 'rapido','completo','topico','revisao','laboratorio'
    TYPE_CHOICES = [(QUICK,'Simulado rápido'),(FULL,'Simulado completo'),(TOPIC,'Por tópico'),(REVIEW,'Modo revisão'),(LAB,'Modo laboratório')]
    title = models.CharField(max_length=140, unique=True)
    certification = models.ForeignKey(CertificationLevel, on_delete=models.PROTECT, related_name='simulations')
    simulation_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=QUICK)
    topics = models.ManyToManyField(Topic, blank=True)
    question_count = models.PositiveSmallIntegerField(default=10)
    duration_minutes = models.PositiveSmallIntegerField(default=20)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    def __str__(self): return self.title
    def question_queryset(self, user=None):
        qs = Question.objects.filter(active=True, certification=self.certification)
        if self.topics.exists(): qs = qs.filter(topic__in=self.topics.all())
        if self.simulation_type == self.LAB: qs = qs.filter(requires_lab=True)
        if self.simulation_type == self.REVIEW and user:
            wrong = AttemptAnswer.objects.filter(attempt__user=user, is_correct=False).values_list('question_id', flat=True)
            qs = qs.filter(id__in=wrong)
        return qs.distinct().order_by('?')[:self.question_count]

class SimulationAttempt(models.Model):
    IN_PROGRESS, FINISHED = 'em_andamento','finalizada'
    STATUS_CHOICES = [(IN_PROGRESS,'Em andamento'),(FINISHED,'Finalizada')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='simulation_attempts')
    simulation = models.ForeignKey(Simulation, on_delete=models.PROTECT, related_name='attempts')
    started_at = models.DateTimeField(default=timezone.now)
    finished_at = models.DateTimeField(null=True, blank=True)
    duration_minutes = models.PositiveSmallIntegerField(default=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=IN_PROGRESS)
    score_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    @property
    def end_at(self): return self.started_at + timedelta(minutes=self.duration_minutes)
    @property
    def time_used_seconds(self): return int(((self.finished_at or timezone.now()) - self.started_at).total_seconds())
    def calculate_score(self):
        total = self.answers.count(); correct = self.answers.filter(is_correct=True).count()
        self.score_percent = round((correct * 100 / total), 2) if total else 0
        return self.score_percent
    def finish(self):
        for a in self.answers.select_related('selected_option'):
            a.is_correct = bool(a.selected_option and a.selected_option.is_correct); a.save(update_fields=['is_correct'])
        self.calculate_score(); self.finished_at = timezone.now(); self.status = self.FINISHED
        self.save(update_fields=['score_percent','finished_at','status'])
        UserProgress.refresh_for_user(self.user, self.simulation.certification)
    def performance_by_topic(self):
        rows = self.answers.values('question__topic__name').annotate(total=Count('id'), correct=Count('id', filter=Q(is_correct=True))).order_by('question__topic__name')
        return [{'topic': r['question__topic__name'], 'total': r['total'], 'correct': r['correct'], 'percent': round(r['correct']*100/r['total'], 1) if r['total'] else 0} for r in rows]

class AttemptAnswer(models.Model):
    attempt = models.ForeignKey(SimulationAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    selected_option = models.ForeignKey(AnswerOption, null=True, blank=True, on_delete=models.SET_NULL)
    marked_for_review = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)
    answered_at = models.DateTimeField(null=True, blank=True)
    class Meta: unique_together = ('attempt','question')
    def answer(self, option_id=None, marked=None):
        if self.attempt.status == SimulationAttempt.FINISHED: return
        if option_id: self.selected_option_id = int(option_id); self.answered_at = timezone.now()
        if marked is not None: self.marked_for_review = bool(marked)
        self.is_correct = bool(self.selected_option and self.selected_option.is_correct)
        self.save()

class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    certification = models.ForeignKey(CertificationLevel, on_delete=models.CASCADE)
    best_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    attempts_count = models.PositiveIntegerField(default=0)
    average_time_seconds = models.PositiveIntegerField(default=0)
    last_attempt_at = models.DateTimeField(null=True, blank=True)
    class Meta: unique_together = ('user','certification')
    @classmethod
    def refresh_for_user(cls, user, cert):
        attempts = SimulationAttempt.objects.filter(user=user, simulation__certification=cert, status=SimulationAttempt.FINISHED)
        obj,_ = cls.objects.get_or_create(user=user, certification=cert)
        obj.attempts_count = attempts.count(); obj.best_score = max([a.score_percent for a in attempts] or [0])
        obj.average_time_seconds = int(sum(a.time_used_seconds for a in attempts)/obj.attempts_count) if obj.attempts_count else 0
        obj.last_attempt_at = attempts.order_by('-finished_at').values_list('finished_at', flat=True).first()
        obj.save(); return obj
