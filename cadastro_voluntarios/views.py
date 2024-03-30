from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def cadastro_voluntario(request):
    return render(request, 'cadastro_voluntario.html')