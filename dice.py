import random

class Dice:
    def __init__(self):
        self.diceValue = self.rollDice()

    def rollDice(self):
        value = random.randint(1,7)
        self.setdiceValue()
        return value

    def getdiceValue(self):
        return self.diceValue

    def setdiceValue(self):
        self.diceValue += 1
