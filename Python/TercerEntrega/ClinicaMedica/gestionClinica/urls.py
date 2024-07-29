from django.urls import path
from . import views

urlpatterns = [
    path('insertar_paciente/', views.insertar_paciente, name='insertar_paciente'),
    path('insertar_medico/', views.insertar_medico, name='insertar_medico'),
    path('insertar_cita/', views.insertar_cita, name='insertar_cita'),
    path('buscar_pacientes/', views.buscar_pacientes, name='buscar_pacientes'),
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
]
