from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),
    path('reiniciar/', views.reiniciar, name='reiniciar'),
    path('missao/<slug:slug>/', views.missao_detail, name='missao_detail'),
    path('desafio/<slug:slug>/', views.desafio_detail, name='desafio_detail'),
]
