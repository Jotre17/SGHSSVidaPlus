from django.contrib import admin
from .models import RegistroAcesso, Suprimento, RelatorioFinanceiro
from core.models import Administrador

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'permissao')
    search_fields = ['nome', 'email']  


@admin.register(RegistroAcesso)
class RegistroAcessoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data_hora', 'acao')
    search_fields = ['usuario__nome', 'acao']  


@admin.register(Suprimento)
class suprimentoAdmin(admin.ModelAdmin):
    list_display = ('unidade_saude', 'nome', 'quantidade', 'tipo', 'validade')
    search_fields = ['nome']  


@admin.register(RelatorioFinanceiro)
class RelatorioFinanceiroAdmin(admin.ModelAdmin):
    list_display = ('unidade_saude', 'valor', 'data_registro')
    search_fields = ['unidade_saude__nome']  
