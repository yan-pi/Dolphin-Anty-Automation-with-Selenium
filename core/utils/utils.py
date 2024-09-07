import os
import sys

def get_resource_path(relative_path):
    """Retorna o caminho absoluto do recurso, lidando com o empacotamento PyInstaller"""
    if getattr(sys, 'frozen', False):  # Executando em um executável
        base_path = sys._MEIPASS  # Diretório temporário criado pelo PyInstaller
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)
