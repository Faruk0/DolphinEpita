class Asset:
    id = 0
    name = ""
    type = ""

    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def tostring(self):
        return "ID : " + str(self.id) + "\n" + \
               "Nom : " + self.name + "\n" + \
               "type : " + self.type
