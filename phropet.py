import pandas as pd
from fbprophet import Prophet


def get_predict(data):
    m = Prophet(
        changepoint_prior_scale=0.5,
        # seasonality
        # weekly_seasonality=10,
        # yearly_seasonality=20,
        # daily_seasonality=False
    )
    df = pd.DataFrame(data)
    df.columns = ["ds", "y"]

    m.fit(df)

    future = m.make_future_dataframe(periods=144, freq="10min")
    forecast = m.predict(future)

    forecast = forecast[-143:]
    forecast = forecast.sort_values(by=['yhat'], ascending=False)

    forecast.to_csv("filename.csv", encoding="utf-8")

    result = {
        "high": {
            "time": forecast.iloc[0]["ds"],
            "price": forecast.iloc[0]["yhat"],
        },
        "low": {
            "time": forecast.iloc[-1]["ds"],
            "price": forecast.iloc[-1]["yhat"],
        }
    }

    return result

