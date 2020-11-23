class Asset:
    id = 0
    name = ""
    type = ""
    quantity = 0
    cost = 0
    amount = 0
    nav = 0

    def __init__(self, id, name, type, quantity, cost, amount, nav):
        self.id = id
        self.name = name
        self.type = type
        self.quantity = quantity
        self.cost = cost
        self.amount = amount
        self.nav = nav

    def tostring(self):
        return "id : " + str(self.id) + "\n" + \
               "name : " + self.name + "\n" + \
               "type : " + self.type + "\n" + \
               "quantity : " + str(self.quantity) + "\n" + \
               "cost : " + str(self.cost) + "\n" + \
               "amount : " + str(self.amount) + "\n" + \
               "%NAV : " + str(self.nav) + "\n"
