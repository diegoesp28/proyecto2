from django.urls import path
from .views import *

urlpatterns =[ 
    path('home/', home, name='home'),
    path('inicio/',index, name='inicio'),
    path('nosotros/',nosotros, name='nosotros'),
    path('consulta',consulta, name='consulta'),
    path('contacto',contacto, name='contacto'),
    path('administrador',administrador, name='administrador'),
    
]

