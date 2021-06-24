from core.models import mascotas
from django.shortcuts import render


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
def administrador(request):
    return render(request,'core/administrador.html')
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


