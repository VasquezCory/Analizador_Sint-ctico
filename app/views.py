from django.shortcuts import render
# Create your views here.
#Peticiones/Respuestas
from django.http import HttpRequest
#Vistas genéricas
from django.views import generic

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'home.html'
    )

def perfil(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'perfil.html'
    )

def discos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'discos.html'
    )

def creditos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'creditos.html'
    )

def ventaDiscos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'ventaDiscos.html'
    )