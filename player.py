from dice import Dice
import pygame

BLACK = 0,0,0
tokenPoly = [[55.0, 61.0], [54.0, 61.0], [54.0, 53.0], [47.0, 29.0], [47.0, 29.0], [49.0, 27.0], [49.0, 26.0], [47.0, 24.0], [47.0, 24.0], [51.0, 14.0], [37.0, 0.0], [22.0, 14.0], [27.0, 24.0], [26.0, 24.0], [24.0, 26.0], [24.0, 27.0], [26.0, 29.0], [27.0, 29.0], [20.0, 53.0], [20.0, 61.0], [18.0, 61.0], [16.0, 63.0], [16.0, 68.0], [18.0, 70.0], [18.0, 70.0], [18.0, 74.0], [55.0, 74.0], [55.0, 70.0], [57.0, 68.0], [57.0, 63.0], [55.0, 61.0]]
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
        '''is player choosing their own token'''
        for token in self.allTokens:
            if x in token.tokenLocation[0] and y in token.tokenLocation[1]:
                return token
    
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
        for i in range(token.currentTilePathPosition,token.currentTilePathPosition+moveBy+1):
            tokenStepCoordinate = token.tokenTilesPath[i][0].endCoordinates
            # -5 is just for Dale to stop getting OCD centered token
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
                new_translated_token_path = [[x + token.xBaseCoord, token.yBaseCoord +y] for [x, y] in tokenPoly]
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
