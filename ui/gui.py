import tkinter as tk
from tkinter import ttk
from core.profile.start_profiles import start_profiles
from core.profile.stop_profiles import stop_profiles
from core.profile.extension_manager import upload_extension
from core.utils.auth_service import AuthService

running = False
drivers = []
auth_token = ""
auth_service = AuthService()

def toggle_profiles():
    global running, drivers, auth_token
    if running:
        stop_profiles(drivers, auth_token)
        update_gui_stop()
    else:
        auth_token = entry_auth_token.get()
        if not auth_token:
            print("Auth token is required.")
            return
        upload_extension(auth_token)
        drivers = start_profiles(
            int(entry_num_profiles.get()), 
            get_proxies(text_proxies), 
            auth_token
        )
        update_gui_start()

def get_proxies(text_widget):
    return text_widget.get("1.0", tk.END).strip().split("\n")

def update_gui_start():
    global running
    running = True
    button_toggle.config(text="Stop Profiles")

def update_gui_stop():
    global running
    running = False
    button_toggle.config(text="Create Profiles")

def login_user():
    username = entry_username.get()
    password = entry_password.get()
    
    success, message = auth_service.login(username, password)
    
    if success:
        print(message)
        open_profile_manager()
    else:
        print(f"Erro: {message}")

def open_profile_manager():
    global button_toggle, entry_num_profiles, text_proxies, entry_auth_token
    login_frame.pack_forget()  # Remove a tela de login

    # Gerenciador de Perfis
    profile_manager_frame = tk.Frame(root, bg="#1d1d1d")
    profile_manager_frame.pack(fill="both", expand=True)

    # Header Label
    tk.Label(profile_manager_frame, text="Profile Manager", bg="#1d1d1d", fg="#fff", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=20)

    # Number of Profiles
    tk.Label(profile_manager_frame, text="Number of Profiles:", bg="#1d1d1d", fg="#fff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_num_profiles = tk.Entry(profile_manager_frame, bg="#2d2d2d", fg="#fff", insertbackground="#fff")
    entry_num_profiles.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Proxies
    tk.Label(profile_manager_frame, text="Proxies (one per line):", bg="#1d1d1d", fg="#fff").grid(row=2, column=0, padx=10, pady=10, sticky="ne")
    text_proxies = tk.Text(profile_manager_frame, height=5, width=40, bg="#2d2d2d", fg="#fff", insertbackground="#fff")
    text_proxies.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Auth Token
    tk.Label(profile_manager_frame, text="Auth Token:", bg="#1d1d1d", fg="#fff").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_auth_token = tk.Entry(profile_manager_frame, bg="#2d2d2d", fg="#fff", insertbackground="#fff")
    entry_auth_token.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Action Button
    button_toggle = tk.Button(profile_manager_frame, text="Create Profiles", bg="#1e6aa5", fg="#fff", bd=0, padx=20, pady=10, command=toggle_profiles)
    button_toggle.grid(row=4, column=0, columnspan=2, pady=20)

def setup_gui():
    global root, entry_username, entry_password, login_frame
    root = tk.Tk()
    root.title("Login")

    # Tela de Login
    login_frame = tk.Frame(root, bg="#1d1d1d")
    login_frame.pack(fill="both", expand=True)

    tk.Label(login_frame, text="Login", bg="#1d1d1d", fg="#fff", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(login_frame, text="Username:", bg="#1d1d1d", fg="#fff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_username = tk.Entry(login_frame, bg="#2d2d2d", fg="#fff", insertbackground="#fff")
    entry_username.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    tk.Label(login_frame, text="Password:", bg="#1d1d1d", fg="#fff").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    entry_password = tk.Entry(login_frame, show="*", bg="#2d2d2d", fg="#fff", insertbackground="#fff")
    entry_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    button_login = tk.Button(login_frame, text="Login", bg="#1e6aa5", fg="#fff", bd=0, padx=20, pady=10, command=login_user)
    button_login.grid(row=3, column=0, columnspan=2, pady=20)

    root.mainloop()

setup_gui()
