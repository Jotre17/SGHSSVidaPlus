from django.db import models
# Importa o modelo padrão de usuários do Django
from django.contrib.auth.models import User  

class Profissional(models.Model):
    # Relaciona o profissional a um usuário do Django (login/autenticação)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_profissional')

    # Relacionamento com uma unidade de saúde (vários profissionais para uma unidade)
    unidade_saude = models.ForeignKey('core.UnidadeSaude', on_delete=models.CASCADE, related_name='profissionais')

    # Dados pessoais e profissionais
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, default='(XX) XXXXX-XXXX')
    email = models.EmailField(max_length=100)
    crm_coren = models.CharField(max_length=20, default='CRM-COREN/EE 00000000')

    class Meta:
        db_table = 'profissional'  # Nome da tabela no banco de dados

    def __str__(self):
        return f"{self.nome}, ({self.especialidade})"  # Exibição no admin e interfaces de log


from django.db import models

class Leito(models.Model):
    # Tipos disponíveis de leitos
    class TipoLeitoChoices(models.TextChoices):
        ENFERMARIA = 'Enfermaria', 'Enfermaria'
        UTI = 'UTI', 'UTI'
        ISOLAMENTO = 'Isolamento', 'Isolamento'

    # Situações possíveis para o leito
    class StatusChoices(models.TextChoices):
        DISPONIVEL = 'Disponível', 'Disponível'
        OCUPADO = 'Ocupado', 'Ocupado'
        MANUTENCAO = 'Manutenção', 'Manutenção'

    # Campos do modelo
    tipo_leito = models.CharField(max_length=20,choices=TipoLeitoChoices.choices,default=TipoLeitoChoices.ENFERMARIA)

    status = models.CharField(max_length=20,choices=StatusChoices.choices,default=StatusChoices.DISPONIVEL)

    unidade_saude = models.ForeignKey('core.UnidadeSaude',on_delete=models.CASCADE,related_name='leitos')

    paciente = models.ForeignKey('pacientes.Paciente',on_delete=models.SET_NULL,null=True,blank=True,related_name='leitos')

    def __str__(self):
        return f"Leito {self.id} - {self.tipo_leito} - {self.status}"


class Internacao(models.Model):
    # Relacionamentos com paciente, profissional e leito
    paciente = models.ForeignKey('pacientes.Paciente',on_delete=models.CASCADE,related_name='internacoes')
    profissional = models.ForeignKey('profissionais.Profissional',on_delete=models.CASCADE,related_name='internacoes')
    leito = models.ForeignKey('profissionais.Leito',on_delete=models.CASCADE,related_name='internacoes')

    # Informações da internação
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField(blank=True, null=True)  
    diagnostico = models.TextField()

    class Meta:
        db_table = 'internacao'  # Nome da tabela

    def __str__(self):
        return f"Internação de {self.paciente.nome} no leito {self.leito.id}"  # Exibição no admin e interfaces de log
