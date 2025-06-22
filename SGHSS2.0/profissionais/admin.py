# Importa o módulo de administração do Django
from django.contrib import admin

# Importa os modelos que serão registrados no admin
from .models import Profissional, Leito, Internacao

# Registra o modelo Profissional no admin e define como será exibido
@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    # Define as colunas visíveis na listagem de profissionais no painel admin
    list_display = ('nome', 'especialidade', 'unidade_saude')
    
    # Permite busca por nome e especialidade no campo de busca
    search_fields = ('nome', 'especialidade')

# Registra o modelo Leito no admin e define como será exibido
@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    # Define as colunas visíveis na listagem de leitos
     list_display = ('id', 'tipo_leito', 'status', 'unidade_saude', 'paciente')
    # Adiciona filtros laterais por tipo e status do leito
     list_filter = ('tipo_leito', 'status')

# Registra o modelo Internacao no admin e define como será exibido
@admin.register(Internacao)
class InternacaoAdmin(admin.ModelAdmin):
    # Define as colunas visíveis na listagem de internações
    list_display = ('paciente', 'leito', 'data_entrada', 'data_saida')

    # Permite busca por nome do paciente
    search_fields = ('paciente__nome',)
