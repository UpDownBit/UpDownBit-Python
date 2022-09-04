from db.init import db


def read():
    high_low_eos_ref = db.collection(u'HighLow-EOS')
    docs = high_low_eos_ref.stream()

    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')


def insert(market, date, highs, lows):
    data = {
        u'highs': highs,
        u'lows': lows,
    }

    # db.collection(u'HighLow').document(u'{}'.format(market)).collection(u'{}'.format(date)).document().set(data)
    db.collection(u'HighLow-{}'.format(market)).document(u'{}'.format(date)).set(data)

    print("insert complete")
