import requests

def upload_extension(file_path, auth_token):
    url = "https://dolphin-anty-api.com/extensions/upload-zipped"
    headers = {
        'Authorization': 'Bearer ' + auth_token,
        'Content-Type': 'application/json'
    }
    files = {
        'file': open(file_path, 'rb')
    }
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        print("Extension uploaded successfully.")
        return response.json()
    else:
        print(f"Error uploading extension: {response.text}")
        return None