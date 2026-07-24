from django.urls import path
from . import views
app_name='simulados'
urlpatterns=[
 path('', views.dashboard, name='dashboard'),
 path('iniciar/<int:simulation_id>/', views.start_attempt, name='start'),
 path('tentativa/<int:attempt_id>/', views.attempt_view, name='attempt'),
 path('resultado/<int:attempt_id>/', views.result, name='result'),
 path('historico/', views.history, name='history'),
 path('historico/<str:code>/', views.history, name='history_level'),
]
