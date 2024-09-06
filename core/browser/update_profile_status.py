import requests

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