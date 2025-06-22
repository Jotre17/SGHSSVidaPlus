# Importa a classe base para configuração de apps do Django
from django.apps import AppConfig

# Define a configuração do aplicativo 'core'
class CoreConfig(AppConfig):
    # Define o tipo padrão de campo de chave primária como BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome do aplicativo
    name = 'core'
