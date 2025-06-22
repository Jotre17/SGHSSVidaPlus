from os import path
from django.contrib import admin
from django.http import HttpResponse
from .models import Consulta, Prontuario, Prescricao, Agendamento
from django.utils.html import format_html
from django.urls import path

from reportlab.pdfgen import canvas
from io import BytesIO


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

#Admin para o modelo Prescricao
@admin.register(Prescricao)
class PrescricaoAdmin(admin.ModelAdmin):
    list_display = ('prontuario', 'medicamento', 'dosagem', 'botao_pdf')
    search_fields = ('medicamento',)

    # Adiciona uma URL personalizada para gerar o PDF
    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path('<int:prescricao_id>/imprimir/', self.admin_site.admin_view(self.gerar_pdf), name='imprimir-receita'),
        ]
        return custom + urls

    # Adiciona um botão na listagem para baixar o PDF
    def botao_pdf(self, obj):
        return format_html(
            '<a class="button" href="{}">Imprimir PDF</a>',
            f"{obj.id}/imprimir/"
        )
    botao_pdf.short_description = "Receita"
    botao_pdf.allow_tags = True

    # Gera o PDF quando o botão for clicado
    def gerar_pdf(self, request, prescricao_id):
        prescricao = Prescricao.objects.get(id=prescricao_id)

        paciente = prescricao.prontuario.paciente
        profissional = prescricao.prontuario.profissional

        buffer = BytesIO()
        p = canvas.Canvas(buffer)
        # Cabeçalho
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 800, "Vida Plus Saúde")
        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, 780, "RECEITA MÉDICA")
         # Conteúdo do PDF
        p.setFont("Helvetica", 12)
        p.drawString(100, 760, f"Paciente: {paciente.nome}")
        p.drawString(100, 740, f"CPF: {paciente.cpf}")
        p.drawString(100, 720, f"Profissional: {profissional.nome}")
        p.drawString(100, 700, f"CRM/COREN: {profissional.crm_coren}")
        p.drawString(100, 660, f"Medicamento: {prescricao.medicamento}")
        p.drawString(100, 640, f"Dosagem: {prescricao.dosagem}")
        p.drawString(100, 620, f"Modo de uso: {prescricao.instrucoes or '---'}")
           # Finaliza o PDF
        p.showPage()
        p.save()
        buffer.seek(0)

        return HttpResponse(buffer.getvalue(), content_type='application/pdf')


# Admin para o modelo Agendamento
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    # Campos mostrados na listagem do admin
    list_display = ('id', 'paciente', 'profissional', 'data_hora', 'tipo', 'status', 'meet_link')
    # Campo somente leitura para exibir o link do Meet
    readonly_fields = ('meet_link',)

    # Método para mostrar o link do Meet na listagem
    def meet_link(self, obj):
        # Verifica se o tipo do agendamento é 'Online' (case-sensitive)
        if obj.tipo == 'Online':
            # Gera o link do Meet (supondo que get_meet_link() esteja implementado no model)
            link = obj.get_meet_link()
            # Retorna o link formatado em HTML para abrir em nova aba
            return format_html('<a href="{}" target="_blank">{}</a>', link, "Abrir Meet")
        # Se não for online, informa que é presencial
        return "Consulta presencial"

    # Define o título da coluna no admin
    meet_link.short_description = "Link do Meet"
