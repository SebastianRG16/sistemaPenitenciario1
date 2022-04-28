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
    
class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=100, verbose_name="Identificacion")
    hora = models.TimeField(verbose_name="Hora")
    numero_permiso = models.CharField(max_length=100, verbose_name="Numero de permiso")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    idVisitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)

class Niveles_seguridad(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_acceso = models.CharField(max_length=100, verbose_name="Tipo de acceso")

class Dispositivos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    dirrecion_ip = models.CharField(max_length=100, verbose_name="Direccion IP")
    dirrecion_mac = models.CharField(max_length=100, verbose_name="Direccion MAC")
    identificador = models.CharField(max_length=100, verbose_name="Identificador")
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicacion")

class Permiso(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de fin")
    objetos = models.CharField(max_length=100, verbose_name="Objetos")
    idVisitante_permi = models.ForeignKey(Visitante, on_delete=models.CASCADE, related_name="visitante_permiso", null=True)
    idNiveles_seguridad = models.ForeignKey(Niveles_seguridad, on_delete=models.CASCADE) 

class Punto_control(models.Model):
    id = models.AutoField(primary_key=True)

class Punto_control_permiso(models.Model):
    idPunto_control = models.ForeignKey(Punto_control, on_delete=models.CASCADE)
    idPermiso = models.ForeignKey(Permiso, on_delete=models.CASCADE,null=True)

class Punto_control_Dispositivos(models.Model):
    idPunto_control_dispo = models.ForeignKey(Punto_control, on_delete=models.CASCADE)
    idDispositivos = models.ForeignKey(Dispositivos, on_delete=models.CASCADE)