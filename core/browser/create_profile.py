import requests
import json

def create_profiles_in_bulk(profiles, auth_token):
    url = "https://dolphin-anty-api.com/browser_profiles/mass"
    payload = json.dumps({
        "common": {
            "browserType": "anty",
            "platform": "windows",
            "platformVersion": "10.0.0",
            "mainWebsite": "google",
            "useragent": {
                "mode": "manual",
                "value": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            },
            "webrtc": {
                "mode": "altered",
                "ipAddress": None
            },
            "canvas": {
                "mode": "noise"
            },
            "webgl": {
                "mode": "real"
            },
            "webglInfo": {
                "mode": "random"
            },
            "geolocation": {
                "mode": "real",
                "latitude": None,
                "longitude": None
            },
            "cpu": {
                "mode": "real",
                "value": None
            },
            "memory": {
                "mode": "manual",
                "value": 8
            },
            "timezone": {
                "mode": "auto",
                "value": None
            },
            "locale": {
                "mode": "auto",
                "value": None
            }
        },
        "items": profiles
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print("Profiles created successfully.")
        return response.json()
    else:
        print(f"Error creating profiles: {response.text}")
        return None

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