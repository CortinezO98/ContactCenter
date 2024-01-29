from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

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
    return render(request, 'index.html')

