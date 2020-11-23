from myasset import Asset


class Portfolio:
    id = ""
    value = ""
    device = "EUR"
    assets = []

    def addasset(self, asset):
        self.assets.append(asset)

    def toString(self):
        result = ""
        for asset in self.assets:
            result = result + asset.tostring() + "\n"
        return result


pf = Portfolio()
as1 = Asset("1", "test", "action", "60", "3000", "50", "10%")
as2 = Asset("2", "test2", "obligation", "80", "300", "500", "50%")
pf.addasset(as1)
print(pf.toString())
pf.addasset(as2)
print(pf.toString())
