from fastapi import APIRouter

from db.crud import highlow
from phropet import get_predict


router = APIRouter()


@router.get("/prophet_predict/{market}")
def get_candles_ten_minutes(market):
    docs = highlow.read(market)
    result = get_predict(docs)

    return result
