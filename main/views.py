from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from .models import *

def Login(request):
    if request.user.is_authenticated:
        return redirect('main:index')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:index')
        else:
            messages.error(request, 'El usuario o la contraseña son incorrectos.')
            return redirect('main:login')
    else:
        return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('main:login')

@login_required
def index(request):
    if request.method == 'GET' and request.GET.get('documentoCliente'):
        cliente = Cliente.objects.filter(documento=request.GET.get('documentoCliente')).first()
        tipoSolicitudes = TipoSolicitud.objects.all()
        return render(request,'index.html', {"cliente": cliente, "tipoSolicitudes":tipoSolicitudes})

    return render(request, 'index.html')

@login_required
def vistaSolicitud(request, id):
    solicitud = Solicitud.objects.filter(id=id).first()
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    return render(request, 'vistaSolicitud.html', {"solicitud":solicitud, 'fecha_actual': fecha_actual})

@login_required
def crearCliente(request):
    if request.method == 'POST':
        nuevoCliente = Cliente(
            documento = request.POST.get('documento'),
            nombres = request.POST.get('nombres'),
            apellidos = request.POST.get('apellidos'),
            correo = request.POST.get('correo'),
            celular = request.POST.get('celular')
        )
        nuevoCliente.save()
        messages.success(request, 'Se registró el cliente de manera exitosa')
        return redirect(f"/?documentoCliente={nuevoCliente.documento}")
    return redirect("main:index")

@login_required
def crearSolicitud(request):
    if request.method == 'POST':
        agente = Agente.objects.filter(usuario=request.user).first()
        if agente:
            solicitud = Solicitud(
                tipoSolicitud = TipoSolicitud.objects.filter(id=request.POST.get('tipoSolicitudId')).first(),
                llamaEnNombrePropio = request.POST.get('llamaEnNombrePropio'),
                seAgendaCita = request.POST.get('seAgendaCita'),
                quedaCitaEnEspera = request.POST.get('quedaCitaEnEspera'),
                cliente = Cliente.objects.filter(documento=request.POST.get('documentoCliente')).first(),
                agente = agente
            )
            solicitud.save()
            return redirect("main:vistaSolicitud", solicitud.id)
        else:
            messages.info(request, 'Usted no esta autorizado para gestionar una solicitud debido a que no es un agente')
            return redirect("main:index")
    return redirect("main:index")

@login_required
def agendarCita(request):
    if request.method == 'GET' and request.GET.get('documentoCliente') and request.GET.get('fecha'):
        documentoCliente = request.GET.get('documentoCliente')
        fechaStr = request.GET.get('fecha')
        fecha = datetime.strptime(fechaStr, '%Y-%m-%d').date()
        return render(request, 'agendarCita.html', {"fecha":fecha})

    return redirect("main:index")

