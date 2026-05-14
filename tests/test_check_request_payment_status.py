import os
import base64
import uuid
import time
from dotenv import load_dotenv
from collection_client import Client, AuthenticatedClient
from collection_client.api.default import create_access_token, requestto_pay, requestto_pay_transaction_status
from collection_client.models.request_to_pay import RequestToPay
from collection_client.models.party import Party
from collection_client.models.party_party_id_type import PartyPartyIdType
from collection_client.models.request_to_pay_result import RequestToPayResult
import pytest

load_dotenv()

def get_token():
    base_url = "https://sandbox.momodeveloper.mtn.com/collection"
    client = Client(base_url=base_url)
    x_reference_id = os.getenv("X_REFERENCE_ID")
    api_key = os.getenv("API_KEY")
    subscription_key = os.getenv("PRIMARY_KEY")
    auth_str = f"{x_reference_id}:{api_key}"
    authorization = f"Basic {base64.b64encode(auth_str.encode()).decode()}"
    client = client.with_headers({"Ocp-Apim-Subscription-Key": subscription_key})
    response = create_access_token.sync_detailed(client=client, authorization=authorization)
    return response.parsed.access_token if response.status_code == 200 else None

def test_check_request_payment_status_success():
    """Test RequestToPayTransactionStatus successfully using collection_client"""
    base_url = "https://sandbox.momodeveloper.mtn.com/collection"
    subscription_key = os.getenv("PRIMARY_KEY")
    token = get_token()
    
    if not token:
        pytest.fail("Failed to get token for check_status test")
        
    client = AuthenticatedClient(base_url=base_url, token=token)
    client = client.with_headers({"Ocp-Apim-Subscription-Key": subscription_key})
    
    # 1. Create a payment first
    x_reference_id = str(uuid.uuid4())
    body = RequestToPay(
        amount="100",
        currency="EUR",
        external_id=str(uuid.uuid4()),
        payer=Party(
            party_id_type=PartyPartyIdType.MSISDN,
            party_id="0783089337"
        ),
        payer_message="Status Check Test",
        payee_note="Status Check Note"
    )
    
    requestto_pay.sync_detailed(
        client=client,
        body=body,
        authorization=f"Bearer {token}",
        x_reference_id=x_reference_id,
        x_target_environment="sandbox"
    )
    
    # Give the sandbox a moment to process
    time.sleep(2)
    
    # 2. Check its status
    response = requestto_pay_transaction_status.sync_detailed(
        reference_id=x_reference_id,
        client=client,
        authorization=f"Bearer {token}",
        x_target_environment="sandbox"
    )
    
    if response.status_code == 200:
        assert isinstance(response.parsed, RequestToPayResult)
        assert response.parsed.amount == "100"
        assert response.parsed.currency == "EUR"
        print(f"\n[SUCCESS] Transaction Status: {response.parsed.status}")
        print(f"Details: {response.parsed.to_dict()}")
    else:
        print(f"\n[ERROR] Status Code: {response.status_code}")
        print(f"Response Content: {response.content.decode()}")
        pytest.fail(f"Failed to get transaction status: {response.status_code}")

if __name__ == "__main__":
    pytest.main([__file__, "-s"])
