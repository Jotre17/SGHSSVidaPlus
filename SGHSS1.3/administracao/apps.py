# Importa a classe base AppConfig, usada para configurar o aplicativo
from django.apps import AppConfig

# Define a configuração da aplicação 'administracao'
class AdministracaoConfig(AppConfig):
    # Define o tipo padrão de campo auto incrementável para chaves primárias
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome do aplicativo Django.
    name = 'administracao'