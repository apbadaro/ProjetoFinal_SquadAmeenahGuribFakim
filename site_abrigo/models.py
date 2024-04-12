from django.db import models

# Create your models here

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    idade = models.IntegerField()
    castrado = models.BooleanField(default=False)
    data_entrada = models.DateTimeField(
        null=True, db_column="Data de Entrada", verbose_name="Data de Entrada"
    )
    # especie ou porte?
    historico_saude = models.TextField()
    pelagem = models.CharField(max_length=10, choices=[('curto', 'Curto'), ('medio', 'Medio'), ('longo', 'Longo')])
    foto = models.ImageField(upload_to='pets', blank=True, null=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"