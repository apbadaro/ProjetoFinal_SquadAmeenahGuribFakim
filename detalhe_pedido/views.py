from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from adocoes.models import Animal
from .forms import AdocaoForm
from adocoes.models import Solicitante  # Importa a classe Solicitante do app "adocoes"
# from adocoes.forms import SolicitanteForm
from .forms import SolicitanteForm

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

# apagar teste
def teste_disponiveis(request):
    return render(request, '0_lista_pets.html')

# =========================================================================
# rever:

def solicitar_adocao(request):
    if request.method == 'POST':
        form = SolicitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_sucesso')  # redirecionar para a página de sucesso
    else:
        form = SolicitanteForm()
    return render(request, 'solicitante_form.html', {'form': form})
