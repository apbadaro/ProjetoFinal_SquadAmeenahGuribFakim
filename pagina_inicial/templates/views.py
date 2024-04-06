from django.shortcuts import render
from .models import Animal

def search_animals(request):
    query = request.GET.get('q')

    if query:
        animals = Animal.objects.filter(nome__icontains=query) | \
                  Animal.objects.filter(especie__icontains=query) | \
                  Animal.objects.filter(raca__icontains=query)
                  # Pode adicionar mais filtros se for necessário
    else:
        animals = Animal.objects.all()

    return render(request, 'search_results.html', {'animals': animals})

# Esse trecho do cógigo verifica se há parâmetros de consulta na URL (usando request.GET.get('q')) 
# e, se houver, realiza uma pesquisa no banco de dados usando os campos nome,especie e raca