import requests
from uuid import uuid4
from dotenv import load_dotenv
from os import getenv
from base64 import b64encode


ENV_FILE_PATH: str = "./.env"

load_dotenv(ENV_FILE_PATH)

URL = "https://sandbox.momodeveloper.mtn.com/collection/token/"

X_REFERENCE_ID = getenv("X_REFERENCE_ID")
SUBSCRIPTION_KEY = getenv("PRIMARY_KEY")
API_KEY = getenv("API_KEY")


if not X_REFERENCE_ID:
    raise ValueError("X_REFERENCE_ID is not set")

if not SUBSCRIPTION_KEY:
    raise ValueError("SUBSCRIPTION_KEY is not set")

if not API_KEY:
    raise ValueError("API_KEY is not set")


print(f"X_REFERENCE_ID: {X_REFERENCE_ID}", "X_REFERENCE_ID")
print(f"API_KEY: {API_KEY}", "API_KEY")

AUTHORIZATION = b64encode(f"{X_REFERENCE_ID}:{API_KEY}".encode()).decode()

print(f"AUTHORIZATION: {AUTHORIZATION}", "AUTHORIZATION")

headers = {
    "X-Reference-Id": X_REFERENCE_ID,
    "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
    "Authorization": f"Basic {AUTHORIZATION}"
}


response = requests.post(
    url=URL,
    headers=headers
)

if response.status_code == 201:
    print("User ID created successfully")
    print(f"User ID: {X_REFERENCE_ID}")

else:
    print("Failed to create user ID")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
