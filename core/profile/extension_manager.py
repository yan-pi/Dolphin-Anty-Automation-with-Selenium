import requests
from core.utils.utils import get_resource_path

def upload_extension(auth_token):
    file_path = get_resource_path('static/rise_extension_V.1.20.5.zip')

    url = "https://dolphin-anty-api.com/extensions/upload-zipped"
    headers = {
        'Authorization': 'Bearer ' + auth_token
    }
    
    # Campos obrigatórios
    payload = {
        'mainWebsite[]': 'all',  # Enviar como string 'all' ou o valor apropriado
        'sharedToEntireTeam': '1',  # Enviar '1' para representar verdadeiro
        'extensionName': 'test'  # Nome da extensão
    }

    try:
        # Enviar a extensão
        with open(file_path, 'rb') as file:
            files = {
                'file': ('rise_extension_V.1.20.5.zip', file, 'application/zip')
            }
            response = requests.post(url, headers=headers, files=files, data=payload)
            if response.status_code == 200:
                print("Extension uploaded successfully.")
                return response.json()
            else:
                print(f"Error uploading extension: {response.status_code} - {response.text}")
                return None
    except FileNotFoundError:
        print(f"Extension file not found at {file_path}")
        return None
