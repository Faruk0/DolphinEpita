class Asset:
    id = ""
    name = ""
    type = ""
    quantity = ""
    cost = ""
    amount = ""
    nav = ""

    def tostring(self):
        return "id : " + self.id + \
            " name : " + self.name + \
            " type : " + self.type + \
            " quantity : " + self.quantity + \
            " cost : " + self.cost + \
            " amount : " + self.amount +\
            " %NAV : " + self.nav