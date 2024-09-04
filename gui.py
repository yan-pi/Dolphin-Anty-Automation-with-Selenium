import tkinter as tk
from profile_manager import start_profiles, stop_profiles

running = False
drivers = []  # Initialize drivers as an empty list

def toggle_profiles():
    global running, drivers  # Add drivers to the global declaration
    if running:
        stop_profiles(drivers)
        update_gui_stop()
    else:
        drivers = start_profiles(int(entry_num_profiles.get()), get_proxies(text_proxies))
        update_gui_start()

def get_proxies(text_widget):
    return text_widget.get("1.0", tk.END).strip().split("\n")

def update_gui_start():
    global running
    button_toggle.config(text="Parar")
    running = True

def update_gui_stop():
    global running, drivers
    button_toggle.config(text="Criar Perfis")
    running = False
    drivers = []

def setup_gui():
    global button_toggle, entry_num_profiles, text_proxies
    root = tk.Tk()
    root.title("Criar Perfis")

    tk.Label(root, text="Número de Perfis:").grid(row=0, column=0)
    entry_num_profiles = tk.Entry(root)
    entry_num_profiles.grid(row=0, column=1)

    tk.Label(root, text="Proxies (um por linha):").grid(row=1, column=0)
    text_proxies = tk.Text(root, height=10, width=50)
    text_proxies.grid(row=1, column=1)

    button_toggle = tk.Button(root, text="Criar Perfis", command=toggle_profiles)
    button_toggle.grid(row=2, column=0, columnspan=2)

    root.mainloop()