import requests

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