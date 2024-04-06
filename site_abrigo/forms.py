# forms.py

from django import forms
from .models import Animal

class AdocaoForm(forms.Form):
    nome_completo = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14)
    telefone = forms.CharField(max_length=15)
    endereco = forms.CharField(widget=forms.Textarea)

    

'''
from cadastro.models import Cadastro
class CadastroForm(forms.Form):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
'''