from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .forms import visitanteForm
from mainSistema.models import Visitante
# Create your views here.


def inicio(request):
    return render(request,"index.html")

def visitante(request):
    return render(request,"layouts/visitante.html")

def ingreso(request):
    return render(request,'layouts/ingreso.html')

def dispositivos(request):
    return render(request,"layouts/dispositivos.html")

def puntos_de_control(request):
    return render(request,"layouts/puntos_de_control.html")

def permisos(request):
    return render(request,"layouts/permisos.html")

def reporte_visitante(request):
    return render(request,"layouts/reporte_visitante.html")

def generar_QR(request):
    return render(request,"layouts/generarQR.html")

def crearVisitante (request):
    formularioVISI = visitanteForm(request.POST or None)
    return render(request,"paginas/layout/visitante.html",{'formularioVISI':formularioVISI})

def pruebas_DB(request,nombre,apellidos,documento,fecha_nac,cargo,organizacion,permiso):
  

    nuevo_visit = Visitante(
        nombre = nombre,
        apellido = apellidos,
        documento = documento,
        fechaNacimiento = fecha_nac,
        cargo = cargo,
        organizacion = organizacion,
        permiso = permiso
    
        
    )

    nuevo_visit.save()
   
    return HttpResponse(f"El visitante {nuevo_visit.nombres} ha sido guardado")


def get_visitante (request):
    try:
        visitante = Visitante.objects.get(id = 15)
        response = f"el visitante solicitado es : {visitante.nombres }{visitante.apellidos}"
    except:
        response = "el visitante no existe"

    return HttpResponse (visitante)


def save_visitante(request):

    if request.method == 'POST':
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]
        documento = request.POST["documento"]
        fecha_nac = request.POST["fecha_nac"]
        cargo = request.POST["cargo"]
        organizacion = request.POST["organizacion"]
        permiso = request.POST["permiso"]
   


        visit = Visitante(

            nombre = nombres,
            apellido = apellidos,
            documento = documento,
            fechaNacimiento = fecha_nac,
            cargo = cargo,
            organizacion = organizacion,
            permiso = permiso


        )
        visit.save()

        return redirect("inicio")
    
    else:
        return redirect("inicio")

def pruebas_orm(request):

    visitas = visitante.objects.all('nombres', 'apellidos', 'documento').values

    return JsonResponse({
        'visitantes' : list(visitas)


    }, status=200)




