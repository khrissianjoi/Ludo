class TokenCreate:
    def __init__(self, tokenNum,tokenColour, playerOwner, tokenLocation, baseCoord, tokenPath):
        self.tokenID = (tokenNum, tokenColour)
        self.playerOwner = playerOwner
        self.tokenLocation = tokenLocation

        # new
        self.tokenPath = tokenPath
        self.xBaseCoord, self.yBaseCoord = baseCoord

    def getLocation(self):
        return self.tokenLocation

    def setPlayerOwner(self, player):
        self.playerOwner = player
        
    def setLocation(self):
        pass