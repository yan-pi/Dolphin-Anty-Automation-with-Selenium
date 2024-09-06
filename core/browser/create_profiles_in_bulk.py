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