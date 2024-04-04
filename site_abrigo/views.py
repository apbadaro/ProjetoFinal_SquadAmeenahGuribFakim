from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Página Principal do Site:
def site(request):
    return render(request, 'index.html')

def cadastro_pet(request):
    pass


# ============================

