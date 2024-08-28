import tkinter as tk
from tkinter import messagebox
from create_profile import create_profile, update_profile
from open_profile import open_profile
from delete_browsers import list_browsers, delete_browser

created_profiles = []

def create_profiles():
    num_profiles = int(entry_num_profiles.get())
    proxies = text_proxies.get("1.0", tk.END).strip().split("\n")
    
    if len(proxies) < num_profiles:
        messagebox.showerror("Erro", "Número de proxies insuficiente.")
        return

    for i in range(num_profiles):
        proxy_parts = proxies[i].split(":")
        if len(proxy_parts) == 4:
            host, port, proxy_user, proxy_password = proxy_parts
        else:
            messagebox.showerror("Erro", f"Formato de proxy inválido: {proxies[i]}")
            return

        proxy_details = {
            "type": "http",  # ou "socks5", "socks4" conforme necessário
            "host": host,
            "port": port,
            "login": proxy_user,
            "password": proxy_password,
            "name": f"proxy_{i+1}"
        }
        profile_id = create_profile(f"browser_{i+1}", proxy_details)
        if profile_id:
            update_profile(profile_id)
            created_profiles.append(profile_id)
    messagebox.showinfo("Sucesso", "Perfis criados com sucesso.")

def start_profiles():
    for profile_id in created_profiles:
        driver = open_profile(profile_id)
        if driver:
            print(f"Perfil {profile_id} iniciado com sucesso.")
        else:
            print(f"Erro ao iniciar o perfil {profile_id}.")

def create_and_start_profiles():
    create_profiles()
    start_profiles()

root = tk.Tk()
root.title("Criar Perfis")

tk.Label(root, text="Número de Perfis:").grid(row=0, column=0)
entry_num_profiles = tk.Entry(root)
entry_num_profiles.grid(row=0, column=1)

tk.Label(root, text="Proxies (um por linha):").grid(row=1, column=0)
text_proxies = tk.Text(root, height=10, width=50)
text_proxies.grid(row=1, column=1)

tk.Button(root, text="Criar e Iniciar Perfis", command=create_and_start_profiles).grid(row=2, column=0, columnspan=2)

root.mainloop()