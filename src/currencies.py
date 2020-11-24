from rest import RestQueries
import json

class Currencies:
    rates = {"EUR" : 1}

    def addCur(curName):
        if not curName in Currencies.rates:
            res = RestQueries.get("currency/rate/" + curName + "/to/EUR")
            value = float(res["rate"]["value"].replace(",", "."))
            Currencies.rates[curName] = value

    def dump():
        for key, value in Currencies.rates.items():
            print(key, value)
