# Importa a classe base AppConfig usada para configurar aplicativos Django
from django.apps import AppConfig

# Define a configuração do aplicativo 'pacientes'
class PacientesConfig(AppConfig):
    # Define o tipo de campo padrão para chaves primárias como BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome interno do app, que deve coincidir com o nome da pasta
    name = 'pacientes'
