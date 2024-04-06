from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path
from adocoes.views import home_inicio

urlpatterns = [
    path("", login_required(views.adocoes), name="adocoes"),
    path("adocao/criar/", login_required(views.adocao_criar), name="adocao_criar"),
    path(
        "adocao/detalhes/<int:pk>/",
        login_required(views.adocao_detalhes),
        name="adocao_detalhes",
    ),
    path(
        "adocao/atualizar/<int:pk>/",
        login_required(views.adocao_atualizar),
        name="adocao_atualizar",
    ),
    path(
        "adocao/excluir/<int:pk>/",
        login_required(views.adocao_excluir),
        name="adocao_excluir",
    ),