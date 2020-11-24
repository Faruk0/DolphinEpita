from src.rest import RestQueries


class Asset:
    id = 0
    name = ""
    type = ""
    value = 0

    def __init__(self, id, name, type, value):
        self.id = id
        self.name = name
        self.type = type
        self.value = value

    def getinfo(self):
        return RestQueries.get("asset/" + str(self.id))

    def getattribute(self, attribute):
        return RestQueries.get("asset/" + str(self.id) + "/attribute/" + attribute)

    def toString(self):
        return "ID : " + str(self.id) + "\n" + \
               "Nom : " + self.name + "\n" + \
               "type : " + self.type
