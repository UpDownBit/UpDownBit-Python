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

        data_tmp = res.json()

        for dt in data_tmp:
            insert_data = {
                "price": dt["trade_price"],
                "time": dt["candle_date_time_kst"],
            }

            result.append(insert_data)

        print("{}(UST) Finished.....".format(target_time))

        time.sleep(0.1)

    return result
