# Importa o módulo de administração do Django
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from .forms import GroupForm  # Novo formulário para filtrar permissões

# Importa os modelos pertencentes ao app 'administracao'
from .models import RegistroAcesso, Suprimento, RelatorioFinanceiro

# Importa o modelo Administrador que está definido no app 'core'
from core.models import Administrador

# Remove o GroupAdmin original para sobrescrever com o personalizado
admin.site.unregister(Group)

# Registra o modelo Group com um formulário customizado que filtra permissões
@admin.register(Group)
class CustomGroupAdmin(GroupAdmin):
    form = GroupForm

# Registra o modelo Administrador no Django Admin com configurações personalizadas
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'permissao')
    search_fields = ['nome', 'email']
    list_filter = ['permissao']

# Registra o modelo RegistroAcesso com configurações para visualização no admin
@admin.register(RegistroAcesso)
class RegistroAcessoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_hora', 'acao')
    search_fields = ['usuario__nome', 'acao']
    list_filter = ['data_hora']

# Registra o modelo Suprimento no admin
@admin.register(Suprimento)
class SuprimentoAdmin(admin.ModelAdmin):
    list_display = ('unidade_saude', 'nome', 'quantidade', 'tipo', 'validade')
    search_fields = ['nome']

# Registra o modelo RelatorioFinanceiro no admin
@admin.register(RelatorioFinanceiro)
class RelatorioFinanceiroAdmin(admin.ModelAdmin):
    list_display = ('unidade_saude', 'valor', 'data_registro')
    search_fields = ['unidade_saude__nome']