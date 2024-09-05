import tkinter as tk
from core.profile.profile_manager import start_profiles, stop_profiles
from core.browser.create_profile import upload_extension
import os
import sys

running = False
drivers = []  # Initialize drivers as an empty list

def toggle_profiles():
    global running, drivers  # Add drivers to the global declaration
    if running:
        stop_profiles(drivers)
        update_gui_stop()
    else:
        auth_token = entry_auth_token.get()  # Get the auth token from the GUI entry
        
        # Obtenha o diretório do executável
        base_dir = os.path.dirname(sys.executable)
        # Construa o caminho do arquivo dinamicamente
        file_path = os.path.join(base_dir, 'rise_extension_V.1.20.5.zip')
        
        upload_extension(file_path, auth_token)
        drivers = start_profiles(int(entry_num_profiles.get()), get_proxies(text_proxies), auth_token)
        update_gui_start()

def get_proxies(text_widget):
    return text_widget.get("1.0", tk.END).strip().split("\n")

def update_gui_start():
    global running
    running = True
    button_toggle.config(text="Parar Perfis")

def update_gui_stop():
    global running
    running = False
    button_toggle.config(text="Criar Perfis")

def setup_gui():
    global button_toggle, entry_num_profiles, text_proxies, entry_auth_token
    root = tk.Tk()
    root.title("Criar Perfis")

    tk.Label(root, text="Número de Perfis:").grid(row=0, column=0)
    entry_num_profiles = tk.Entry(root)
    entry_num_profiles.grid(row=0, column=1)

    tk.Label(root, text="Proxies (um por linha):").grid(row=1, column=0)
    text_proxies = tk.Text(root, height=10, width=50)
    text_proxies.grid(row=1, column=1)

    tk.Label(root, text="Auth Token:").grid(row=2, column=0)
    entry_auth_token = tk.Entry(root)
    entry_auth_token.grid(row=2, column=1)

    button_toggle = tk.Button(root, text="Criar Perfis", command=toggle_profiles)
    button_toggle.grid(row=3, column=0, columnspan=2)

    root.mainloop()