from myasset import Asset


class PortfolioItem:
    asset = None
    qty = 0
    cours = 0
    montant = 0
    nav = 0

    def __init__(self, asset, qty, cours, montant, nav):
        self.asset = asset
        self.qty = qty
        self.cours = cours
        self.montant = montant
        self.nav = nav

    def tostring(self):
        return self.asset.tostring() + "\n" + \
                  "Quantity : " + str(self.qty) + "\n" + \
                  "Cours : " + str(self.cours) + "\n" + \
                  "Montant : " + str(self.montant) + "\n" + \
                  "%NAV : " + str(self.nav) + "\n"
