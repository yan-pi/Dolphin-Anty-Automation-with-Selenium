import requests
import json

def update_profile(profile_id, updated_data, auth_token):
    url = f"https://dolphin-anty-api.com/browser_profiles/{profile_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }
    payload = json.dumps(updated_data)

    response = requests.put(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Profile {profile_id} updated successfully.")
        return response.json()
    else:
        print(f"Error updating profile {profile_id}: {response.text}")
        return None