from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Animal

# Create your views here.

# Página Principal do Site:
def site(request):
    return render(request, 'index.html')

def animais_disponiveis(request):
   # bichinho = Animal.objects.all()
    bichinho = Animal.objects.all()
    contexto = contexto = {'bichinho': bichinho,}
    return render(request, 'animais_disponiveis.html', contexto )
