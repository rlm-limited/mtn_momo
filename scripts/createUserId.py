import requests
from dotenv import load_dotenv
from os import getenv
from uuid import uuid4
import sys

def create_api_user(x_reference_id=None, callback_host="https://evstaging.meshpower.co.rw/payment/callback/mtn"):
    """
    Creates an API User in the MTN MoMo Sandbox.
    Returns: tuple (x_reference_id, success_boolean, error_message)
    """
    load_dotenv(override=True)
    subscription_key = getenv("PRIMARY_KEY")

    if not subscription_key:
        return None, False, "Missing PRIMARY_KEY in .env"

    if not x_reference_id:
        x_reference_id = str(uuid4())

    url = "https://sandbox.momodeveloper.mtn.com/v1_0/apiuser"

    headers = {
        "X-Reference-Id": x_reference_id,
        "Ocp-Apim-Subscription-Key": subscription_key,
    }

    data = {
        "providerCallbackHost": callback_host
    }

    try:
        response = requests.post(url=url, headers=headers, json=data)
        if response.status_code == 201:
            return x_reference_id, True, None
        else:
            return x_reference_id, False, response.text
    except Exception as e:
        return x_reference_id, False, str(e)

if __name__ == "__main__":
    ref_id = getenv("X_REFERENCE_ID")
    print(f"Creating API User with X_REFERENCE_ID: {ref_id}")
    ref_id, success, error = create_api_user(x_reference_id=ref_id)
    if success:
        print(f"User ID created successfully: {ref_id}")
    else:
        print(f"Failed to create user ID. Error: {error}")
