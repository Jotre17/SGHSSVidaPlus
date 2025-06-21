from django.contrib import admin
from .models import Profissional, Leito, Internacao

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'unidade_saude')
    search_fields = ('nome', 'especialidade')


@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipoLeito', 'status', 'unidade_saude', 'paciente')
    list_filter = ('tipoLeito', 'status')


@admin.register(Internacao)
class InternacaoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'leito', 'data_entrada', 'data_saida')
    search_fields = ('paciente__nome',)
