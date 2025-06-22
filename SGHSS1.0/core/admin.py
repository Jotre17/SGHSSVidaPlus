# app: core
# script: admin.py

from django.contrib import admin
from .models import UnidadeSaude

@admin.register(UnidadeSaude)
class UnidadeSaudeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'cidade', 'telefone')
    search_fields = ('nome', 'cidade')
