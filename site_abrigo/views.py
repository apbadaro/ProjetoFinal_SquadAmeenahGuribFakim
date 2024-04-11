from django.shortcuts import render, redirect
from django.http import HttpResponse
from adocoes.models import Animal

# Create your views here.


# Página Principal do Site:
def site(request):
    return render(request, "index.html")


def animais_disponiveis(request):
    query = request.GET.get("q")
    if query:
        if query.lower() == "gato":
            bichinho = Animal.objects.filter(especie__iexact="G")
        elif query.lower() == "cachorro":
            bichinho = Animal.objects.filter(especie__iexact="C")
        else:
            bichinho = Animal.objects.filter(
                nome__icontains=query
            ) | Animal.objects.filter(raca__icontains=query)
    else:
        bichinho = Animal.objects.all()
    contexto = {"bichinho": bichinho}
    return render(request, "animais_disponiveis.html", contexto)
