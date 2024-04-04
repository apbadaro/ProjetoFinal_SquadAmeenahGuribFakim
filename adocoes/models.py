from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    ESPECIE = [
        ("C", "Cachorro"),
        ("G", "Gato"),
    ]
    especie = models.CharField(max_length=15, choices=ESPECIE, verbose_name="Espécie")
    SEXO = [
        ("M", "Macho"),
        ("F", "Fêmea"),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO)
    CASTRADO = [
        ("S", "Sim"),
        ("N", "Não"),
    ]
    castrado = models.CharField(
        max_length=1, choices=CASTRADO, verbose_name="Animal castrado?"
    )
    idade = models.CharField(null=True, max_length=30)
    raca = models.CharField(null=True, max_length=50, verbose_name="Raça")
    historico_saude = models.TextField(verbose_name="Histórico de Saúde")
    data_entrada = models.DateTimeField(
        null=True, db_column="Data de Entrada", verbose_name="Data de Entrada"
    )
    foto = models.ImageField(upload_to="animais/", blank=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"
        ordering = ["id"]

    def __str__(self):
        return f"{self.nome} - {self.especie} - {self.sexo}"


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.EmailField()
    _telefone = models.CharField(
        max_length=20, verbose_name="Telefone", db_column="Telefone"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ["id"]

    def get_telefone(self):
        return self._telefone

    def save(self, *args, **kwargs):
        super(Funcionario, self).save(*args, **kwargs)
        if not self.user:
            username = self.email
            self.user = User.objects.create_user(username=username)
            self.save()

    def __str__(self):
        return f"{self.user.username if self.user else 'Usuário não associado'} - Funcionário: {self.nome}, {self.cargo}"


class Solicitante(models.Model):
    nome = models.CharField(max_length=100)
    _cpf = models.CharField(max_length=14, verbose_name="CPF", db_column="CPF")
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Cadastro"
    )
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, default=None, blank=True, null=True
    # )

    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"
        ordering = ["id"]

    def get_cpf(self):
        return self._cpf

    def __str__(self):
        return f"{self.nome}"


class Adocao(models.Model):
    solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Solicitação"
    )
    status = models.CharField(
        max_length=20, choices=[("A", "Aprovada"), ("R", "Recusada"), ("P", "Pendente")]
    )

    def __str__(self):
        return f"{self.solicitante.nome} - {self.animal} - {self.status}"

    class Meta:
        verbose_name = "Adoção"
        verbose_name_plural = "Adoções"
        ordering = ["-data_solicitacao"]
