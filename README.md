# MTN Momo API Client Library

This repository contains a Python client library for interacting with the MTN Momo API. The library provides an easy-to-use interface for developers to integrate MTN Momo payment functionalities into their applications.

## Features

- Create and manage payment requests

## Installation

You can install the library using pip:

```bash
pip install "mtn-momo @ git+https://github.com/rlm-limited/mtn_momo.git"
```

## Usage

## Callbacks

MoMo has **two** separate callback settings. Mixing them up is the usual reason callbacks never arrive:

| Setting | Where it is set | Format | Scope |
| --- | --- | --- | --- |
| `providerCallbackHost` | Body of `POST /v1_0/apiuser`, at API user creation | **Bare hostname only** — no scheme, no path, no port (e.g. `evstaging.meshpower.co.rw`) | Fixed for the life of the API user |
| `X-Callback-Url` | Request header on `requesttopay` and similar calls | Full HTTPS URL, must sit under the registered host | Per transaction |

### Registering a new callback provider URL

**There is no update endpoint for `providerCallbackHost`.** MTN's `POST /v1_0/apiuser` is create-only, so pointing callbacks at a new host means provisioning a **new API user** with a **new `X-Reference-Id`**, then minting a **new `API_KEY`** for it. The previous `API_KEY` belongs to the old API user and will stop working once you switch.

1. Generate a fresh reference id:

   ```bash
   python -c "import uuid; print(uuid.uuid4())"
   ```

2. In `.env`, set `X_REFERENCE_ID` to that UUID and `PROVIDER_CALLBACK_HOST` to the new bare hostname.

3. Create the API user (expects `201`):

   ```bash
   python scripts/createUserId.py
   ```

   A `409` means that UUID is already registered — go back to step 1 and generate another one.

4. Create the matching API key (expects `201`) and write the returned value to `.env` as `API_KEY`:

   ```bash
   python scripts/createApiKey.py
   ```

5. Read the API user back to confirm what MTN actually stored — check `providerCallbackHost` and `targetEnvironment`:

   ```bash
   python scripts/checkApiUser.py
   ```

6. Confirm the new `X_REFERENCE_ID` / `API_KEY` pair authenticates:

   ```bash
   python scripts/createAccessToken.py
   ```

7. Set `CALLBACK_URL` in `.env` to the full URL under the new host, then trigger a payment and watch the endpoint receive the callback:

   ```bash
   python scripts/requestToPay.py 100
   ```

**Note:** `providerCallbackHost` must be a bare hostname. Sending a full URL such as `https://example.com/payment/callback` is the most common reason step 3 is rejected.

**Note:** `X-Callback-Url` must be HTTPS, publicly reachable, hold a valid certificate, and live under the registered `providerCallbackHost`. MoMo silently drops callbacks it cannot deliver — it will not tell you the URL was wrong. Verify the registration with `checkApiUser.py` rather than assuming it worked, and use `checkRequestToPayStatus.py` to confirm a transaction independently of whether its callback landed.

### Environment variables

These live in `.env`, which is gitignored — values are never committed.

| Variable | Role |
| --- | --- |
| `PRIMARY_KEY` | Subscription key from the MoMo developer portal, sent as `Ocp-Apim-Subscription-Key` |
| `X_REFERENCE_ID` | UUID identifying the API user; also the username half of the token Basic auth |
| `API_KEY` | API key generated for that API user; the password half of the token Basic auth |
| `PROVIDER_CALLBACK_HOST` | Bare hostname registered against the API user |
| `CALLBACK_URL` | Full URL sent as `X-Callback-Url` on payment requests |

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

### Update OpenAPI Specification

If you need to update the OpenAPI specification, you can place it in the `docs` directory and run the following script to clean it up:

```bash
python scripts/fixCollectionOpenApi.py
```

**Note:** The script will read the `collection.json` file from the `docs` directory, clean it up, and save the cleaned version as `collection_fixed.json` in the same directory.

Make sure to update the paths in the script if your OpenAPI specification is located elsewhere. The working directory should be the root of the repository when running the script.

### Generate Client Library
To generate the client library from the OpenAPI specification, you can use the OpenAPI Generator CLI. First, make sure you have it installed:

```bash
openapi-python-client generate --path docs/collection_fixed.json
```


## Workflow to Create a New API User and Key

1. Create a new user ID with a unique `X_REFERENCE_ID` and set the `PROVIDER_CALLBACK_HOST` in `.env`.

```sh
Generate a new UUID for X_REFERENCE_ID:
python -c "import uuid; print(uuid.uuid4())"
```
Note: store the generated UUID in `.env` as `X_REFERENCE_ID`.

2. Create the API user by running the `createUserId.py` script. This will register the new user with MTN Momo.

```sh
python scripts/createUserId.py
```

3. Create the API key for the new user by running the `createApiKey.py` script. This will generate a new API key and store it in `.env`.

```sh
python scripts/createApiKey.py
```

4. Verify the API user and key by running the `checkApiUser.py` script. This will confirm that the new user and key are valid.

```sh
python scripts/checkApiUser.py