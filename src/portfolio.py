from asset import Asset


class Portfolio:
    id = ""
    value = ""
    device = "EUR"
    assets = []

    def addasset(self, asset):
        self.assets.append(asset)

    def toString(self):
        assets = ""
        for asset in self.assets:
            assets.append(asset.tostring + "\n")
        return assets