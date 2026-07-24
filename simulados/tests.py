from unittest.mock import patch
from django.contrib.auth.models import User
from django.test import TestCase
from .models import *
from .services import ZabbixAPIClient
class SimulationTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user('leo')
        self.cert=CertificationLevel.objects.create(code='ZCU',name='ZCU')
        self.topic=Topic.objects.create(name='Itens',slug='itens')
        self.sim=Simulation.objects.create(title='ZCU rápido',certification=self.cert,question_count=1)
        self.q=Question.objects.create(statement='Q1',certification=self.cert,topic=self.topic,correct_explanation='ok',wrong_explanation='no')
        self.ok=AnswerOption.objects.create(question=self.q,text='ok',is_correct=True)
        self.no=AnswerOption.objects.create(question=self.q,text='no')
    def test_finish_score(self):
        a=SimulationAttempt.objects.create(user=self.user,simulation=self.sim)
        AttemptAnswer.objects.create(attempt=a,question=self.q,selected_option=self.ok)
        a.finish(); self.assertEqual(float(a.score_percent),100.0)
    def test_wrong_score(self):
        a=SimulationAttempt.objects.create(user=self.user,simulation=self.sim)
        AttemptAnswer.objects.create(attempt=a,question=self.q,selected_option=self.no)
        a.finish(); self.assertEqual(float(a.score_percent),0.0)
    @patch.object(ZabbixAPIClient,'call')
    def test_zabbix_api_mock(self,mock_call):
        mock_call.side_effect=['7.0.0','token']
        self.assertTrue(ZabbixAPIClient().validate_connection()['logged'])
