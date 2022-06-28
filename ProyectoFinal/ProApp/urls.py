from django.urls import path
from ProApp import views

urlpatterns = [
    path('inicio', views.inicio, name = 'Inicio'),
    path('autos', views.autos, name = 'Autos'),
    path('motos', views.motos, name = 'Motos'),
    path('camiones', views.camiones, name = 'Camiones'),
    path('buscar/', views.buscar, name='Buscar'),
   
]

