from fastapi import APIRouter
from dotenv import dotenv_values
import requests

from utils import get_upbit_token

router = APIRouter()
config = dotenv_values(".env")


@router.get("/accounts")
def get_my_account_info():
    headers = get_upbit_token()

    res = requests.get(config.get("UPBIT_SERVER_URL") + '/v1/accounts', headers=headers)
    return res.json()


@router.get("/candles_ten_minutes")
def get_candles_ten_minutes():
    headers = {"Accept": "application/json"}

    res = requests.get(config.get("UPBIT_SERVER_URL") + '/v1/candles/minutes/1?market=KRW-ADA&to=2022-09-01 12:00:00&count=2', headers=headers)
    return res.json()
