from django.http import HttpResponse
from django.template import Template, Context, loader
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
    nom = "nombre"
    ap= "apellido"
    listaNotas=[1,2,3,4,5]
    diccionario = {"nombre":nom, "apellido":ap, "hoy":datetime.datetime.now(), "notas":listaNotas}

    # miHtml = open(r"C:\Users\Lautaro Perez\Documents\CH\Python\PythonProyecto1\Proyecto1\plantillas\template1.html")
    # plantilla = Template(miHtml.read())
    # miHtml.close()
    # miContexto = Context(diccionario)
    # documento = plantilla.render(miContexto)
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)