from django.db import models
from core.models import Administrador  # Importa o modelo Administrador, usado como chave estrangeira

# Modelo: RegistroAcesso

class RegistroAcesso(models.Model):
    # Usuário (administrador) responsável pela ação registrada
    usuario = models.ForeignKey(
        Administrador,
        on_delete=models.CASCADE,         # Se o administrador for excluído, seus registros também serão
        related_name='registros_acesso_core'  # Nome usado no acesso reverso: admin.registros_acesso_core.all()
    )
    # Data e hora em que a ação foi realizada, preenchida automaticamente
    data_hora = models.DateTimeField(auto_now_add=True)
    # Ação realizada (exemplo: "Login", "Cadastro de paciente", etc.)
    acao = models.TextField()
    # Descrição opcional com mais detalhes sobre a ação
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'registro_acesso_admin'  # Nome customizado da tabela no banco

    def __str__(self):
        # Representação legível do objeto no admin e shell
        return f"{self.usuario.nome} - {self.acao} em {self.data_hora}"

# Modelo: Suprimento

class Suprimento(models.Model):
    # Unidade de saúde associada ao suprimento
    unidade_saude = models.ForeignKey(
        'core.UnidadeSaude',
        on_delete=models.CASCADE  # Deleta suprimentos se a unidade for excluída
    )
    nome = models.CharField(max_length=255)       # Nome do suprimento (ex: "Seringa", "Luvas")
    quantidade = models.PositiveIntegerField()    # Quantidade (só permite valores positivos)
    tipo = models.CharField(max_length=50)        # Tipo (ex: "Medicamento", "Equipamento")
    validade = models.DateField()                 # Data de validade

    class Meta:
        db_table = 'suprimento'

    def __str__(self):
        return f"{self.nome} - {self.unidade_saude.nome}"



# Modelo: RelatorioFinanceiro

class RelatorioFinanceiro(models.Model):
    # Unidade de saúde a que o relatório pertence
    unidade_saude = models.ForeignKey(
        'core.UnidadeSaude',  
        on_delete=models.CASCADE,
        related_name='relatorios_financeiros'  # Acesso reverso: unidade.relatorios_financeiros.all()
    )
    descricao = models.TextField(blank=True, null=True)  # Descrição opcional do relatório
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor financeiro, exemplo: R$ 99999999.99
    data_registro = models.DateTimeField(auto_now_add=True)  # Data e hora do registro, preenchida automaticamente

    class Meta:
        db_table = 'relatorio_financeiro'

    def __str__(self):
        return f"R${self.valor} - {self.unidade_saude.nome} em {self.data_registro}"