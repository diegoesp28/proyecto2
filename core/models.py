from django.db import models

# Create your models here.

#modelo para categoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

#modelo para el vehiculo

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca vehiculo')
    modelo = models.CharField(max_length=20, null=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patente

#datos animales
class animal(models.Model):
    id_animal = models.IntegerField(primary_key=True, verbose_name='Id animal')
    tipo_animal= models.CharField(max_length=50, verbose_name='tipo de animal')

    def __str__(self):
        return self.tipo_animal

class mascotas(models.Model):
    numero = models.CharField(max_length=6, primary_key=True, verbose_name='numero de chip')
    nombre = models.CharField(max_length=20, verbose_name='nombre mascota')
    edad = models.CharField(max_length=20, null=True, verbose_name='edad nacimiento')
    img_mascota = models.ImageField(upload_to='mascota',null=True)
    id_tipo_animal = models.ForeignKey(animal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
