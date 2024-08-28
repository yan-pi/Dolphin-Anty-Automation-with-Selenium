import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

auth_token = os.getenv('AUTH_TOKEN')

def create_proxy(proxy_details):
    url = "https://dolphin-anty-api.com/proxy?Content-Type=application/json"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }
    payload = json.dumps(proxy_details)
    
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f"Proxy {proxy_details['name']} created successfully.")
        return response.json().get("proxyId")
    else:
        print(f"Error creating proxy {proxy_details['name']}: {response.text}")
        return None

def create_profile(name, proxy_details):
    proxy_id = create_proxy(proxy_details)
    if not proxy_id:
        return None
    
    url = "https://dolphin-anty-api.com/browser_profiles/mass"
    payload = {
        "common": {
            "browserType": "anty",
            "platform": "windows",
            "platformVersion": "10.0.0",
            "mainWebsite": "google",
            "useragent": {
                "mode": "manual",
                "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            },
            "webrtc": {
                "mode": "altered",
            },
            "canvas": {
                "mode": "noise"
            },
            "webgl": {
                "mode": "real"
            },
            "webglInfo": {
                "mode": "manual",
                "vendor": "Intel Inc.",
                "renderer": "Intel Iris Pro 5200",
                "webgl2Maximum": {
                    "MAX_SAMPLES": 8,
                    "MAX_DRAW_BUFFERS": 8,
                    "MAX_TEXTURE_SIZE": 16384,
                    "MAX_ELEMENT_INDEX": 4294967294,
                    "MAX_VIEWPORT_DIMS": [16384, 16384],
                    "MAX_VERTEX_ATTRIBS": 16,
                    "MAX_3D_TEXTURE_SIZE": 2048,
                    "MAX_VARYING_VECTORS": 30,
                    "MAX_ELEMENTS_INDICES": 2147483647,
                    "MAX_TEXTURE_LOD_BIAS": 15,
                    "MAX_COLOR_ATTACHMENTS": 8,
                    "MAX_ELEMENTS_VERTICES": 2147483647,
                    "MAX_RENDERBUFFER_SIZE": 16384,
                    "MAX_UNIFORM_BLOCK_SIZE": 65536,
                    "MAX_VARYING_COMPONENTS": 120,
                    "MAX_TEXTURE_IMAGE_UNITS": 32,
                    "MAX_ARRAY_TEXTURE_LAYERS": 2048,
                    "MAX_COMBINED_TEXTURE_IMAGE_UNITS": 64,
                    "MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS": 229376,
                    "MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS": 4,
                    "MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS": 229376,
                    "MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS": 4,
                    "MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS": 128
                }
            }
        },
        "items": [
            {
                "name": name,
                "tags": ["testtesttesttest"],
                "mainWebsite": "",
                "proxy": {
            		"id": proxy_id
        		},
                "statusId": 0,
            }
        ]
    }

    payload_json = json.dumps(payload)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }

    response = requests.post(url, headers=headers, data=payload_json)
    if response.status_code == 200:
        print(f"Profile {name} created successfully.")
        return response.json().get("browserProfileId")
    else:
        print(f"Error creating profile {name}: {response.text}")
        return None

def update_profile(browser_profile_id):
    url = f"https://dolphin-anty-api.com/browser_profiles/{browser_profile_id}"

    updated_payload = {
        "name": "Browser",
        "canvas": {"mode": "real"},
        "webgl": {"mode": "real"},
        "webglInfo": {
            "mode": "software"
        },
        "timezone": {
            "mode": "auto"
        },
        "locale": {
            "mode": "manual",
            "value": "tr_TR"
        },
        "geolocation": {
            "mode": "real"
        },
        "cpu": {
            "mode": "real"
        },
        "memory": {
            "mode": "real"
        }
    }

    updated_payload_json = json.dumps(updated_payload)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }

    response = requests.patch(url, headers=headers, data=updated_payload_json)

    if response.status_code == 200:
        print("Profile updated successfully.")
    else:
        print("Profile wasn't able to update.")