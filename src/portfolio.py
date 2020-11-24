from src.myasset import Asset
from src.portfolioItem import PortfolioItem
from src.rest import RestQueries


def getportfoliobyid(id):
    return RestQueries.get("portfolio/" + str(id) + "/dyn_amount_compo")

class Portfolio:
    id = 1830
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

    def getportfolio(self):
        return RestQueries.get("portfolio/" + str(self.id) + "/dyn_amount_compo")
