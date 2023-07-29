from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from clases.models import Alumnos, Profesores, Consultas

# Create your views here.

def alumnos(request):
    contexto = {}
    alumnos_list = Alumnos.objects.all()
    return render(request, 'clases/alumnos.html', {'alumnos_list': alumnos_list})


def registro_alumno(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        if nombre and apellido and dni:
            alumno = Alumnos(nombre=nombre, apellido=apellido, dni=dni, email=email, telefono=telefono)
            alumno.save()
            return redirect('/alumnos/registro_completo')
        error_message = "Todos los campos son obligatorios."
        return render(request=request, template_name='clases/registro_alumno.html', context={'error_message': error_message})

    return render(request=request, template_name='clases/registro_alumno.html')


def cv_completo(request):  
    contexto = {}
    http_response = render(request=request, template_name='clases/cv_completo.html', context=contexto)
    return http_response

def profesor_cv(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        experiencia = request.POST.get('experiencia')
        if nombre and apellido and dni:
            alumno = Profesores(nombre=nombre, apellido=apellido, dni=dni, email=email, telefono=telefono)
            alumno.save()
            return redirect('/alumnos/cv_completo')
        error_message = "Todos los campos son obligatorios."
        return render(request=request, template_name='clases/profesor_cv.html', context={'error_message': error_message})

    return render(request=request, template_name='clases/profesor_cv.html')




def registro_completo(request):  
    contexto = {}
    http_response = render(request=request, template_name='clases/registro_completo.html', context=contexto)
    return http_response

def consultas_generales(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        consulta = request.POST.get('consulta') 

        if nombre and apellido and consulta and email:
            consultas_generales = Consultas(nombre=nombre, apellido=apellido, consulta=consulta, email=email, telefono=telefono)
            consultas_generales.save()
            return redirect('/alumnos/consultas_realizadas')
        error_message = "Todos los campos son obligatorios."
        return render(request=request, template_name='clases/consultas_generales.html', context={'error_message': error_message})

    return render(request=request, template_name='clases/consultas_generales.html')

def consultas_realizadas(request):  
    contexto = {}
    http_response = render(request=request, template_name='clases/consultas_realizadas.html', context=contexto)
    return http_response

def resultado_busqueda(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data.get("busqueda") 
        if busqueda:
            alumnos = Alumnos.objects.filter(Q(nombre__icontains=busqueda) | Q(apellido__icontains=busqueda))
            context = {"resultados": alumnos}
            return render(request, template_name='clases/resultados_busqueda.html', context=context)
    context = {"resultados": []} 
    return render(request, template_name='clases/resultados_busqueda.html', context=context)
