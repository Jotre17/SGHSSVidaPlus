from django.db import models
from django.contrib.auth.models import User

class Profissional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_profissional')
    unidade_saude = models.ForeignKey('core.UnidadeSaude',on_delete=models.CASCADE,related_name='profissionais')
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, default= '(XX) XXXXX-XXXX')
    email = models.EmailField(max_length=100)
    crm_coren = models.CharField(max_length=20, default= 'CRM-COREN/EE 00000000' )

    class Meta:
        db_table = 'profissional'

    def __str__(self):
        return f"{self.nome}, ({self.especialidade})"


class Leito(models.Model):
    class TipoLeitoChoices(models.TextChoices):
        ENFERMARIA = 'Enfermaria', 'Enfermaria'
        UTI = 'UTI', 'UTI'
        ISOLAMENTO = 'Isolamento', 'Isolamento'

    class StatusChoices(models.TextChoices):
        DISPONIVEL = 'Disponível', 'Disponível'
        OCUPADO = 'Ocupado', 'Ocupado'
        MANUTENCAO = 'Manutenção', 'Manutenção'

    unidade_saude = models.ForeignKey(
        'core.UnidadeSaude',
        on_delete=models.CASCADE,
        related_name='leitos'
    )
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        related_name='leitos'
    )
    paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.CASCADE)
    tipoLeito = models.CharField(max_length=20, choices=TipoLeitoChoices.choices)
    status = models.CharField(max_length=20, choices=StatusChoices.choices)

    class Meta:
        db_table = 'leito'

    def __str__(self):
        return f"Leito {self.id} - {self.tipoLeito} ({self.status})"


class Internacao(models.Model):
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='internacoes'
    )
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        related_name='internacoes'
    )
    leito = models.ForeignKey(
        'profissionais.Leito',
        on_delete=models.CASCADE,
        related_name='internacoes'
    )
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField(blank=True, null=True)
    diagnostico = models.TextField()

    class Meta:
        db_table = 'internacao'

    def __str__(self):
        return f"Internação de {self.paciente.nome} no leito {self.leito.id}"