from django.db import models

class Consulta(models.Model):
    class TipoChoices(models.TextChoices):
        ONLINE = 'Online', 'Online'
        PRESENCIAL = 'Presencial', 'Presencial'

    class StatusChoices(models.TextChoices):
        AGENDADA = 'Agendada', 'Agendada'
        REALIZADA = 'Realizada', 'Realizada'
        CANCELADA = 'Cancelada', 'Cancelada'

    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=20, choices=TipoChoices.choices)
    status = models.CharField(max_length=20, choices=StatusChoices.choices)

    class Meta:
        db_table = 'consulta'

    def __str__(self):
        return f"Consulta {self.data_hora} - {self.status}"


class Prontuario(models.Model):
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='prontuarios_consulta'
    )
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        related_name='prontuarios_consulta'
    )
    data_registro = models.DateTimeField()
    descricao = models.TextField()

    class Meta:
        db_table = 'prontuario'

    def __str__(self):
        return f"Prontuário de {self.paciente.nome} em {self.data_registro}"


class Prescricao(models.Model):
    prontuario = models.ForeignKey(
        Prontuario,
        on_delete=models.CASCADE,
        related_name='prescricoes'
    )
    medicamento = models.CharField(max_length=255)
    dosagem = models.CharField(max_length=50)
    instrucoes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'prescricao'

    def __str__(self):
        return f"{self.medicamento} para {self.prontuario.paciente.nome}"
class Agendamento(models.Model):
    class StatusChoices(models.TextChoices):
        AGENDADO = 'Agendado', 'Agendado'
        CANCELADO = 'Cancelado', 'Cancelado'
        CONCLUIDO = 'Concluído', 'Concluído'

    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    unidade_saude = models.ForeignKey(
        'core.UnidadeSaude',
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    especialidade = models.CharField(max_length=100)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=StatusChoices.choices)

    class Meta:
        db_table = 'agendamento'

    def __str__(self):
        return f"Agendamento de {self.paciente.nome} com {self.profissional.nome} em {self.data_hora}"