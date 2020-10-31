from django.db import models

# Create your models here.


# creacion tablas para slider y misionyvision
class Slider1(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    imagen = models.ImageField(upload_to='autos',null=True)

    def __str__(self):
        return self.ident

# Crear tabla de insumos.
class Insumos(models.Model):
    nombre = models.CharField(max_length=120,primary_key=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

# Crear tabla de misionyvision.
class MisionyVision(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()
    valores = models.TextField(null=False,default=1)

    def __str__(self):
        return self.ident

# Crear tabla de galeria.
class Galeria(models.Model):
    ident = models.CharField(max_length=15,primary_key=True)
    imagengaleria = models.ImageField(upload_to='galeria',null=True)

    def __str__(self):
        return self.ident

