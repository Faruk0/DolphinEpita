import json

from src.myasset import Asset
from src.portfolioItem import PortfolioItem
from src.rest import RestQueries

class Portfolio:
    id = 0
    value = ""
    device = "EUR"
    items = []

    def additem(self, item):
        self.items.append(item)

    def toString(self):
        result = ""
        for item in self.items:
            result = result + item.tostring() + "\n"
        return result

    def getportfolio(self, id):
        return RestQueries.get("portfolio/" + str(id) + "/dyn_amount_compo")


pf = Portfolio()

ourpf = pf.getportfolio(1830)
with open('portfolio.txt', 'w') as outfile:
    json.dump(ourpf, outfile)

pfref = pf.getportfolio(2201)
with open('ref.txt', 'w') as outfile:
    json.dump(pfref, outfile)
