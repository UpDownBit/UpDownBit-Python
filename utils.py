from dotenv import dotenv_values
import jwt
import uuid


def get_upbit_token():
    config = dotenv_values(".env")

    access_key = config.get("UPBIT_ACCESS_KEY")
    secret_key = config.get("UPBIT_SECRET_KEY")

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
        'Authorization': authorization,
    }

    return headers
