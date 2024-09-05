import requests
import json

def list_browsers(auth_token):
    url = "https://dolphin-anty-api.com/browser_profiles"
    headers = {
        'Authorization': 'Bearer ' + auth_token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Browsers listed successfully.", response.json())
        return response.json()
    else:
        print("Error listing browsers:", response.text)
        return []

def delete_browser(profile_id, auth_token):
    url = "https://dolphin-anty-api.com/browser_profiles?forceDelete=1"
    headers = {
        'Authorization': 'Bearer ' + auth_token,
        'Content-Type': 'application/json'
    }
    payload = {
        'ids': [profile_id]
    }
    response = requests.delete(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"Profile {profile_id} deleted successfully.")
    else:
        print(f"Error deleting profile {profile_id}: {response.text}")

def close_browsers(drivers):
    for index, driver in enumerate(drivers):
        try:
            driver.quit()
            print(f"Navegador {index+1} fechado com sucesso.")
        except Exception as e:
            print(f"Erro ao fechar navegador {index+1}: {e}")
        finally:
            # Garantir que o driver seja marcado como None, mesmo se houver uma exceção
            drivers[index] = None
    
    # Limpar a lista de drivers
    while None in drivers:
        drivers.remove(None)

def update_profile_status(profile_id, auth_token, running=False):
    url = f"https://dolphin-anty-api.com/browser_profiles/{profile_id}"
    headers = {
        'Authorization': 'Bearer ' + auth_token,
        "Content-Type": "application/json"
    }
    data = {
        "running": running
    }
    response = requests.patch(url, json=data, headers=headers)
    if response.status_code == 200:
        print(f"Status do perfil {profile_id} atualizado com sucesso.")
    else:
        print(f"Falha ao atualizar o status do perfil {profile_id}. Status code: {response.status_code}")
        print(f"Resposta: {response.text}")