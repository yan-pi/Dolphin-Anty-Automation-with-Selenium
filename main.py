import tkinter as tk
from tkinter import messagebox
from create_profile import create_profiles_in_bulk, update_profile
from open_profile import open_profile
from delete_browsers import list_browsers, delete_browser

def create_profiles():
    num_profiles = int(entry_num_profiles.get())
    proxies = text_proxies.get("1.0", tk.END).strip().split("\n")
    
    if len(proxies) < num_profiles:
        messagebox.showerror("Erro", "Número de proxies insuficiente.")
        return

    profiles = []
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

        profile = {
            "name": f"browser_{i+1}",
            "tags": ["testtesttesttest"],
            "mainWebsite": "",
            "notes": {
                "content": None,
                "color": "blue",
                "style": "text",
                "icon": None
            },
            "proxy": proxy_details,
            "statusId": 0,
            "doNotTrack": False
        }
        profiles.append(profile)

    response = create_profiles_in_bulk(profiles)
    if response:
        for profile in response.get("items", []):
            profile_id = profile.get("browserProfileId")
            if profile_id:
                update_profile(profile_id)
            else:
                messagebox.showerror("Erro", f"Falha ao criar perfil para o proxy: {profile['proxy']['name']}")

root = tk.Tk()
root.title("Criar Perfis")

tk.Label(root, text="Número de Perfis:").grid(row=0, column=0)
entry_num_profiles = tk.Entry(root)
entry_num_profiles.grid(row=0, column=1)

tk.Label(root, text="Proxies (um por linha):").grid(row=1, column=0)
text_proxies = tk.Text(root, height=10, width=50)
text_proxies.grid(row=1, column=1)

tk.Button(root, text="Criar Perfis", command=create_profiles).grid(row=2, column=0, columnspan=2)

root.mainloop()