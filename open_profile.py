from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
import requests


login_url = 'http://localhost:3001/v1.0/auth/login-with-token'
auth_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYWE4OGY3Njg4ZmUzYmRlOGQ1ODVkZmI3ODVjNWRiZjg1MmJlYzBhODEwMDg3YzdhODRjZmRkYzA4OWEzNTU0MDczNWFmNmVhYjQ1ZDU5NWQiLCJpYXQiOjE3MjQ2NDAxMjAuODc5OTE3LCJuYmYiOjE3MjQ2NDAxMjAuODc5OTE5LCJleHAiOjE3NTYxNzYxMjAuODcyMzY0LCJzdWIiOiIzNjg1MzcwIiwic2NvcGVzIjpbXX0.r2jVs3Vod-NPlqkT-ZZXdf5hZjK6U7EsBxz01RCKt9dLEkeLSNyK0jfbvdD-bzLjzsRWx7U2kScKpHFERH_Won3ZNRRBb1QddjmqWsavI12lBdzzO9mp1epe-h0sHQeSEjYeD0kcJt1MW7YSsDhT-IxYyxAArfHdjILJl-RrN2lt6lfZ84MmmtBpYLRKjXxaXl_wYciz_v20dA_gmp553ZnHvOfA47WDy_UEY7OjKC8WbnqVfZKaNvoWWEB9o4GePVvMQUkM2SjZWUvF1dPg4Y-8betvRm4cWcqqKtOI7z0tRtIG9Mv7xNAYr8h46Ew4_IJHNCkbsIcKJFgwvScbnABQARkrLbHzHC1qDgAcL3wLt_JAXDgsgFmHtAAAMcIyrOtq8o7o8BMJx-eiiGHB3IKnbqOtxQHp9D_estC-sd47vrV7c-r-eTOmuRL6lpNse_7689Rpm1hyvOvRXBi80UOObAeTS8OMOSz1rmpkpRnnaQHWKiJzCBPml9XJPf_P9ruNv_3DLNd1EsPjKEvAUKU1j2hZtfT7ana6_FqcILeUEylzqr48VNrpi1lV-_wGXczF8gNGxwg_Q5vOZVPwX5wvxgmPblMRGMvWY3I-5qimdgicpF9KtpW77yWMMKDN6IAeMA70IvTk2ybMOvXNKM2d1rjNpxJM3BPMokNmzrU' # Your API Key

request_data = {
    'token':auth_token
}
headers = {
    'Content-Type': 'application/json'
}

profile_id = '' # Profile id of that you want to open

response = requests.post(login_url, json=request_data, headers=headers)
if response.status_code == 200: # Profile opened successfully

    req_url = 'http://localhost:3001/v1.0/browser_profiles/'+  profile_id  +'/start?automation=1'
    response = requests.get(req_url)
    response_json = response.json()
    port = str(response_json['automation']['port'])
    chrome_drive_path = Service("C:/Users/HP/Desktop/adbot/include/chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.debugger_address = '127.0.0.1:' + port

    driver = webdriver.Chrome(service=chrome_drive_path, options=options)

else: # Profile was not opened
    print('Error:', response.status_code)



