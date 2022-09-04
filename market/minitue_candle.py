from dotenv import dotenv_values

import time
import datetime
import requests

config = dotenv_values(".env")


def refine_ten_minute_candle(market, date):
    headers = {"Accept": "application/json"}

    kst = "{} 00:00:00".format(date)
    datetime_format = "%Y-%m-%d %H:%M:%S"
    datetime_result = datetime.datetime.strptime(kst, datetime_format)
    utc = datetime_result - datetime.timedelta(hours=8)

    result = []

    for i in range(24):
        target_time = utc + datetime.timedelta(hours=i)

        res = requests.get(
            config.get("UPBIT_SERVER_URL") + '/v1/candles/minutes/10?market={}&to={}&count=6'.format(market,
                                                                                                     target_time),
            headers=headers
        )

        result += res.json()

        print("{}(UST) Finished.....".format(target_time))

        time.sleep(0.1)

    result = sorted(result, key=lambda x: x["trade_price"])
    highs_tmp, lows_tmp = result[-5:], result[:5]
    highs, lows = [], []

    for i in range(5):
        highs.append({"time": highs_tmp[0]["candle_date_time_kst"], "price": highs_tmp[0]["trade_price"]})
        lows.append({"time": lows_tmp[0]["candle_date_time_kst"], "price": lows_tmp[0]["trade_price"]})

    return highs, lows
