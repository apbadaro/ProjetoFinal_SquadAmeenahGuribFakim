# forms.py
from django import forms
from adocoes.models import Animal
from adocoes.models import Solicitante

class AdocaoForm(forms.Form):
    nome_completo = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14)
    telefone = forms.CharField(max_length=20)
    animal_id = forms.CharField(widget=forms.HiddenInput())
    # endereco = forms.CharField(max_length=255)

# SOLICITAÇÃO DE ADOÇÃO:
class SolicitanteForm(forms.ModelForm):
    animal_id = forms.CharField(required=False)
    animal_nome = forms.CharField(widget=forms.HiddenInput())  

    def clean_animal_id(self):
        animal_id = self.cleaned_data.get('animal_id')
        if not animal_id:
            raise forms.ValidationError("O campo ID do animal é obrigatório.")
        return animal_id

    class Meta:
        model = Solicitante
        # fields = '__all__'
        fields = ['nome', '_cpf', 'email', 'telefone', 'animal_id', 'animal_nome']

# Banco de Dados:
# python manage.py makemigrations
# python manage.py migrate