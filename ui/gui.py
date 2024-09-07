import tkinter as tk
from tkinter import ttk
from core.profile.start_profiles import start_profiles
from core.profile.stop_profiles import stop_profiles
from core.profile.extension_manager import upload_extension

running = False
drivers = []
auth_token = ""

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

def setup_gui():
    global button_toggle, entry_num_profiles, text_proxies, entry_auth_token
    root = tk.Tk()
    root.title("Profile Manager")

    # Set background and text color
    root.configure(bg="#1d1d1d")
    
    # Header Label
    tk.Label(root, text="Profile Manager", bg="#1d1d1d", fg="#fff", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=20)

    # Number of Profiles
    tk.Label(root, text="Number of Profiles:", bg="#1d1d1d", fg="#fff").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_num_profiles = tk.Entry(root, bg="#2d2d2d", fg="#fff", insertbackground="#fff")
    entry_num_profiles.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Proxies
    tk.Label(root, text="Proxies (one per line):", bg="#1d1d1d", fg="#fff").grid(row=2, column=0, padx=10, pady=10, sticky="ne")
    text_proxies = tk.Text(root, height=5, width=40, bg="#2d2d2d", fg="#fff", insertbackground="#fff")
    text_proxies.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Auth Token
    tk.Label(root, text="Auth Token:", bg="#1d1d1d", fg="#fff").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    entry_auth_token = tk.Entry(root, bg="#2d2d2d", fg="#fff", insertbackground="#fff")
    entry_auth_token.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Action Button
    button_toggle = tk.Button(root, text="Create Profiles", bg="#1e6aa5", fg="#fff", bd=0, padx=20, pady=10, command=toggle_profiles)
    button_toggle.grid(row=4, column=0, columnspan=2, pady=20)

    root.mainloop()

setup_gui()
