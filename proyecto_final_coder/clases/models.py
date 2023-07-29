from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}, {self.telefono}"
    
    
class Profesores(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    experiencia = models.CharField(max_length=32)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.telefono}"

class Consultas(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    consulta = models.CharField(max_length=400)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.telefono}"

    

