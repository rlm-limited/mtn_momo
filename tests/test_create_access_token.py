import os
import base64
from dotenv import load_dotenv
from collection_client import Client
from collection_client.api.default import create_access_token
from collection_client.models.token_post_200_application_json_response import TokenPost200ApplicationJsonResponse
import pytest

load_dotenv()

def test_create_access_token_success():
    """Test CreateAccessToken successfully using collection_client"""
    # Use the product-specific path in the base_url
    base_url = "https://sandbox.momodeveloper.mtn.com/collection"
    client = Client(base_url=base_url)
    
    x_reference_id = os.getenv("X_REFERENCE_ID", "").replace('"', '').replace("'", "")
    api_key = os.getenv("API_KEY", "").replace('"', '').replace("'", "")
    subscription_key = os.getenv("PRIMARY_KEY", "").replace('"', '').replace("'", "")
    
    if not all([x_reference_id, api_key, subscription_key]):
        pytest.skip("Credentials missing in .env")
        
    auth_str = f"{x_reference_id}:{api_key}"
    authorization = f"Basic {base64.b64encode(auth_str.encode()).decode()}"
    
    client = client.with_headers({
        "Ocp-Apim-Subscription-Key": subscription_key,
        "X-Reference-Id": x_reference_id
    })
    
    response = create_access_token.sync_detailed(
        client=client,
        authorization=authorization
    )
    if response.status_code == 200:
        assert isinstance(response.parsed, TokenPost200ApplicationJsonResponse)
        assert response.parsed.access_token is not None
        print(f"\n[SUCCESS] Access Token: {response.parsed.access_token[:15]}...")
        print(response.parsed)
    else:
        print(f"\n[ERROR] Status Code: {response.status_code}")
        print(f"Response Content: {response.content.decode()}")
        pytest.fail(f"Failed to create access token: {response.status_code}")

if __name__ == "__main__":
    pytest.main([__file__, "-s"])
