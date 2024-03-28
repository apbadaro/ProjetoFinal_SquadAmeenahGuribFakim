from django.db import models


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
    idade = models.IntegerField(null=True)
    raca = models.CharField(max_length=50, verbose_name="Raça")
    historico_saude = models.TextField(verbose_name="Histórico de Saúde")
    data_entrada = models.DateTimeField(
        null=True, db_column="Data de Entrada", verbose_name="Data de Entrada"
    )
    foto = models.ImageField(upload_to="animais/", blank=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

    def __str__(self):
        return f"{self.nome} - {self.especie} - {self.sexo}"


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.EmailField()
    _telefone = models.CharField(
        max_length=20, verbose_name="Telefone", db_column="Telefone"
    )

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def get_telefone(self):
        return self._telefone

    def __str__(self):
        return f"Funcionário: {self.nome}, {self.cargo}"


class Solicitante(models.Model):
    nome = models.CharField(max_length=100)
    _cpf = models.IntegerField(verbose_name="CPF", db_column="CPF")
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Cadastro"
    )

    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"

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
        return f"{self.solicitante.nome} - {self.animal.nome} - {self.status}"

    class Meta:
        verbose_name = "Adoção"
        verbose_name_plural = "Adoções"
        ordering = ["-data_solicitacao"]
