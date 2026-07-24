from django.urls import path
from . import views
app_name = 'game'
urlpatterns = [
    path('', views.home, name='home'),
    path('casos/', views.case_center, name='case_center'),
    path('casos/<slug:cert>/', views.certification_detail, name='certification_detail'),
    path('estudos/', views.study_resources_index, name='study_resources'),
    path('estudos/checklist/', views.checklist_preparacao, name='checklist_preparacao'),
    path('estudos/gabarito/', views.answer_key_index, name='answer_key_index'),
    path('estudos/gabarito/casos/<slug:cert>/', views.answer_key_cases_cert, name='answer_key_cases_cert'),
    path('estudos/gabarito/extras/<slug:slug>/', views.answer_key_extra_mission, name='answer_key_extra_mission'),
    path('estudos/guia/<slug:cert>/', views.study_guide_cert, name='study_guide_cert'),
    path('estudos/revisao/<slug:cert>/', views.revision_plan_cert, name='revision_plan_cert'),
    path('estudos/dicas/<slug:cert>/', views.tips_cert, name='tips_cert'),
    path('estudos/<slug:slug>/', views.study_resource_detail, name='study_resource_detail'),
    path('missao/<int:mission_id>/', views.mission_detail, name='mission_detail'),
    path('missao/<slug:slug>/', views.mission_detail_slug, name='mission_detail_slug'),
    path('desafio/<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    path('desafio/<slug:slug>/', views.challenge_detail_slug, name='challenge_detail_slug'),
]
