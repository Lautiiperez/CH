from django.contrib import admin
from .models import Paciente, Medico, Cita, BlogPost

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Cita)
admin.site.register(BlogPost)
