import pygame

class TokenCreate:
    def __init__(self, tokenNum,tokenColour, playerOwner, tokenLocation, baseCoord, tokenTilesPath, display = None):
        self.display = display
        self.tokenID = (tokenNum, tokenColour)
        self.playerOwner = playerOwner
        self.tokenLocation = tokenLocation
        # new
        self.xBaseCoord, self.yBaseCoord = baseCoord
        self.tokenPoly =  [[55.0, 61.0], [54.0, 61.0], [54.0, 53.0], [47.0, 29.0], [47.0, 29.0], [49.0, 27.0], [49.0, 26.0], [47.0, 24.0], [47.0, 24.0], [51.0, 14.0], [37.0, 0.0], [22.0, 14.0], [27.0, 24.0], [26.0, 24.0], [24.0, 26.0], [24.0, 27.0], [26.0, 29.0], [27.0, 29.0], [20.0, 53.0], [20.0, 61.0], [18.0, 61.0], [16.0, 63.0], [16.0, 68.0], [18.0, 70.0], [18.0, 70.0], [18.0, 74.0], [55.0, 74.0], [55.0, 70.0], [57.0, 68.0], [57.0, 63.0], [55.0, 61.0]]
        self.tokenTilesPath = tokenTilesPath
        self.currentTilePathPosition = 5

    def moveToken(self,refresh,moveBy):
        # refresh = refresh.gameDisplay
        # tileNumber is the tile position in the list of the token path
        for i in range(self.currentTilePathPosition,self.currentTilePathPosition+moveBy+1):
            test = self.tokenTilesPath[i][0].endCoordinates
            # -5 is just for Dale to stop getting OCD centered token
            translated_token_path = [[x + test[0]-5, test[1] + y-5] for [x, y] in self.tokenPoly]
            pygame.draw.polygon(refresh.gameDisplay,(189,9,9),translated_token_path)
            self.playerOwner.drawTokens(refresh,self,self.tokenPoly)
            pygame.display.update()
            pygame.time.delay(400)
            refresh.regenerateBoard()
        self.currentTilePathPosition += moveBy
        return self.tokenTilesPath[self.currentTilePathPosition]

    def setPlayerOwner(self,player):
        self.playerOwner = player
    
    def setTokenLocation(self,newtokenLocation):
        self.tokenLocation = newtokenLocation

    def getLocation(self):
        return self.tokenLocation

    def setPlayerOwner(self, player):
        self.playerOwner = player

    # def drawToken(self)

    def setLocation(self):
        pass

    def test(self):
        try:
            for i in range(0,len(self.tokenTilePath)):
                # print(self.tokenTilePath[i][0])
                current = self.tokenTilePath[i][0]
                pygame.draw.circle(self.display,(189,9,9),current.endCoordinates,10)
                pygame.display.update()
                pygame.time.delay(200)

        except Exception as e:
            print(e)
            pass