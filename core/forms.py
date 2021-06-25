from django import forms
from django.db.models import fields

from .models import mascotas, animal

class MascotaFrom(forms.ModelForm):
    
    class Meta:
        model = mascotas
        # fields = ('__all__')
        fields = ['numero', 
            'nombre',
            'edad', 
            'img_mascota',
            'id_tipo_animal',
            'id_genero'
            
        ]
        label= {
            'numero': 'Numero ', 
            'nombre': 'Nombre',
            'edad': 'Edad', 
            'img_mascota': 'IMG mascota',
            'id_tipo_animal': 'tipo animal',
            'id_genero':'Genero'
        }
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'col-5 form-control'}), 
            'nombre': forms.TextInput(attrs={'class': 'col-5 form-control'}),
            'edad': forms.TextInput(attrs={'class': 'col-5 form-control'}), 
            'img_mascota': forms.FileInput(attrs={'class': '' }),
            'id_tipo_animal' : forms.Select(attrs={'class': 'col-5 form-control'}),
            'id_genero': forms.Select(attrs={'class': 'col-5 form-control'})
        }

class AnimalFrom(forms.ModelForm):
     class Meta:
        model = animal
        fields = ('__all__')