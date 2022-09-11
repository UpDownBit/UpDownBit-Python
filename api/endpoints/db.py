from fastapi import APIRouter

from db.crud import highlow, predict
from phropet import get_predict


router = APIRouter()


@router.get("/prophet_predict/{market}")
def prophet_predict(market):
    data = highlow.read(market)
    result = get_predict(data)
    predict.insert_time(result, market)

    return result
