from .forms import AdocaoForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404

@login_required  # Garante que apenas usuários autenticados tenham acesso
def adocoes(request):
    try:
        # Puxa todas as instâncias de Adoção e Animal do BD
        adocoes = Adocao.objects.all()
        animais = Animal.objects.all()
    except Exception as e:
        return HttpResponseServerError(
            f"Ocorreu um erro ao listar as adoções: {str(e)}"
        )

    # Página de listagem de todas as adoções
    return render(request, "adocoes.html", {"adocoes": adocoes, "animais": animais})


@login_required
def adocao_detalhes(request, pk):
    try:
        # Puxa os detalhes de uma adoção específica com base na chave primária (pk)
        adocao = get_object_or_404(Adocao, pk=pk)
    except Adocao.DoesNotExist:
        raise Http404("Adoção não encontrada.")

    # Página dos detalhes de uma adoção específica
    return render(request, "detalhes.html", {"adocao": adocao})


@login_required
def adocao_criar(request):
    if request.method == "POST":
        try:
            form = AdocaoForm(request.POST)
            if form.is_valid():
                adocao = form.save(commit=False)
                solicitante = get_object_or_404(Solicitante, user=request.user)
                adocao.solicitante = solicitante
                adocao.save()
                return redirect("adocoes")
        except Exception as e:
            return HttpResponseServerError(
                f"Ocorreu um erro ao criar a adoção: {str(e)}"
            )
    else:
        form = AdocaoForm()

    return render(request, "form.html", {"form": form})


@login_required
def adocao_atualizar(request, pk):
    adocao = get_object_or_404(Adocao, pk=pk)
    if request.method == "POST":
        form = AdocaoForm(request.POST, instance=adocao)
        try:
            if form.is_valid():
                adocao = form.save(commit=False)
                adocao.save()
                return redirect("adocao_detalhes", pk=adocao.pk)
        except Exception as e:
            return HttpResponseServerError(
                f"Ocorreu um erro ao atualizar a adoção: {str(e)}"
            )
    else:
        form = AdocaoForm(instance=adocao)

    return render(request, "form.html", {"form": form})


@login_required
def adocao_excluir(request, pk):
    try:
        adocao = get_object_or_404(Adocao, pk=pk)
        if request.method == "POST":
            adocao.delete()
            return redirect("adocoes")
        else:
            return render(request, "excluir_confirm.html", {"adocao": adocao})

    except Exception as e:
        return HttpResponseServerError(f"Ocorreu um erro ao excluir a adoção: {str(e)}")

# ============================

# Para Front:
def home_inicio(request):
    return render(request, 'index.html')
