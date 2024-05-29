from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password'] == request.POST['confirmP']:
            try:
                #registrando un usuario
                user = User.objects.create_user(username=request.POST['usuario'],password=request.POST['password'])
                user.save()
                login(request,user)
                return redirect('inicio')
            except IntegrityError:
                return render(request,'signup.html',{
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request,'signup.html',{
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def signin(request):

    if request.method =='GET':    
        return render(request,'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['usuario'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request,user)
            return redirect('inicio')

def inicio(request):
    return render(request,'inicio.html')

def signout(request):
    logout(request)
    return redirect('signin')

import pandas as pd
from django.shortcuts import render
from django.db import connections
from .models import AccidentesHmo
from django.db.models import Sum

def inicio(request):
    # Obtener la suma de muertos y heridos por año
    suma_por_anio = (
        AccidentesHmo.objects
        .values('anio')
        .annotate(total_muertos=Sum('suma_muertos'), total_heridos=Sum('suma_heridos'))
        .order_by('anio')
    )

    # Preparar los datos para la gráfica
    anios = [dato['anio'] for dato in suma_por_anio]
    total_muertos = [dato['total_muertos'] for dato in suma_por_anio]
    total_heridos = [dato['total_heridos'] for dato in suma_por_anio]

    context = {
        'anios': anios,
        'total_muertos': total_muertos,
        'total_heridos': total_heridos,
    }
    return render(request, 'inicio.html', context)

