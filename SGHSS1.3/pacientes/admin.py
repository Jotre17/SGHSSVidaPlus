# Importa o módulo de administração do Django
from django.contrib import admin

# Importa o modelo Paciente do aplicativo 'core'
from .models import Paciente

# Registra o modelo Paciente no Django Admin com configurações personalizadas
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    # Define os campos que serão exibidos como colunas na listagem
    list_display = ('nome', 'cpf', 'sexo', 'unidade_saude')
    # Define os campos para realizar buscas no admin
    search_fields = ('nome', 'cpf')


