from django import forms
from django.db.models import fields

from .models import mascotas

class MascotaFrom(forms.ModelForm):
    
    class Meta:
        model = mascotas
        # fields = ('__all__')
        fields = ['numero', 
            'nombre',
            'edad', 
            'img_mascota',
            'id_tipo_animal'
        ]
        label= {
            'numero': 'Numero', 
            'nombre': 'Nombre',
            'edad': 'Edad', 
            'img_mascota': 'IMG mascota',
            'id_tipo_animal': 'tipo animal'
        }
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}), 
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}), 
            'img_mascota': forms.FileInput(attrs={'class': '' }),
            'id_tipo_animal' : forms.Select(attrs={'class': 'form-control'})
        }
