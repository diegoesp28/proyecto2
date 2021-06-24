from django.urls import path
from .views import *

urlpatterns =[ 
    path('home/', home, name='home'),
    path('inicio/',index, name='inicio'),
    path('nosotros/',nosotros, name='nosotros'),
    path('consulta',consulta, name='consulta'),
    path('contacto',contacto, name='contacto'),
    path('animales/', animal, name='animales'),
    path('formulario/', agregar, name='formulario'),
    path('modificar/<id>', edit, name='modificar'),
    path('masco/<id>', mascota, name='masco'),
]

