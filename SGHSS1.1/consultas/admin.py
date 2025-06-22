from django.contrib import admin
from .models import Consulta, Prontuario, Prescricao


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'profissional', 'data_hora', 'tipo', 'status')
    list_filter = ('tipo', 'status')
    search_fields = ('paciente__nome', 'profissional__nome')


@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'profissional', 'data_registro')
    search_fields = ('paciente__nome',)


@admin.register(Prescricao)
class PrescricaoAdmin(admin.ModelAdmin):
    list_display = ('prontuario', 'medicamento', 'dosagem')
    search_fields = ('medicamento',)
