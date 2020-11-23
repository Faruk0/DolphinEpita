class Asset:
    id = ""
    name = ""
    type = ""
    quantity = ""
    cost = ""
    amount = ""
    nav = ""

    def __init__(self, id, name, type, quantity, cost, amount, nav):
        self.id = id
        self.name = name
        self.type = type
        self.quantity = quantity
        self.cost = cost
        self.amount = amount
        self.nav = nav

    def tostring(self):
        return "id : " + self.id + "\n" + \
               "name : " + self.name + "\n" + \
               "type : " + self.type + "\n" + \
               "quantity : " + self.quantity + "\n" + \
               "cost : " + self.cost + "\n" + \
               "amount : " + self.amount + "\n" + \
               "%NAV : " + self.nav + "\n"
