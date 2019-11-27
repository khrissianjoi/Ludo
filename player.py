from dice import Dice
import pygame


colours = [(77, 5, 232, 1),(247, 202, 24, 1),(77, 5, 232, 1),(247, 202, 24, 1)]
class Player:
    def __init__(self,playerName,colour,tokensOnHome, tokensOnBase,tokenOnTrack):
        self.playerName = playerName
        self.colour = colour
        self.tokensOnHome = tokensOnHome
        self.tokensOnBase = tokensOnBase
        self.tokensOnTrack = tokenOnTrack

        self.myDice = Dice()

    def rollDice(self):
        return self.myDice.rollDice()

    def chooseToken(self):
        pass
    
    def getTokensOnTrack(self):
        return self.tokensOnTrack

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

    def drawTokens(self,refresh,otherThan,translated_token_path):
        for token in self.tokensOnBase:
            if token != otherThan:
                new_translated_token_path = [[x + token.xBaseCoord, token.yBaseCoord +y] for [x, y] in translated_token_path]
                pygame.draw.polygon(refresh.gameDisplay,self.colour,new_translated_token_path)