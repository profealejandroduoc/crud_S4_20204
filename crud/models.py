from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .tipos import *
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    rut=models.CharField(max_length=10, null=False)
    direccion=models.CharField(max_length=500, null=False)

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10, primary_key=True)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    f_nacto=models.DateField()
    email=models.EmailField(max_length=100, null=False)
    imagen=models.ImageField(upload_to='personas', null=True)
    
    def __str__(self):
        return f"{self.rut} - {self.nombre} {self.apellido}"
    
class Mascota(models.Model):
    nombre=models.CharField(max_length=25)
    edad=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(250)])
    tipo=models.CharField(max_length=20, choices=TIPO_MASCOTA)
    subtipo=models.CharField(max_length=15,choices=SUBTIPO_MASCOTA, default='OTRO')
    propietario=models.ForeignKey(Persona,on_delete=models.PROTECT,default='100')
    
    def __str__(self):
        return self.nombre + "-" + self.tipo