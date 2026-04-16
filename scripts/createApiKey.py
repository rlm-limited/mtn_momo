import requests
from uuid import uuid4
from dotenv import load_dotenv
from os import getenv


ENV_FILE_PATH: str = "./.env"

load_dotenv(ENV_FILE_PATH)



X_REFERENCE_ID = getenv("X_REFERENCE_ID")
API_KEY = getenv("PRIMARY_KEY")



if not X_REFERENCE_ID:
    raise ValueError("X_REFERENCE_ID is not set")

if not API_KEY:
    raise ValueError("PRIMARY_KEY is not set")

URL = f"https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{X_REFERENCE_ID}/apikey"


print(f"X_REFERENCE_ID: {X_REFERENCE_ID}", "X_REFERENCE_ID")
print(f"API_KEY: {API_KEY}", "API_KEY")
print(f"URL: {URL}", "URL")


headers = {
    "X-Reference-Id": X_REFERENCE_ID,
    "Ocp-Apim-Subscription-Key": API_KEY,
}


response = requests.post(
    url=URL,
    headers=headers,
)

if response.status_code == 201:
    print("api key created successfully")
    print(f"API Key: {response.json()}")

else:
    print("Failed to create api key")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
