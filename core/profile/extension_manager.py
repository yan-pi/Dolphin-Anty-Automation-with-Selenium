import requests
from core.utils.utils import get_resource_path
import os

def upload_extension(auth_token):
    # Caminho correto para o arquivo da extensão
    file_path = get_resource_path('static/rise_extension_V.1.20.5.zip')

    url = "https://dolphin-anty-api.com/extensions/upload-zipped"
    
    # Definir headers sem especificar 'Content-Type', pois será 'multipart/form-data' automaticamente
    headers = {
        'Authorization': 'Bearer ' + auth_token
    }
    
    try:
        # Abrindo o arquivo zip da extensão
        with open(file_path, 'rb') as file:
            files = {'file': file}
            # Fazendo o POST request
            response = requests.post(url, headers=headers, files=files)

            # Checando se a resposta foi bem-sucedida
            if response.status_code == 200:
                print("Extension uploaded successfully.")
                return response.json()  # Retorna a resposta JSON se necessário
            else:
                print(f"Error uploading extension: {response.status_code} - {response.text}")
                return None
    except FileNotFoundError:
        print(f"Extension file not found at {file_path}")
        return None
