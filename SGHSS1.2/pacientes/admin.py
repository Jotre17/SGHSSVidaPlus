from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'sexo', 'unidade_saude')
    search_fields = ('nome', 'cpf')


