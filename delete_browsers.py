import requests
import json

auth_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYWE4OGY3Njg4ZmUzYmRlOGQ1ODVkZmI3ODVjNWRiZjg1MmJlYzBhODEwMDg3YzdhODRjZmRkYzA4OWEzNTU0MDczNWFmNmVhYjQ1ZDU5NWQiLCJpYXQiOjE3MjQ2NDAxMjAuODc5OTE3LCJuYmYiOjE3MjQ2NDAxMjAuODc5OTE5LCJleHAiOjE3NTYxNzYxMjAuODcyMzY0LCJzdWIiOiIzNjg1MzcwIiwic2NvcGVzIjpbXX0.r2jVs3Vod-NPlqkT-ZZXdf5hZjK6U7EsBxz01RCKt9dLEkeLSNyK0jfbvdD-bzLjzsRWx7U2kScKpHFERH_Won3ZNRRBb1QddjmqWsavI12lBdzzO9mp1epe-h0sHQeSEjYeD0kcJt1MW7YSsDhT-IxYyxAArfHdjILJl-RrN2lt6lfZ84MmmtBpYLRKjXxaXl_wYciz_v20dA_gmp553ZnHvOfA47WDy_UEY7OjKC8WbnqVfZKaNvoWWEB9o4GePVvMQUkM2SjZWUvF1dPg4Y-8betvRm4cWcqqKtOI7z0tRtIG9Mv7xNAYr8h46Ew4_IJHNCkbsIcKJFgwvScbnABQARkrLbHzHC1qDgAcL3wLt_JAXDgsgFmHtAAAMcIyrOtq8o7o8BMJx-eiiGHB3IKnbqOtxQHp9D_estC-sd47vrV7c-r-eTOmuRL6lpNse_7689Rpm1hyvOvRXBi80UOObAeTS8OMOSz1rmpkpRnnaQHWKiJzCBPml9XJPf_P9ruNv_3DLNd1EsPjKEvAUKU1j2hZtfT7ana6_FqcILeUEylzqr48VNrpi1lV-_wGXczF8gNGxwg_Q5vOZVPwX5wvxgmPblMRGMvWY3I-5qimdgicpF9KtpW77yWMMKDN6IAeMA70IvTk2ybMOvXNKM2d1rjNpxJM3BPMokNmzrU' # Your API Key

def listBrowsers():

    url = "https://dolphin-anty-api.com/browser_profiles"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200: # Select Profile List

        response_data = json.loads(response.text)
        data = response_data.get('data', [])

        if data:
            url = "https://dolphin-anty-api.com/browser_profiles?forceDelete=1"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + auth_token
            }
            for item in data:
                profile_id = item.get("id")
                payload = {'ids': [profile_id], 'forceDelete': True}
                
                delete_url = f"https://dolphin-anty-api.com/browser_profiles/{profile_id}"
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + auth_token
                }
                
                # Delete all profiles
                response = requests.delete(delete_url, headers=headers, json=payload)
                print(response.text)

        else:
            print("There isn't any profile created.")


listBrowsers()

