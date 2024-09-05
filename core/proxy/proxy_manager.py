from tkinter import messagebox

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