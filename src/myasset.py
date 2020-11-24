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

    def toString(self):
        return "ID : " + str(self.id) + "\n" + \
               "Nom : " + self.name + "\n" + \
               "type : " + self.type
