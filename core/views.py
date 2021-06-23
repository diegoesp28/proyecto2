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
    data = {'form':MascotaFrom()}
    if request.method == 'POST':
        formulario = MascotaFrom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] ='mascota guardado'
        else:
            data['form']= formulario

    return render(request,'core/administrador.html',data)
