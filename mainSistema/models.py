from tabnanny import verbose
from django.db import models

# Create your models here.

class Visitante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    documento = models.CharField(max_length=100, verbose_name="Documento")
    permiso = models.CharField(max_length=100, verbose_name="Permiso")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    organizacion = models.CharField(max_length=100, verbose_name="Organizacion")
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    imagen = models.ImageField(upload_to='imagenes/', null=True,verbose_name="Imagen")
    
    