from django.conf import settings
from django.db import models
from django.utils import timezone

class Mission(models.Model):
    TRACK_MAIN = 'principal'
    TRACK_EXTRA = 'extra'
    TRACK_CHOICES = [(TRACK_MAIN, 'Eixo principal'), (TRACK_EXTRA, 'Missões extras')]
    code = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    title = models.CharField(max_length=140)
    certification = models.CharField(max_length=12, blank=True)
    track = models.CharField(max_length=20, choices=TRACK_CHOICES, default=TRACK_MAIN)
    summary = models.TextField()
    objective = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    unlocked_by_default = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['track', 'order', 'id']
    def __str__(self): return self.title
    @property
    def total_challenges(self): return self.challenges.filter(active=True).count()

class Challenge(models.Model):
    EASY, MEDIUM, HARD = 'facil', 'media', 'dificil'
    DIFFICULTY_CHOICES = [(EASY, 'Fácil'), (MEDIUM, 'Média'), (HARD, 'Difícil')]
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='challenges')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    title = models.CharField(max_length=160)
    study_topic = models.CharField(max_length=100, blank=True)
    scenario = models.TextField(help_text='Cenário prático do laboratório')
    task = models.TextField(default='', blank=True, help_text='O que o aluno deve fazer')
    step_by_step = models.TextField(default='', blank=True, help_text='Passo a passo de execução')
    explanation = models.TextField(help_text='Explicação técnica e raciocínio')
    expected_result = models.TextField(default='', blank=True)
    checklist = models.TextField(default='', blank=True)
    official_reference = models.CharField(max_length=255, blank=True)
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES, default=MEDIUM)
    order = models.PositiveSmallIntegerField(default=0)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['mission__order', 'order', 'id']
    def __str__(self): return f'{self.mission.code} - {self.title}'
    def steps(self): return [s.strip() for s in self.step_by_step.splitlines() if s.strip()]
    def checks(self): return [s.strip() for s in self.checklist.splitlines() if s.strip()]
    @property
    def correct_option(self): return self.options.filter(is_correct=True).first()


class ChallengeOption(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='options')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    explanation = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    class Meta:
        ordering = ['order', 'id']
    def __str__(self): return self.text[:80]

class ChallengeAttempt(models.Model):
    STATUS_CHOICES = [('iniciado','Iniciado'),('concluido','Concluído')]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='attempts')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='iniciado')
    notes = models.TextField(blank=True)
    selected_option = models.ForeignKey('ChallengeOption', null=True, blank=True, on_delete=models.SET_NULL)
    is_correct = models.BooleanField(default=False)  # compatível com progresso antigo
    answered_at = models.DateTimeField(default=timezone.now)
    class Meta: ordering = ['-answered_at']
    def save(self, *args, **kwargs):
        self.is_correct = bool(self.selected_option and self.selected_option.is_correct) if self.selected_option_id else self.status == 'concluido'
        super().save(*args, **kwargs)

class PlayerProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    completed_challenges = models.PositiveIntegerField(default=0)
    last_activity_at = models.DateTimeField(null=True, blank=True)
    class Meta: unique_together = ('user', 'mission')
    @classmethod
    def refresh(cls, user, mission):
        done = ChallengeAttempt.objects.filter(user=user, challenge__mission=mission, status='concluido').values('challenge_id').distinct().count()
        obj, _ = cls.objects.get_or_create(user=user, mission=mission)
        obj.completed_challenges = done
        obj.last_activity_at = timezone.now()
        obj.save()
        return obj
