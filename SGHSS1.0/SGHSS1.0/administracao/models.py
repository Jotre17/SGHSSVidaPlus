from django.db import models
from core.models import Administrador

class RegistroAcesso(models.Model):
    usuario = models.ForeignKey(
        Administrador,
        on_delete=models.CASCADE,
        related_name='registros_acesso_core'
    )
    data_hora = models.DateTimeField()
    acao = models.TextField()
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'registro_acesso_admin'

    def __str__(self):
        return f"{self.usuario.nome} - {self.acao} em {self.data_hora}"


class Suprimento(models.Model):
    unidade_saude = models.ForeignKey(
        'core.UnidadeSaude',
        on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=50)
    validade = models.DateField()

    class Meta:
        db_table = 'suprimento'

    def __str__(self):
        return f"{self.nome} - {self.unidade_saude.nome}"


class RelatorioFinanceiro(models.Model):
    unidade_saude = models.ForeignKey(
        'core.UnidadeSaude',  
        on_delete=models.CASCADE,
        related_name='relatorios_financeiros'
    )
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_registro = models.DateTimeField()

    class Meta:
        db_table = 'relatorio_financeiro'

    def __str__(self):
        return f"R${self.valor} - {self.unidade_saude.nome} em {self.data_registro}"
