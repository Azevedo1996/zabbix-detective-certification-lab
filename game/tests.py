from django.test import TestCase
from django.contrib.auth.models import User
from .models import Mission, Challenge, ChallengeAttempt, PlayerProgress
class GameTests(TestCase):
    def test_lab_progress(self):
        u=User.objects.create_user('aluno')
        m=Mission.objects.create(code='M01',title='Missão',summary='s')
        c=Challenge.objects.create(mission=m,title='Lab',study_topic='Itens',scenario='s',task='fazer',step_by_step='passo 1',explanation='e',expected_result='ok',checklist='validou')
        ChallengeAttempt.objects.create(user=u,challenge=c,status='concluido')
        p=PlayerProgress.refresh(u,m)
        self.assertEqual(p.completed_challenges,1)
