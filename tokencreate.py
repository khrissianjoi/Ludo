import pygame


BLACK = 0, 0, 0
tokenPoly = [[27.5, 30.5], [27.0, 30.5], [27.0, 26.5], [23.5, 14.5], [23.5, 14.5], [24.5, 13.5], [24.5, 13.0], [23.5, 12.0], [23.5, 12.0], [25.5, 7.0], [18.5, 0.0], [11.0, 7.0], [13.5, 12.0], [13.0, 12.0], [12.0, 13.0], [12.0, 13.5], [13.0, 14.5], [13.5, 14.5], [10.0, 26.5], [10.0, 30.5], [9.0, 30.5], [8.0, 31.5], [8.0, 34.0], [9.0, 35.0], [9.0, 35.0], [9.0, 37.0], [27.5, 37.0], [27.5, 35.0], [28.5, 34.0], [28.5, 31.5], [27.5, 30.5]]


class TokenCreate:
    def __init__(self, tokenNum, tokenColour, playerOwner, tokenLocation, baseCoord, tokenTilesPath, homeCoord):
        self.display = None
        self.tokenID = (tokenNum, tokenColour)
        self.playerOwner = playerOwner
        self.tokenLocation = tokenLocation
        self.xBaseCoord, self.yBaseCoord = baseCoord
        self.xHomeCoord, self.yHomeCoord = homeCoord
        self.tokenTilesPath = tokenTilesPath
        self.currentTilePathPosition = 0

    def drawOtherPlayersTokens(self, otherPlayers, refresh):
        for player in otherPlayers:
            for token in player.tokensOnPath:
                new_translated_token_path = [[x + token.tokenLocation[0][0], token.tokenLocation[1][0] + y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay, player.colour, new_translated_token_path)
                pygame.draw.polygon(refresh.gameDisplay,  BLACK, new_translated_token_path, 1)
            # when other player is doing their turn all of the other player's tokens don't move
            for token in player.tokensOnBase:
                new_translated_token_path = [[x + token.xBaseCoord, token.yBaseCoord+y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay, player.colour, new_translated_token_path)
                pygame.draw.polygon(refresh.gameDisplay,  BLACK, new_translated_token_path, 1)
            for token in player.tokensOnHome:
                new_translated_token_path = [[x*0.85 + token.xHomeCoord, token.yHomeCoord + y*0.85] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay, player.colour, new_translated_token_path)
                pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path, 1)

    def tokenNewTile(self, moveBy):
        return self.tokenTilesPath[self.currentTilePathPosition + moveBy][0]

    def moveOneToken(self, refresh, colour, path):
        pygame.draw.polygon(refresh.gameDisplay, colour, path)
        pygame.draw.polygon(refresh.gameDisplay, BLACK,  path, 1)

    def setCurrentTilePathPosition(self, moveBy):
        if moveBy != 0:
            self.currentTilePathPosition += moveBy
        else:
            self.currentTilePathPosition = moveBy

    def drawTokenOnHome(self, refresh, currentPos, moveBy, otherPlayers):
        for i in range(currentPos, moveBy+currentPos):
            tokenStepCoordinate = self.tokenTilesPath[i][0].endCoordinates
            translated_token_path = [[x + tokenStepCoordinate[0], tokenStepCoordinate[1] + y] for [x, y] in tokenPoly]
            self.moveOneToken(refresh, self.tokenID[1], translated_token_path)
            self.playerOwner.drawTokens(refresh, self, tokenPoly)
            self.drawOtherPlayersTokens(otherPlayers, refresh)
            pygame.display.update()
            pygame.time.delay(300)
            refresh.regenerateBoard()
        translated_token_path = [[x*0.85 + self.xHomeCoord, y*0.85 + self.yHomeCoord] for [x, y] in tokenPoly]
        pygame.draw.polygon(refresh.gameDisplay, self.tokenID[1], translated_token_path)
        pygame.draw.polygon(refresh.gameDisplay, BLACK, translated_token_path, 1)
        self.playerOwner.drawTokens(refresh, self, tokenPoly)
        self.drawOtherPlayersTokens(otherPlayers, refresh)

    def setPlayerOwner(self, player):
        self.playerOwner = player

    def setTokenLocation(self, newtokenLocation):
        self.tokenLocation = newtokenLocation

    def getLocation(self):
        return self.tokenLocation

    def setPlayerOwner(self, player):
        self.playerOwner = player

    def drawToken(self, refresh):
        if self.tokenTilesPath[self.currentTilePathPosition] == 0:
            new_translated_token_path = [[x + self.tokenLocation[0][0], self.tokenLocation[1][0] + y] for [x, y] in tokenPoly]
            pygame.draw.polygon(refresh.gameDisplay, self.tokenID[1], new_translated_token_path)
            pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path, 1)
        elif self.tokenTilesPath[self.currentTilePathPosition][0].tileType != "home" and self.tokenLocation is not None:
            new_translated_token_path = [[x + self.tokenLocation[0][0], self.tokenLocation[1][0] + y] for [x, y] in tokenPoly]
            pygame.draw.polygon(refresh.gameDisplay, self.tokenID[1], new_translated_token_path)
            pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path, 1)
        elif self.tokenLocation is None:
            translated_token_path = [[x*0.85 + self.xHomeCoord, y*0.85 + self.yHomeCoord] for [x, y] in tokenPoly]
            pygame.draw.polygon(refresh.gameDisplay, self.tokenID[1], translated_token_path)
            pygame.draw.polygon(refresh.gameDisplay, BLACK, translated_token_path, 1)
