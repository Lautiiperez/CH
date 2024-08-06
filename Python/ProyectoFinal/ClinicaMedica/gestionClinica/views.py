from django.shortcuts import render, redirect
from .forms import PacienteForm, MedicoForm, CitaForm
from .models import Paciente, BlogPost
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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
            return redirect('inicio') 
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

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-post_date')
    return render(request, 'gestionClinica/blog_list.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Redirige a la página principal después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio') 