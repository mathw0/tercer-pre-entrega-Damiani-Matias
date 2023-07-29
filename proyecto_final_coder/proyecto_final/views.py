from django.http import HttpResponse
from django.shortcuts import render

def  inicio(request):
    http_response = render(request=request, template_name='inicio.html', context={},)
    return http_response