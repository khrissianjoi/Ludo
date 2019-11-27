import pygame


tokenPoly = [[55.0, 61.0], [54.0, 61.0], [54.0, 53.0], [47.0, 29.0], [47.0, 29.0], [49.0, 27.0], [49.0, 26.0], [47.0, 24.0], [47.0, 24.0], [51.0, 14.0], [37.0, 0.0], [22.0, 14.0], [27.0, 24.0], [26.0, 24.0], [24.0, 26.0], [24.0, 27.0], [26.0, 29.0], [27.0, 29.0], [20.0, 53.0], [20.0, 61.0], [18.0, 61.0], [16.0, 63.0], [16.0, 68.0], [18.0, 70.0], [18.0, 70.0], [18.0, 74.0], [55.0, 74.0], [55.0, 70.0], [57.0, 68.0], [57.0, 63.0], [55.0, 61.0]]
class TokenCreate:
    def __init__(self, tokenNum,tokenColour, playerOwner, tokenLocation, baseCoord, tokenTilesPath, display = None):
        self.display = display
        self.tokenID = (tokenNum, tokenColour)
        self.playerOwner = playerOwner
        self.tokenLocation = tokenLocation
        # new
        self.xBaseCoord, self.yBaseCoord = baseCoord
        self.tokenTilesPath = tokenTilesPath
        self.currentTilePathPosition = 0

    def drawOtherPlayersTokens(self,otherPlayers,refresh):
        for player in otherPlayers:
            if player.colour == (189, 9, 9):
                print(len(player.tokensOnBase))
            # print("player.tokensOnBase {}: {}".format(player.colour,len(player.tokensOnBase)))
            for token in player.tokensOnTrack:
                
                new_translated_token_path = [[x + token.tokenLocation[0][0], token.tokenLocation[1][0] +y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay,player.colour,new_translated_token_path)
            # when other player is doing their turn all of the other player's tokens don't move
            for token in player.tokensOnBase:
                # print("player: {}, {}".format(player.colour,len(player.tokensOnBase)))
                new_translated_token_path = [[x + token.xBaseCoord, token.yBaseCoord+y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay,player.colour,new_translated_token_path)
            for token in player.tokensOnHome:
                new_translated_token_path = [[x + token.tokenLocation[0][0], token.tokenLocation[1][0] +y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay,player.colour,new_translated_token_path)
            
    def tokenNewTile(self,moveBy):
        return self.tokenTilesPath[self.currentTilePathPosition+moveBy][0]

    def moveToken(self,refresh,moveBy,otherPlayers):
        # tileNumber is the tile position in the list of the token path
        for i in range(self.currentTilePathPosition,self.currentTilePathPosition+moveBy+1):
            tokenStepCoordinate = self.tokenTilesPath[i][0].endCoordinates
            # -5 is just for Dale to stop getting OCD centered token
            translated_token_path = [[x + tokenStepCoordinate[0], tokenStepCoordinate[1] + y] for [x, y] in tokenPoly]
            pygame.draw.polygon(refresh.gameDisplay,self.tokenID[1],translated_token_path)
            self.playerOwner.drawTokens(refresh,self,tokenPoly)
            self.drawOtherPlayersTokens(otherPlayers,refresh)
            pygame.display.update()
            pygame.time.delay(300)
            refresh.regenerateBoard()
        self.currentTilePathPosition += moveBy
        

    def setPlayerOwner(self,player):
        self.playerOwner = player
    
    def setTokenLocation(self,newtokenLocation):
        self.tokenLocation = newtokenLocation

    def getLocation(self):
        return self.tokenLocation

    def setPlayerOwner(self, player):
        self.playerOwner = player

    def setLocation(self):
        pass

    def test(self):
        try:
            for i in range(0,len(self.tokenTilePath)):
                # print(self.tokenTilePath[i][0])
                current = self.tokenTilePath[i][0]
                pygame.draw.circle(self.display,self.tokenID[1],current.endCoordinates,10)
                pygame.display.update()
                pygame.time.delay(200)

        except Exception as e:
            print(e)
            pass