class Player:
    def __init__(self, username):
        self.username = username
        self.chips = 10000
    
    def addChips(self, delta):
        self.setChips(self.getChips() + delta)

    def getChips(self):
        return self.chips
    
    def setChips(self, val):
        self.chips = val

    def __repr__(self):
        return self.username


class Chip:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value



    
    



