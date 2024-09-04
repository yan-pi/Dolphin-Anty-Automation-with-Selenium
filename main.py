import tkinter as tk
from tkinter import messagebox
from create_profile import create_profiles_in_bulk
from open_profile import open_profile
from delete_browsers import list_browsers, delete_browser, update_profile_status, close_browsers
import time

running = False  # Variável global para rastrear o estado atual
drivers = []  # Armazena os drivers dos navegadores abertos

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

def toggle_profiles():
    global running
    if running:
        stop_profiles()
    else:
        start_profiles()

def start_profiles():
    global running, drivers
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
    
    print("Abrindo perfis criados...")
    drivers = list_and_open_profiles()

    # Mudar estado para "Rodando"
    button_toggle.config(text="Parar")
    running = True


def stop_profiles():
    global running, drivers
    print("Fechando navegadores e excluindo perfis...")

    # Fechar navegadores abertos
    close_browsers(drivers)
    drivers = []  # Limpar a lista de drivers

    # Esperar um pouco para garantir que todos os navegadores foram fechados
    time.sleep(5)

    profiles_response = list_browsers()
    profiles = profiles_response.get('data', [])
    
    for profile in profiles:
        profile_id = profile['id']
        
        # Marcar o perfil como não em execução
        if profile.get('running', False):
            print(f"Perfil {profile_id} ainda está marcado como em execução. Tentando atualizar o status...")
            try:
                update_profile_status(profile_id, running=False)
                time.sleep(2)  # Esperar um pouco após a atualização
            except Exception as e:
                print(f"Erro ao atualizar o status do perfil {profile_id}: {e}")
        
        # Tentar excluir o perfil
        try:
            delete_browser(profile_id)
            print(f"Perfil {profile_id} excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir perfil {profile_id}: {e}")
    
    # Mudar estado para "Criar Perfis"
    button_toggle.config(text="Criar Perfis")
    running = False

    
    # Mudar estado para "Criar Perfis"
    button_toggle.config(text="Criar Perfis")
    running = False

def list_and_open_profiles():
    profiles_response = list_browsers()
    profiles = profiles_response.get('data', [])
    
    opened_drivers = []
    for index, profile in enumerate(profiles):
        profile_id = profile['id']
        print(f"Abrindo perfil {profile_id}...")
        
        try:
            driver = open_profile(profile_id)
            if driver:
                opened_drivers.append(driver)
                # Mover a janela para uma posição diferente
                x_offset = (index % 3) * 400  # Mudança horizontal
                y_offset = (index // 3) * 400  # Mudança vertical
                driver.set_window_position(x_offset, y_offset)
            
            time.sleep(1)  # Aumente o tempo de espera para 1 segundo entre cada abertura
        except Exception as e:
            print(f"Erro ao iniciar o perfil {profile_id}: {e}")
            continue

    return opened_drivers

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

if __name__ == "__main__":
    setup_gui()