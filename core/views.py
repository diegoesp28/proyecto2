from django.http.response import HttpResponse
from core.models import mascotas
from django.shortcuts import render, redirect
from .forms import MascotaFrom


# Create your views here.
def  home(request):
    mascota=mascotas.objects.all()
    datos = {
        'mascota': mascota
    }
    
    return render(request,'core/home.html',datos)
def index(request):
    return render(request,'core/index.html')
def nosotros(request):
    return render(request,'core/nosotros.html')
def consulta(request):
    return render(request,'core/consulta.html')
def contacto(request):
    return render(request,'core/contactos.html')
def animal(request):
    mascota=mascotas.objects.all()
    datos = {
        'mascota': mascota
    }
    return render(request,'core/animales.html',datos)

def agregar(request):
    datos = {
        'form': MascotaFrom()
    }
    if request.method == 'POST':
        formulario = MascotaFrom(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= "guardados correctamente}"
        else:
            datos['mensaje']= f"error {formulario.is_valid()} {formulario.errors}"

    return render(request,'core/administrador.html',datos)
