import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time
import os

chromedriver_path = os.getenv('CHROMEDRIVER_PATH', 'C:/Users/HP/Desktop/adbot/include/chromedriver.exe')

def open_profile(profile_id, auth_token):
    login_url = 'http://localhost:3001/v1.0/auth/login-with-token'

    request_data = {
        'token': auth_token
    }
    headers = {
        'Content-Type': 'application/json'
    }

    print(f"Enviando requisição de login para {login_url} com token auth...")
    response = requests.post(login_url, json=request_data, headers=headers)
    if response.status_code == 200: 
        print(f"Login bem-sucedido. Iniciando perfil {profile_id}...")
        req_url = f'http://localhost:3001/v1.0/browser_profiles/{profile_id}/start'
        response = requests.get(req_url)
        if response.status_code == 200:
            response_json = response.json()
            port = str(response_json['automation']['port'])
            print(f"Perfil {profile_id} iniciado na porta {port}.")
            
            chrome_drive_path = Service(chromedriver_path)
            options = webdriver.ChromeOptions()
            options.debugger_address = '127.0.0.1:' + port

            driver = webdriver.Chrome(service=chrome_drive_path, options=options)
            return driver
        else:
            print(f"Erro ao iniciar o perfil {profile_id}: {response.status_code} - {response.text}")
            return None
    else:  # Erro no login
        print(f"Erro ao fazer login: {response.status_code} - {response.text}")
        return None