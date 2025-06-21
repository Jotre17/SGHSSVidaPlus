from django.db import models
from django.contrib.auth.models import User

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

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='administrador',verbose_name='Usuário do Django')
    nome = models.CharField(max_length=200, verbose_name='Nome completo')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    permissao = models.CharField(max_length=10,choices=PermissaoChoices.choices,default=PermissaoChoices.PARCIAL,verbose_name='Permissão')

    class Meta:
        db_table = 'administrador'
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

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
