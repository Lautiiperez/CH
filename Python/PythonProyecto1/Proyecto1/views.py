from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
    return HttpResponse("Hola Django - Lauti")

def segunda_vista(request):
    return HttpResponse("<br><br>Segunda Pruena :D")

def dia_hoy(request):
    dia = datetime.datetime.now()
    texto = f"Hoy es el dia: <br> {dia}"
    return HttpResponse(texto)

def mi_nombre(self, nombre):
    texto = f"Mi nombre es <bt>{nombre}"
    return HttpResponse(texto)

def template1(self):
    miHtml = open(r"C:\Users\Lautaro Perez\Documents\CH\Python\PythonProyecto1\Proyecto1\plantillas\template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)