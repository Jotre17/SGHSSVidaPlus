from django.contrib import admin
from .models import Consulta, Prontuario, Prescricao, Agendamento
from django.utils.html import format_html


# Admin para o modelo Consulta
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    # Campos mostrados na lista do admin para Consulta
    list_display = ('paciente', 'profissional', 'data_hora', 'tipo', 'status')
    # Filtros laterais para tipo e status
    list_filter = ('tipo', 'status')
    # Permite busca por nomes do paciente e profissional
    search_fields = ('paciente__nome', 'profissional__nome')


# Admin para o modelo Prontuario
@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    # Campos visíveis na lista
    list_display = ('paciente', 'profissional', 'data_registro')
    # Busca por nome do paciente
    search_fields = ('paciente__nome',)


# Admin para o modelo Prescricao
@admin.register(Prescricao)
class PrescricaoAdmin(admin.ModelAdmin):
    # Campos exibidos na listagem
    list_display = ('prontuario', 'medicamento', 'dosagem')
    # Busca pelo nome do medicamento
    search_fields = ('medicamento',)


# Admin para o modelo Agendamento
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    # Campos mostrados na listagem do admin
    list_display = ('id', 'paciente', 'profissional', 'data_hora', 'tipo', 'status', 'meet_link')
    # Campo somente leitura para exibir o link do Meet
    readonly_fields = ('meet_link',)

    # Método para mostrar o link do Meet na listagem
    def meet_link(self, obj):
        # Verifica se o tipo do agendamento é 'Online' (considerar case-sensitive)
        if obj.tipo == 'Online':
            # Gera o link do Meet (supondo que get_meet_link() esteja implementado no model)
            link = obj.get_meet_link()
            # Retorna o link formatado em HTML para o admin exibir clicável e abrir em nova aba
            return format_html('<a href="{}" target="_blank">{}</a>', link, "Abrir Meet")
        # Se não for online, informa que é presencial
        return "Consulta presencial"

    # Define o título da coluna no admin
    meet_link.short_description = "Link do Meet"