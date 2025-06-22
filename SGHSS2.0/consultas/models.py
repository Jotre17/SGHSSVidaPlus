from django.db import models

# Modelo que representa uma Consulta médica
class Consulta(models.Model):
    # Enum para os tipos de consulta disponíveis
    class TipoChoices(models.TextChoices):
        ONLINE = 'Online', 'Online'        # Consulta online
        PRESENCIAL = 'Presencial', 'Presencial'  # Consulta presencial

    # Enum para os status possíveis da consulta
    class StatusChoices(models.TextChoices):
        AGENDADA = 'Agendada', 'Agendada'  # Consulta agendada
        REALIZADA = 'Realizada', 'Realizada' # Consulta realizada
        CANCELADA = 'Cancelada', 'Cancelada' # Consulta cancelada

    # Relação com o paciente (chave estrangeira)
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='consultas'
    )

    # Relação com o profissional responsável pela consulta
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        related_name='consultas'
    )

    # Data e hora da consulta
    data_hora = models.DateTimeField()

    # Tipo da consulta, deve ser uma das opções do TipoChoices
    tipo = models.CharField(max_length=20, choices=TipoChoices.choices)

    # Status atual da consulta, deve ser uma das opções do StatusChoices
    status = models.CharField(max_length=20, choices=StatusChoices.choices)

    class Meta:
        db_table = 'consulta'  # Nome da tabela no banco de dados

    def __str__(self):
        # Representação em string da consulta para facilitar exibição
        return f"Consulta {self.data_hora} - {self.status}"

    def get_meet_link(self):
        """
        Retorna um link do Google Meet simulado se a consulta for online.
        """
        if self.tipo == self.TipoChoices.ONLINE:
            # Cria um link com base no ID da consulta
            return f"https://meet.google.com/{self.id:09}".replace(" ", "")
        return None


# Modelo que representa um Prontuário médico
class Prontuario(models.Model):
    # Relação com paciente
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='prontuarios_consulta'
    )
    # Relação com profissional
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        related_name='prontuarios_consulta'
    )
    # Data e hora da criação do prontuário, gerado automaticamente
    data_registro = models.DateTimeField(auto_now_add=True)

    # Descrição do prontuário
    descricao = models.TextField()

    class Meta:
        db_table = 'prontuario'  # Nome da tabela no banco

    def __str__(self):
        # Representação do prontuário com nome do paciente e data de registro
        return f"Prontuário de {self.paciente.nome} em {self.data_registro}"


# Modelo que representa uma Prescrição médica ligada a um prontuário
class Prescricao(models.Model):
    # Relaciona a prescrição ao prontuário
    prontuario = models.ForeignKey(
        Prontuario,
        on_delete=models.CASCADE,
        related_name='prescricoes'
    )
    # Nome do medicamento prescrito
    medicamento = models.CharField(max_length=255)
    # Dosagem do medicamento
    dosagem = models.CharField(max_length=50)
    # Instruções adicionais para uso, campo opcional
    instrucoes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'prescricao'  # Nome da tabela

    def __str__(self):
        # Representação da prescrição com medicamento e paciente
        return f"{self.medicamento} para {self.prontuario.paciente.nome}"


# Modelo que representa um Agendamento de consulta
class Agendamento(models.Model):
    # Enum para tipos de agendamento (online ou presencial)
    class TipoChoices(models.TextChoices):
        ONLINE = 'Online', 'Online'
        PRESENCIAL = 'Presencial', 'Presencial'

    # Enum para status do agendamento
    class StatusChoices(models.TextChoices):
        AGENDADO = 'Agendado', 'Agendado'
        CANCELADO = 'Cancelado', 'Cancelado'
        CONCLUIDO = 'Concluído', 'Concluído'

    # Relação com paciente
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    # Relação com profissional
    profissional = models.ForeignKey(
        'profissionais.Profissional',
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    # Relação com unidade de saúde
    unidade_saude = models.ForeignKey(
        'core.UnidadeSaude',
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )
    # Especialidade médica para o agendamento
    especialidade = models.CharField(max_length=100)
    # Data e hora do agendamento
    data_hora = models.DateTimeField()
    # Tipo do agendamento (online ou presencial)
    tipo = models.CharField(
        max_length=20,
        choices=TipoChoices.choices,
        default=TipoChoices.PRESENCIAL
    )
    # Status do agendamento
    status = models.CharField(max_length=20, choices=StatusChoices.choices)

    class Meta:
        db_table = 'agendamento'  # Nome da tabela

    def __str__(self):
        # String representativa do agendamento
        return f"Agendamento de {self.paciente.nome} com {self.profissional.nome} em {self.data_hora}"

    def get_meet_link(self):
        """
        Retorna um link fictício para reunião no Google Meet caso o agendamento seja online.
        """
        if self.tipo == self.TipoChoices.ONLINE:
            # Cria um link baseado no id do agendamento
            return f"https://meet.google.com/{self.id:09}".replace(" ", "")
        return None
