from django.urls import path
from . import views
from .views import insertar_paciente, insertar_medico, insertar_cita, buscar_pacientes, inicio, blog_list, register, login_view, logout_view

urlpatterns = [
    path('insertar_paciente/', insertar_paciente, name='insertar_paciente'),
    path('insertar_medico/', insertar_medico, name='insertar_medico'),
    path('insertar_cita/', insertar_cita, name='insertar_cita'),
    path('buscar_pacientes/', buscar_pacientes, name='buscar_pacientes'),
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),
    path('blog/', blog_list, name='blog_list'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]
