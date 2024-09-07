import sys
import os
from ui.gui import setup_gui

if __name__ == "__main__":
    setup_gui()  # Inicializa a interface gráfica
    

# Adiciona o diretório "utils/" ao caminho de busca de módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))