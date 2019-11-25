from dice import Dice

class Player:
    def __init__(self,playerName,colour,tokensOnHome, tokensOnBase,tokenOnTrack):
        self.playerName = playerName
        self.colour = colour
        self.tokensOnHome = tokensOnHome
        self.tokensOnBase = tokensOnBase
        self.tokenOnTrack = tokenOnTrack

        self.myDice = Dice()

    def rollDice(self):
        return self.myDice.rollDice()

    def chooseToken(self):
        pass
    
    def getTokensOnTrack(self):
        return self.tokenOnTrack

    def getTokensOnBase(self):
        return self.tokenOnBase

    def getTokensOnHome(self):
        return self.tokensOnHome

    def addTokensToHome(self, token):
        self.rokensOnHome.append(token)

    def addTokensToBase(self, token):
        self.tokensOnBase.append(token)

    def addTokensToTrack(self, token):
        self.tokens.OnTrack(token)
