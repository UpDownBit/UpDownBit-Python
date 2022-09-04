from fastapi import APIRouter

from market import minitue_candle
from db.crud import highlow


router = APIRouter()


@router.get("/candles_ten_minutes/{market}/{date}")
def get_candles_ten_minutes(market, date):
    highs, lows = minitue_candle.refine_ten_minute_candle(market, date)

    highlow.insert(market, date, highs, lows)

    return None
