from django.http.response import HttpResponse
from core.models import mascotas
from django.shortcuts import render, redirect
from .forms import MascotaFrom, AnimalFrom


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
        datos['configuracion']= ""
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= f"Guardados Correctamente"
            datos['configuracion']= "alert alert-success"
        else:
            datos['mensaje']= f"error {formulario.is_valid()}"
            datos['configuracion']= "alert alert-danger"

    return render(request,'core/agregar.html',datos)

def animalADD(request):
    datos = {
        'form': AnimalFrom()
    }
    if request.method == 'POST':
        formulario = AnimalFrom(request.POST)
        datos['configuracion']= ""
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= f"Guardados Correctamente"
            datos['configuracion']= "alert alert-success"
        else:
            datos['mensaje']= f"error {formulario.is_valid()}"
            datos['configuracion']= "alert alert-danger"

    return render(request,'core/addanimal.html',datos)

def edit(request,id):
    masco = mascotas.objects.get(numero=id)

    datos = {
    'form': MascotaFrom(instance=masco)
    }
    if request.method == 'POST':
        formulario = MascotaFrom(data=request.POST, instance=masco)
        datos['configuracion']= ""
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= f"Modificado Correctamente"
            datos['configuracion']= "alert alert-success"
        else:
            datos['mensaje']= f"error {formulario.is_valid()}"
            datos['configuracion']= "alert alert-danger"

    return render(request,'core/form_mod_mascota.html',datos)

def mascota(request,id):

    mascota=mascotas.objects.get(numero=id)
    datos = {
        'mascota': mascota
    }
    return render(request,'core/masco.html',datos)

def eliminar(request,id):
    mascota=mascotas.objects.get(numero=id)
    mascota.delete()
    return redirect(to='home')