from django.contrib import admin

# Register your models here.

from clases.models import Alumnos, Profesores, Consultas

admin.site.register(Alumnos)
admin.site.register(Profesores)
admin.site.register(Consultas)