import datetime

from db.init import db


def insert_time(result, market):
    shoulder_time, knee_time = result["high"]["time"], result["low"]["time"]

    shoulder_time = shoulder_time - datetime.timedelta(minutes=540)
    knee_time = knee_time - datetime.timedelta(minutes=540)

    data = {
        u'shoulder_time': shoulder_time,
        u'knee_time': knee_time,
        u'shoulder_price': 0,
        u'knee_price': 0
    }

    today = datetime.datetime.now().strftime('%Y-%m-%d')

    db.collection(u'Predict-{}'.format(market)).document(u'{}'.format(today)).set(data)

    print("Insert Predict-{} Shoulder & Knee Time Complete...".format(market))
