from django.db import models

class Paciente(models.Model):
    class SexoChoices(models.TextChoices):
        FEMININO = 'Feminino', 'Feminino'
        MASCULINO = 'Masculino', 'Masculino'

    unidade_saude = models.ForeignKey(
        'core.UnidadeSaude',
        on_delete=models.CASCADE,
        related_name='pacientes'
    )
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, default='000.000.000-00')
    sexo = models.CharField(max_length=10, choices=SexoChoices.choices)
    data_nascimento = models.DateField(default= 'DD/MM/AAAA')
    cidade = models.CharField(max_length=255, default='Cidade - EE')
    cep = models.CharField(max_length=8, default='00.000-000')
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, default= '(XX) XXXXX-XXXX')
    email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'paciente'

    def __str__(self):
        return f"{self.nome} - {self.cpf}"

