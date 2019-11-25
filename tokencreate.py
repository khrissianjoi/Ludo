import pygame
class TokenCreate:
    def __init__(self, tokenNum,tokenColour, playerOwner, tokenLocation, baseCoord, tokenPoly, tokenTilePath=None, display = None):
        self.display = display
        self.tokenID = (tokenNum, tokenColour)
        self.playerOwner = playerOwner
        self.tokenLocation = tokenLocation

        # new
        self.tokenPoly = tokenPoly
        self.xBaseCoord, self.yBaseCoord = baseCoord
        self.tokenTilePath = tokenTilePath

    def moveToken(self):
        for i in range(0,6):
            test = self.tokenTilePath[i][0].endCoordinates
            translated_token_path = [[x - 605 + test[0], test[1] + y - 320] for [x, y] in self.tokenPoly]
            pygame.draw.polygon(self.display,(189,9,9),translated_token_path)
            pygame.display.update()
            pygame.time.delay(400)

    def getLocation(self):
        return self.tokenLocation

    def setPlayerOwner(self, player):
        self.playerOwner = player

    def setLocation(self):
        pass

    def test(self):
        try:
            i = 0
            while i < len(self.tokenTilePath)-1:
                # print(self.tokenTilePath[i][0])
                current = self.tokenTilePath[i][0]
                pygame.draw.circle(self.display,(189,9,9),current.endCoordinates,10)
                pygame.display.update()
                pygame.time.delay(200)
                i+=1
        except Exception as e:
            print(e)
            pass