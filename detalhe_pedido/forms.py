# forms.py

from django import forms
from adocoes.models import Animal

class AdocaoForm(forms.Form):
    nome_completo = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14)
    telefone = forms.CharField(max_length=20)
    endereco = forms.CharField(max_length=255)