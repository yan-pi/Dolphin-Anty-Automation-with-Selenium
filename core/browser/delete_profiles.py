import requests

def delete_profiles(profile_id, auth_token):
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
