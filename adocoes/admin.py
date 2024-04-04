from .models import *
from django.contrib import admin


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cargo", "email", "get_telefone"]
    search_fields = ["nome", "cargo", "email"]
    list_filter = ["cargo"]
    ordering = ["id"]


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nome",
        "especie",
        "idade",
        "sexo",
        "castrado",
        "raca",
        "historico_saude",
        "data_entrada",
    ]

    search_fields = ["nome", "especie", "raca"]
    list_filter = ["especie", "sexo", "data_entrada", "castrado"]
    ordering = ["id"]
    list_per_page = 15


@admin.register(Solicitante)
class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "get_cpf", "email", "telefone", "data_cadastro"]
    list_filter = ["nome", "data_cadastro"]
    search_fields = ["nome", "email"]
    ordering = ["id"]
    list_per_page = 15


@admin.register(Adocao)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "solicitante",
        "animal",
        "data_solicitacao",
        "status",
    ]
    list_filter = ["status", "data_solicitacao"]
    search_fields = ["solicitante.nome"]
    ordering = ["id"]
    list_per_page = 15
