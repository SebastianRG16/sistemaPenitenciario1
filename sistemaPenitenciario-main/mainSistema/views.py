from django.shortcuts import render
from django.http import HttpResponse
from .forms import VisitanteForm
# Create your views here.


def inicio(request):
    return render(request,"paginas/inicio.html")


def crearVisitante (request):
    formularioVISI = VisitanteForm(request.POST or None)
    return render(request,"paginas/crearVisitante.html",{'formularioVISI':formularioVISI})