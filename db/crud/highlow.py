import datetime

from db.init import db


def read(market):
    high_low_eos_ref = db.collection(u'HighLow-{}'.format(market))
    docs = high_low_eos_ref.stream()

    data = []
    min_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    for doc in docs:
        # if doc.id < min_date:
        #     continue
        print(doc.id)
        doc_dict = doc.to_dict()

        data += doc_dict["data_set"]

    return data


def insert(market, date, data_set):
    data = {
        u'data_set': data_set,
    }

    # db.collection(u'HighLow').document(u'{}'.format(market)).collection(u'{}'.format(date)).document().set(data)
    db.collection(u'HighLow-{}'.format(market)).document(u'{}'.format(date)).set(data)

    print("insert complete")
