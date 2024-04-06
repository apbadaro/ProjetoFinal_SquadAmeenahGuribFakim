from django.shortcuts import render
from django.http import HttpResponse
from adocoes.models import Animal
# Create your views here.

def inicio(request):
    bichinho = Animal.objects.all()
    contexto = contexto = {'bichinho': bichinho,}
    return render(request, 'inicio.html', contexto)