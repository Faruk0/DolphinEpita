from src.rest import RestQueries


class Asset:
    id = 0
    name = ""
    type = ""
    value = 0

    def __init__(self, id, name, type, value, sharpe=0):
        self.id = id
        self.name = name
        self.type = type
        self.value = value
        self.sharpe = sharpe

    def getinfo(self):
        return RestQueries.get("asset/" + str(self.id))

    def getattribute(self, attribute):
        return RestQueries.get("asset/" + str(self.id) + "/attribute/" + attribute)

    def getcotation(self):
        return RestQueries.get("/asset/" + str(self.id) + "/quote")

    def toString(self):
        return "ID : " + str(self.id) + "\n" + \
               "Nom : " + self.name + "\n" + \
               "Type : " + self.type + "\n" + \
               "Sharpe : " + self.sharpe
