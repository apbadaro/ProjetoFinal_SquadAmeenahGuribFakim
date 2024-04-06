
from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    idade = models.IntegerField()
    
    # Este trecho de código representa os animais no abrigo. 
    # Ele tem quatro campos: nome, especie, raca e idade.