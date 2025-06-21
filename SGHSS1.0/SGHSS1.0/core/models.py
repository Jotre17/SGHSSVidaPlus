from django.db import models

class UnidadeSaude(models.Model):
    class TipoChoices(models.TextChoices):
        CLINICA = 'Clínica', 'Clínica'
        HOSPITAL = 'Hospital', 'Hospital'
        HOME_CARE = 'Home Care', 'Home Care'
        LABORATORIO = 'Laboratório', 'Laboratório'

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TipoChoices.choices)
    cidade = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)

    class Meta:
        db_table = 'unidade_saude'

    def __str__(self):
        return self.nome


class Administrador(models.Model):
    class PermissaoChoices(models.TextChoices):
        TOTAL = 'Total', 'Total'
        PARCIAL = 'Parcial', 'Parcial'

    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    permissao = models.CharField(max_length=10, choices=PermissaoChoices.choices)

    class Meta:
        db_table = 'administrador'

    def __str__(self):
        return f"{self.nome} ({self.permissao})"


class RegistroAcesso(models.Model):
    usuario = models.ForeignKey(
        Administrador,
        on_delete=models.CASCADE,
        related_name='registros_acesso'
    )
    data_hora = models.DateTimeField()
    acao = models.TextField()
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'registro_acesso'

    def __str__(self):
        return f"{self.usuario.nome} - {self.acao} em {self.data_hora}"
