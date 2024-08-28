import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

auth_token = os.getenv('AUTH_TOKEN')

def list_browsers():
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

def delete_browser(profile_id):
    url = f"https://dolphin-anty-api.com/browser_profiles?forceDelete=1"
    headers = {
        'Authorization': 'Bearer ' + auth_token
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        print(f"Profile {profile_id} deleted successfully.")
    else:
        print(f"Error deleting profile {profile_id}: {response.text}")