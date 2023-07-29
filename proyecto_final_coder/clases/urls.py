from django.contrib import admin
from django.urls import path
from clases.views import (alumnos, registro_alumno, registro_completo, profesor_cv, cv_completo, consultas_generales, consultas_realizadas, resultado_busqueda)

urlpatterns = [
    path('alumnos', alumnos),
    path('registro_alumno', registro_alumno),
    path('registro_completo', registro_completo),
    path('profesor_cv', profesor_cv),
    path('cv_completo', cv_completo),
    path('consultas_generales', consultas_generales),
    path('consultas_realizadas', consultas_realizadas),
    path('resultado_busqueda', resultado_busqueda, name='resultado_busqueda'),
]