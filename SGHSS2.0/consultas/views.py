# Importa a classe base de ViewSets do Django REST Framework
from rest_framework import viewsets

# Importa os modelos que serão manipulados pelas views
from .models import Consulta, Agendamento, Prescricao, Prontuario

# Importa os serializers que transformam os dados dos modelos em JSON e vice-versa
from .serializers import ConsultaSerializer, AgendamentoSerializer, ProntuarioSerializer, PrescricaoSerializer

# Biblioteca para geração de PDF
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse


class ConsultaViewSet(viewsets.ModelViewSet):
    # Define o conjunto de dados (queryset) que será manipulado por essa view
    queryset = Consulta.objects.all()
    # Define qual serializer será usado para conversão dos dados
    serializer_class = ConsultaSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer

# ViewSet responsável por lidar com as requisições de Prescrição
class PrescricaoViewSet(viewsets.ModelViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer

    # Sobrescreve o método de criação padrão
def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    prescricao = serializer.save()

    # Geração do PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    paciente = prescricao.prontuario.paciente
    profissional = prescricao.prontuario.profissional

    p.drawString(100, 800, "RECEITA MÉDICA")
    p.drawString(100, 770, f"Paciente: {paciente.nome}")
    p.drawString(100, 750, f"CPF: {paciente.cpf}")
    p.drawString(100, 720, f"Profissional: {profissional.nome}")
    p.drawString(100, 700, f"CRM/COREN: {profissional.crm_coren}")
    p.drawString(100, 660, f"Medicamento: {prescricao.medicamento}")
    p.drawString(100, 640, f"Dosagem: {prescricao.dosagem}")
    p.drawString(100, 620, f"Instruções: {prescricao.instrucoes or '---'}")

    p.showPage()
    p.save()
    buffer.seek(0)

    # Retorna o PDF diretamente como resposta HTTP
    return HttpResponse(buffer.getvalue(), content_type='application/pdf')