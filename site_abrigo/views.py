from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Animal
from .forms import AdocaoForm

# Create your views here.

# Página Principal do Site:
def site(request):
    return render(request, 'index.html')

# página formulario de detalhes do pet e de quero adotar:
def detalheAdotar(request):
    return render(request, 'base_form_detalhe_adocao.html')

# Página Detalhes Pet e Quero Adotar: Versão 2
def detalhes_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            # Processar o formulário de adoção
            # Por exemplo, enviar um e-mail para a parte de administração do Django
            # return redirect('sucesso')
            return render(request, 'aguarde_retorno.html')
    else:
        form = AdocaoForm()
    return render(request, 'detalhes_animal.html', {'animal': animal, 'form': form})

def sucesso(request):
    return render(request, 'aguarde_retorno.html')

def cadastro_pet(request):
    pass


# ============================


'''
# views.py

from django.shortcuts import render, redirect
from .models import Animal
from .forms import AdocaoForm

def detalhes_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            # Processar o formulário de adoção
            # Por exemplo, enviar um e-mail para a parte de administração do Django
            # Após o processamento bem-sucedido, renderizar a página de "Aguarde retorno"
            return render(request, 'aguarde_retorno.html')
    else:
        form = AdocaoForm()
    return render(request, 'detalhes_animal.html', {'animal': animal, 'form': form})

def sucesso(request):
    return render(request, 'aguarde_retorno.html')

'''



'''
# views.py

from django.shortcuts import render, redirect
from .models import Animal
from .forms import AdocaoForm

def detalhes_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            # Processar o formulário de adoção
            # Por exemplo, enviar um e-mail para a parte de administração do Django
            return redirect('sucesso')
    else:
        form = AdocaoForm()
    return render(request, 'detalhes_animal.html', {'animal': animal, 'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')


'''