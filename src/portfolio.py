from myasset import Asset
from portfolioItem import PortfolioItem

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


pf = Portfolio()
as1 = Asset(1, "nom1", "action")
pfi1 = PortfolioItem(as1, 60, 3000, 50, 10)
as2 = Asset(2, "nom2", "obligation")
pfi2 = PortfolioItem(as2, 80, 300, 500, 50)
pf.additem(pfi1)
print(pf.toString())
pf.additem(pfi2)
print(pf.toString())
