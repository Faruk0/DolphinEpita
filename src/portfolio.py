import json

from myasset import Asset
from rest import RestQueries


def getportfoliobyid(id):
    return RestQueries.get("portfolio/" + str(id) + "/dyn_amount_compo")

class Portfolio:
    def __init__(self, id = 1830, currency="EUR", items = [],
                 label="EPITA_PTF_11", date="2016-06-01"):
        self.id = id
        self.value = 0.0
        self.currency = "EUR"
        self.items = []
        self.label = label
        self.date = date
        self.totSharpe = 0.0

    def additem(self, item):
        self.items.append(item)
        self.value += item.value
        self.totSharpe += item.sharpe

    def toString(self):
        result = ""
        for item in self.items:
            result = result + item.toString() + "\n"
        return result

    def getportfolio(self):
        return RestQueries.get("portfolio/" + str(self.id) + "/dyn_amount_compo")

    def checkNav(self):
        lowerNavs, greaterNavs = [], []
        for item in self.items:
            nav = item.value * item.qty
            if nav > self.value / 10:
                greaterNavs.append(item)
            elif nav < self.value / 100:
                lowerNavs.append(item)
        return lowerNavs, greaterNavs

    def lastTouch(self):
        outAssets = []
        for asset in self.items:
            qty = int(asset.qty)
            if (qty == 0) and (asset.sharpe < self.totSharpe / len(outAssets)) and len(outAssets) > 15:
                self.value -= asset.value
                self. totSharpe -=  asset.sharpe
                continue
            elif qty == 0:
                qty = 1

            outAssets.append({
                "asset" : {
                    "asset" : str(asset.id),
                    "quantity" : str(qty)}})
        return outAssets

    def putPortfolio(self, outAssets):
        body = {
            "label" : self.label,
            "currency" : {"code" : self.currency},
            "type" : "front",
            "values" : {self.date : outAssets}
        }
        res = RestQueries.put(f"portfolio/{self.id}/dyn_amount_compo",
                        json.dumps(body))
        return res
