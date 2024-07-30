from django.shortcuts import render, redirect
from .forms import PacienteForm, MedicoForm, CitaForm
from .models import Paciente

def insertar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige después de guardar
    else:
        form = PacienteForm()
    return render(request, 'insertar_paciente.html', {'form': form})

def insertar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige después de guardar
    else:
        form = MedicoForm()
    return render(request, 'insertar_medico.html', {'form': form})

def insertar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige después de guardar
    else:
        form = CitaForm()
    return render(request, 'insertar_cita.html', {'form': form})

def buscar_pacientes(request):
    query = request.GET.get("q")
    if query:
        pacientes = Paciente.objects.filter(nombre__icontains=query)
    else:
        pacientes = None
    return render(request, 'buscar_pacientes.html', {'pacientes': pacientes})

def inicio(request):
    return render(request, 'gestionClinica/index.html') 

