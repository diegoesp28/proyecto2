from django.contrib import admin
from .models import animal, mascotas

# Register your models here.
#permite administrar el modelo completo


admin.site.register(animal)
admin.site.register(mascotas)
