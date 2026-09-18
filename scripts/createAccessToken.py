import requests
from dotenv import load_dotenv
from os import getenv
from base64 import b64encode
import os

# Load .env relative to the current working directory or absolute path if needed
load_dotenv(override=True)

def get_access_token():
    """
    Retrieves a Bearer Access Token from MTN MoMo API.
    Returns: string token or None
    """

    x_reference_id = getenv("X_REFERENCE_ID")
    subscription_key = getenv("PRIMARY_KEY")
    api_key = getenv("API_KEY")
    base_url = getenv("BASE_SCRIPT_URL", "https://sandbox.momodeveloper.mtn.com")

    if not all([x_reference_id, subscription_key, api_key]):
        print("Error: Missing credentials in .env (X_REFERENCE_ID, PRIMARY_KEY, API_KEY)")
        return None

    url = f"{base_url}/collection/token/"
    auth_str = b64encode(f"{x_reference_id}:{api_key}".encode()).decode()
    
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Authorization": f"Basic {auth_str}"
    }

    try:
        response = requests.post(url=url, headers=headers)
        if response.status_code == 200:
            print(f"[DEBUG] Full token response: {response.json()}")
            return response.json().get('access_token')
        else:
            print(f"Failed to Create Access Token. Status: {response.status_code}, Response: {response.text}")
            return None
    except Exception as e:
        print(f"Request Error: {e}")
        return None

if __name__ == "__main__":
    token = get_access_token()
    if token:
        print("Access Token created successfully")
        print(f"Access Token: {token}")
