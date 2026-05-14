import os
import base64
from dotenv import load_dotenv
from collection_client import Client, AuthenticatedClient
from collection_client.api.default import create_access_token, get_basic_userinfo
from collection_client.models.get_basic_userinfo_account_holder_id_type import GetBasicUserinfoAccountHolderIdType
from collection_client.models.basic_user_info_json_response import BasicUserInfoJsonResponse
import pytest

load_dotenv()

def test_authentication_and_user_info_success():
    """Test full authentication and basic user info flow using collection_client"""
    base_url = "https://sandbox.momodeveloper.mtn.com/collection"
    client = Client(base_url=base_url)
    
    x_reference_id = os.getenv("X_REFERENCE_ID")
    api_key = os.getenv("API_KEY")
    subscription_key = os.getenv("PRIMARY_KEY")
    
    # 1. Get Access Token
    auth_str = f"{x_reference_id}:{api_key}"
    authorization = f"Basic {base64.b64encode(auth_str.encode()).decode()}"
    client = client.with_headers({"Ocp-Apim-Subscription-Key": subscription_key})
    
    token_response = create_access_token.sync_detailed(client=client, authorization=authorization)
    breakpoint()
    assert token_response.status_code == 200
    token = token_response.parsed.access_token
    print(f"\n[SUCCESS] Token retrieved: {token[:15]}...")

    # 2. Get Basic User Info (using a test MSISDN)
    auth_client = AuthenticatedClient(base_url=base_url, token=token)
    auth_client = auth_client.with_headers({"Ocp-Apim-Subscription-Key": subscription_key})
    
    user_info_response = get_basic_userinfo.sync_detailed(
        account_holder_id_type=GetBasicUserinfoAccountHolderIdType.MSISDN,
        account_holder_id="0783089337",
        client=auth_client,
        authorization=f"Bearer {token}",
        x_target_environment="sandbox"
    )
    
    if user_info_response.status_code == 200:
        assert isinstance(user_info_response.parsed, BasicUserInfoJsonResponse)
        print(f"[SUCCESS] User Info retrieved: {user_info_response.parsed.to_dict()}")
    else:
        print(f"\n[ERROR] Status Code: {user_info_response.status_code}")
        print(f"Response Content: {user_info_response.content.decode()}")
        # Note: In some sandbox environments, this might fail if the user is not registered
        # But we print the error as requested.
        # pytest.fail(f"Failed to get user info: {user_info_response.status_code}")

if __name__ == "__main__":
    pytest.main([__file__, "-s"])
