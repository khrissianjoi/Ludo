import random
class Dice:
    def __init__(self):
        self.diceValue = self.rollDice()

    def rollDice(self):
        return random.randint(1,7)

    def getdiceValue(self):
        return self.diceValue