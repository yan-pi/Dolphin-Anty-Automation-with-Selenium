import tkinter as tk
from tkinter import messagebox
from create_profile import create_profiles_in_bulk, update_profile
from open_profile import open_profile
from delete_browsers import list_browsers, delete_browser
import time

def get_proxies(text_widget):
    proxies = text_widget.get("1.0", tk.END).strip().split("\n")
    return proxies

def validate_proxies(proxies, num_profiles):
    if len(proxies) < num_profiles:
        messagebox.showerror("Erro", "Número de proxies insuficiente.")
        return False
    return True

def parse_proxy(proxy):
    proxy_parts = proxy.split(":")
    if len(proxy_parts) == 4:
        return proxy_parts
    else:
        messagebox.showerror("Erro", f"Formato de proxy inválido: {proxy}")
        return None

def create_proxy_details(proxy_parts, index):
    host, port, proxy_user, proxy_password = proxy_parts
    return {
        "type": "http",  # ou "socks5", "socks4" conforme necessário
        "host": host,
        "port": port,
        "login": proxy_user,
        "password": proxy_password,
        "name": f"proxy_{index+1}"
    }

def create_profile_details(proxy_details, index):
    return {
        "name": f"browser_{index+1}",
        "tags": ["rise_extension-profiles"],
        "mainWebsite": "",
        "notes": {
            "content": None
        },
        "proxy": proxy_details
    }

def create_profiles():
    num_profiles = int(entry_num_profiles.get())
    proxies = get_proxies(text_proxies)

    if not validate_proxies(proxies, num_profiles):
        return

    profiles = []
    for i in range(num_profiles):
        proxy_parts = parse_proxy(proxies[i])
        if proxy_parts is None:
            return

        proxy_details = create_proxy_details(proxy_parts, i)
        profile = create_profile_details(proxy_details, i)
        profiles.append(profile)

    create_profiles_in_bulk(profiles)
    print("Sucesso", "Perfis criados com sucesso.")
    
    print("Chamando list_and_open_profiles...")
    # Abrir perfis criados
    list_and_open_profiles()

def list_and_open_profiles():
    profiles_response = list_browsers()
    profiles = profiles_response.get('data', [])
    
    drivers = []  # Lista para armazenar todos os drivers abertos
    
    for index, profile in enumerate(profiles):
        profile_id = profile['id']
        print(f"Abrindo perfil {profile_id}...")
        
        try:
            driver = open_profile(profile_id)
            if driver:
                drivers.append(driver)
                # Mover a janela para uma posição diferente
                x_offset = (index % 3) * 400  # Mudança horizontal
                y_offset = (index // 3) * 400  # Mudança vertical
                driver.set_window_position(x_offset, y_offset)
            
            time.sleep(1)  # Aumente o tempo de espera para 15 segundos entre cada abertura
        except Exception as e:
            print(f"Erro ao iniciar o perfil {profile_id}: {e}")
            continue

    return drivers



def setup_gui():
    root = tk.Tk()
    root.title("Criar Perfis")

    tk.Label(root, text="Número de Perfis:").grid(row=0, column=0)
    global entry_num_profiles
    entry_num_profiles = tk.Entry(root)
    entry_num_profiles.grid(row=0, column=1)

    tk.Label(root, text="Proxies (um por linha):").grid(row=1, column=0)
    global text_proxies
    text_proxies = tk.Text(root, height=10, width=50)
    text_proxies.grid(row=1, column=1)

    tk.Button(root, text="Criar Perfis", command=create_profiles).grid(row=2, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()