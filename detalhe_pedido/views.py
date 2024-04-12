from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from adocoes.models import Animal
from .forms import AdocaoForm
from adocoes.models import Solicitante
from .forms import SolicitanteForm
# from .forms import SolicitacaoAdocaoForm
# from detalhe_pedido.views import SolicitacaoAdocaoForm
from django.urls import reverse

# Create your views here.

def detalhe_pedido(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    form = AdocaoForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        # Após processar, redirecione para uma página de sucesso
        return render(request, 'aguarde_retorno.html')

    return render(request, 'detalhes_pet_pedido_adocao.html', {'animal': animal, 'form': form})

def sucesso(request):
    return render(request, 'aguarde_retorno.html')

# Páginas em Construção:
def doar(request):
    return render(request, 'doacao.html')

def cuidador(request):
    return render(request, 'cuidador.html')

def voluntario(request):
    return render(request, 'voluntario.html')

def sobre(request):
    return render(request, 'sobre.html')

def agenda(request):
    return render(request, 'agenda.html')

# =======================================================================
# Teste ok
# SOLICITAÇÃO DE ADOÇÃO:
def cadastrar_solicitante(request, animal_id):
    animal_id = request.resolver_match.kwargs['animal_id']
    if request.method == 'POST':
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            solicitante = form.save(commit=False)
            solicitante.animal_id = animal_id  # Usando o animal_id fornecido na URL
            solicitante.animal_nome = Animal.objects.get(id=animal_id).nome  # Definindo o nome do animal
            solicitante.save()
            return redirect('pagina_sucesso')
    else:
        form = SolicitanteForm(initial={'animal_id': animal_id})
    
    return render(request, 'detalhes_pet_pedido_adocao.html', {'form': form})



# =======================================================================
# Teste 2
# SOLICITAÇÃO DE ADOÇÃO:

def detalhes_pet_pedido_adocao(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    
    if request.method == 'POST':
        form = Solicitante(request.POST)
        if form.is_valid():
            solicitante = form.save(commit=False)
            solicitante.animal_id = animal_id  # Usando o animal_id fornecido na URL
            solicitante.animal_nome = animal.nome  # Definindo o nome do animal
            solicitante.save()
            form.save()
            return redirect('pagina_sucesso')
    else:
        form = Solicitante(initial={'animal_id': animal_id})
    
    return render(request, 'detalhes_pet_pedido_adocao.html', {'animal': animal, 'form': form})

# Teste ok
# SOLICITAÇÃO DE ADOÇÃO:
def pagina_sucesso(request):
    return render(request, 'aguarde_retorno.html')