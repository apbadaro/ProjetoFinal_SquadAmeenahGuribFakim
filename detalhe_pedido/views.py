from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from adocoes.models import Animal
from .forms import AdocaoForm

# Create your views here.

def detalhe_pedido(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    form = AdocaoForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        # Lógica para processar o formulário de adoção e enviar para o admin
        # Exemplo: salvar os dados do formulário no banco de dados ou enviar um e-mail
        # Após processar, redirecione para uma página de sucesso
        return render(request, 'sucesso.html')

    return render(request, '1_detalhes_pet.html', {'animal': animal, 'form': form})

def sucesso(request):
    return render(request, 'aguarde_retorno.html')


def sucesso(request):
    return render(request, 'aguarde_retorno.html')

def teste_disponiveis(request):
    return render(request, '0_lista_pets.html')
