# Importa o módulo de administração do Django
from django.contrib import admin

# Importa o modelo UnidadeSaude que será registrado no admin
from .models import UnidadeSaude

#Modificando o estilo da pagina

admin.site.site_header = "SGHSS Vida Plus serviços de saúde"
admin.site.site_title = "SGHSS Administração"
admin.site.index_title = "Bem-vindo à administração do SGHSS"


# Registra o modelo UnidadeSaude no Django Admin
@admin.register(UnidadeSaude)
class UnidadeSaudeAdmin(admin.ModelAdmin):
    # Define as colunas que serão exibidas na listagem do admin
    list_display = ('nome', 'tipo', 'cidade', 'telefone')

    # Permite que o administrador pesquise pelo nome ou cidade
    search_fields = ('nome', 'cidade')