from dice import Dice
import pygame

BLACK = 0,0,0
tokenPoly = [[27.5, 30.5], [27.0, 30.5], [27.0, 26.5], [23.5, 14.5], [23.5, 14.5], [24.5, 13.5], [24.5, 13.0], [23.5, 12.0], [23.5, 12.0], [25.5, 7.0], [18.5, 0.0], [11.0, 7.0], [13.5, 12.0], [13.0, 12.0], [12.0, 13.0], [12.0, 13.5], [13.0, 14.5], [13.5, 14.5], [10.0, 26.5], [10.0, 30.5], [9.0, 30.5], [8.0, 31.5], [8.0, 34.0], [9.0, 35.0], [9.0, 35.0], [9.0, 37.0], [27.5, 37.0], [27.5, 35.0], [28.5, 34.0], [28.5, 31.5], [27.5, 30.5]]
class Player:
    def __init__(self,playerName,colour,tokensOnHome, tokensOnBase,tokenOnTrack, allTokens=None):
        self.playerName = playerName
        self.colour = colour
        self.tokensOnHome = tokensOnHome
        self.tokensOnBase = tokensOnBase
        self.tokensOnPath = tokenOnTrack
        self.allTokens = allTokens
        self.myDice = Dice()

    def setAllTokens(self,allTokens):
        self.allTokens = allTokens

    def rollDice(self):
        return self.myDice.rollDice()

    def chooseToken(self,x,y):
        '''checks if player choosing their own token'''
        for token in self.allTokens:
            if x in token.tokenLocation[0] and y in token.tokenLocation[1]:
                return token
        return None
    
    def getTokensOnPath(self):
        return self.tokensOnPath

    def getTokensOnBase(self):
        return self.tokensOnBase

    def getTokensOnHome(self):
        return self.tokensOnHome

    def addTokensToHome(self, token):
        self.rokensOnHome.append(token)

    def addTokensToBase(self, token):
        self.tokensOnBase.append(token)

    def addTokensToTrack(self, token):
        self.tokens.OnTrack(token)

    def moveChosenToken(self, refresh, token, moveBy, otherPlayers):
        '''Moves player's chosen token, while recreating the other tokens (including oponents players)'''
        for i in range(token.currentTilePathPosition+1,token.currentTilePathPosition+moveBy):
            tokenStepCoordinate = token.tokenTilesPath[i][0].endCoordinates

            translated_token_path = [[x + tokenStepCoordinate[0], tokenStepCoordinate[1] + y] for [x, y] in tokenPoly]
            token.moveOneToken(refresh,token.tokenID[1],translated_token_path)
            token.playerOwner.drawTokens(refresh,token,tokenPoly)
            token.drawOtherPlayersTokens(otherPlayers,refresh)
            pygame.display.update()
            pygame.time.delay(300)
            refresh.regenerateBoard()
        token.setCurrentTilePathPosition(moveBy)

    def drawTokens(self,refresh,otherThan,tokenPoly):
        for token in self.tokensOnBase:
            if token.tokenID != otherThan.tokenID:
                new_translated_token_path = [[x + token.xBaseCoord, token.yBaseCoord+y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay,self.colour,new_translated_token_path)
                pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path,1)
        # for token in self.tokensOnHome:
        #     if token != otherThan:
        #         new_translated_token_path = [[x + token.xBaseCoord, token.yBaseCoord +y] for [x, y] in translated_token_path]
        #         pygame.draw.polygon(refresh.gameDisplay,self.colour,new_translated_token_path)
        for token in self.tokensOnPath:
            if token.tokenID != otherThan.tokenID:
                new_translated_token_path = [[x + token.tokenLocation[0][0], token.tokenLocation[1][0] +y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay,self.colour,new_translated_token_path)
                pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path,1)
