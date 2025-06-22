# Importa o módulo de modelos do Django
from django.db import models

# Define o modelo Paciente, que representa um paciente cadastrado no sistema
class Paciente(models.Model):
    
    # Define um enumerador com as opções válidas para o campo 'sexo'
    class SexoChoices(models.TextChoices):
        FEMININO = 'Feminino', 'Feminino'
        MASCULINO = 'Masculino', 'Masculino'

    # Chave estrangeira para a unidade de saúde à qual o paciente está vinculado
    unidade_saude = models.ForeignKey('core.UnidadeSaude',on_delete=models.CASCADE,related_name='pacientes')

    # Campos básicos do paciente
    nome = models.CharField(max_length=200)                             # Nome completo
    cpf = models.CharField(max_length=14, default='000.000.000-00')     # CPF formatado 
    sexo = models.CharField(max_length=10, choices=SexoChoices.choices) # Sexo com escolhas pré-definidas (masc/fem)
    data_nascimento = models.DateField(default='DD/MM/AAAA')            # Data de nascimento (o default está como string simbólica)
    cidade = models.CharField(max_length=255, default='Cidade - EE')    # Cidade com valor padrão fictício
    cep = models.CharField(max_length=10, default='00.000-000')         # CEP com máscara padrão
    endereco = models.CharField(max_length=255)                         # Endereço completo
    telefone = models.CharField(max_length=15, default='(XX) XXXXX-XXXX') # Telefone formatado
    email = models.EmailField(max_length=100, blank=True, null=True)    # E-mail opcional

    class Meta:
        db_table = 'paciente'  # Nome da tabela no banco de dados

    def __str__(self):
        # Representação legível do objeto (exibido no Django admin, por exemplo)
        return f"{self.nome} - {self.cpf}"
