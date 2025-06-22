#!/usr/bin/env python
# Esta linha indica ao sistema operacional que este script deve ser executado usando o interpretador Python.


import os  # Módulo para interagir com o sistema operacional.
import sys  # Módulo para acessar argumentos da linha de comando.

def main():
    """Run administrative tasks."""
    # Define a variável de ambiente que aponta para o módulo de configurações (settings) do Django.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SGHSS.settings')

    try:
        # Importa a função que executa os comandos administrativos do Django,
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Se o Django não estiver instalado ou acessível, lança uma mensagem de erro amigável.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Executa o comando passado pela linha de comando. 
    execute_from_command_line(sys.argv)

# Verifica se o script está sendo executado diretamente (e não importado como módulo).
# Se for o caso, chama a função principal.
if __name__ == '__main__':
    main()