# Importa o módulo base de modelos do Django e o modelo de usuário padrão
from django.db import models
from django.contrib.auth.models import User

# MODELO: UnidadeSaude

class UnidadeSaude(models.Model):
    # Define as opções disponíveis para o tipo da unidade de saúde
    class TipoChoices(models.TextChoices):
        CLINICA = 'Clínica', 'Clínica'
        HOSPITAL = 'Hospital', 'Hospital'
        HOME_CARE = 'Home Care', 'Home Care'
        LABORATORIO = 'Laboratório', 'Laboratório'

    # Campos principais da unidade de saúde
    nome = models.CharField(max_length=100)  # Nome da unidade
    tipo = models.CharField(max_length=20, choices=TipoChoices.choices)  # Tipo (escolhido do enum)
    cidade = models.CharField(max_length=255, default='Cidade - EE')  # Cidade (com valor padrão para exibição)
    cep = models.CharField(max_length=10, default='XX.XXX-XXX')  # CEP com formato customizado padrão
    endereco = models.CharField(max_length=255)  # Endereço completo
    telefone = models.CharField(max_length=15, default='(XX) XXXXX-XXXX')  # Telefone padrão mascarado

    class Meta:
        db_table = 'unidade_saude'  # Define o nome da tabela no banco de dados

    def __str__(self):
        return self.nome  # Retorno representativo para exibição no admin e logs



# MODELO: Administrador

class Administrador(models.Model):
    # Define os níveis de permissão que um administrador pode ter
    class PermissaoChoices(models.TextChoices):
        TOTAL = 'Total', 'Total'      # Acesso total ao sistema
        PARCIAL = 'Parcial', 'Parcial'  # Acesso limitado (ex: sem prontuários ou relatórios)

    # Relacionamento 1:1 com o User do Django (para login/autenticação)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='administrador',
        verbose_name='Usuário do Django'
    )

    # Informações pessoais do administrador
    nome = models.CharField(max_length=200, verbose_name='Nome completo')
    email = models.EmailField(max_length=200, verbose_name='E-mail')
    telefone = models.CharField(max_length=15, default='(XX) XXXXX-XXXX')

    # Permissão de acesso (Total ou Parcial)
    permissao = models.CharField(max_length=10,choices=PermissaoChoices.choices,default=PermissaoChoices.PARCIAL,verbose_name='Permissão')

    class Meta:
        db_table = 'administrador'  # Nome da tabela no banco
        verbose_name = 'Administrador'  # Nome legível singular
        verbose_name_plural = 'Administradores'  # Nome legível plural

    def __str__(self):
        return f"{self.nome} ({self.permissao})"  # Representação legível no admin e logs



# MODELO: RegistroAcesso

class RegistroAcesso(models.Model):
    # Relacionamento com o administrador que realizou a ação
    usuario = models.ForeignKey(Administrador,on_delete=models.CASCADE,related_name='registros_acesso')

    # Data e hora do registro (preenchida automaticamente na criação)
    data_hora = models.DateTimeField(auto_now_add=True)

    # Ação executada (ex: login, alteração, exclusão)
    acao = models.TextField()

    # Descrição opcional adicional (detalhes, contexto, etc.)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'registro_acesso'  # Nome da tabela no banco

    def __str__(self):
        # Exibição resumida: nome do usuário e ação realizada
        return f"{self.usuario.nome} - {self.acao} em {self.data_hora}"
