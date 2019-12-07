import random

class Dice:
    def __init__(self):
        self.diceValue = self.rollDice()
        self.rollCount = 1
        self.coOrdinates = None

    def rollDice(self):
        value = random.randint(1,6)
        # self.setdiceValue()
        return 6

    def getdiceValue(self):
        return self.diceValue

    def setCoordinates(self,coOrdinates):
        self.coOrdinates = coOrdinates