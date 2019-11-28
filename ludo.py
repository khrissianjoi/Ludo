import pygame
import datetime
import copy

from board import Board
from player import Player

# team colours
TEAM_BLUE1 = 209,230,238 #dark
TEAM_BLUE2 = 65, 179, 226 #light
BLUE_TOKEN = 77, 5, 232, 1

TEAM_YELLOW1 = 200,189,161
TEAM_YELLOW2 = 251, 217, 132
YELLOW_TOKEN = 247, 202, 24, 1

TEAM_RED1 = 245,221,219
TEAM_RED2 = 241, 120, 107
RED_TOKEN = 189,9,9

TEAM_GREEN1 = 190,235,224
TEAM_GREEN2 = 90, 200, 174
GREEN_TOKEN = 30, 130, 76, 1

class Game:
    def __init__(self):
        self.startTime = datetime.datetime.now()
        self.endTime = None
        self.gameExit = False

        self.players = None

        self.playerRed = None
        self.playerBlue = None
        self.playerGreen = None
        self.playerYellow = None

        self.board = None
        self.currentPlayer = None

    def endGame(self):
        self.endTime = datetime.datetime.now()
        self.gameExit = True

    def isPlayerChoosingOwnToken(self,x,y):
        return self.currentPlayer.chooseToken(x,y)

    def createPlayers(self):
        self.playerRed = Player("Dale",RED_TOKEN,[],self.board.redTokens,[], self.board.redTokens)

        for token in self.board.redTokens:
            token.setPlayerOwner(self.playerRed)

        self.playerYellow = Player("John",YELLOW_TOKEN,[],self.board.yellowTokens,[], self.board.yellowTokens)

        for token in self.board.yellowTokens:
            token.setPlayerOwner(self.playerYellow)

        self.playerBlue = Player("Alex",BLUE_TOKEN,[],self.board.blueTokens,[], self.board.blueTokens)

        for token in self.board.blueTokens:
            token.setPlayerOwner(self.playerBlue)

        self.playerGreen = Player("Joi",GREEN_TOKEN,[],self.board.greenTokens,[], self.board.greenTokens)
        
        for token in self.board.greenTokens:
            token.setPlayerOwner(self.playerGreen)

        self.players = [self.playerRed,self.playerBlue,self.playerGreen,self.playerYellow]


    def main(self):
        pygame.init()

        self.board = Board()
        self.board.createBoard()

        self.createPlayers()

        # counter = 0
        while not self.gameExit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.endGame()
                    if event.type == pygame.MOUSEBUTTONUP:
                        # so it doesn't index out of range
                        # self.currentPlayer = self.players[counter % 4]
                        # print("Turn: {}".format(self.currentPlayer.colour))
                        x,y = pygame.mouse.get_pos()
                        print(x,y)
        #                 currentRoll = self.currentPlayer.rollDice()
        #                 currentToken = self.isPlayerChoosingOwnToken(x,y)
        #                 if currentToken:
        #                     # if currentToken.currentTilePathPosition == -1 it's in base
        #                     if currentToken.currentTilePathPosition > 0:
        #                         # TODO: fix this tuple
        #                         currentTilePosition = currentToken.tokenTilesPath[currentToken.currentTilePathPosition][0]
        #                         currentTilePosition.residents.remove(currentToken)
        #                     newTokenTilePosition = currentToken.tokenNewTile(currentRoll)
        #                     if newTokenTilePosition.tileType == 'path' or newTokenTilePosition.tileType == 'safe':
        #                         if currentToken not in self.currentPlayer.tokensOnPath:
        #                             self.currentPlayer.tokensOnPath.append(currentToken)
        #                             if currentToken in self.currentPlayer.tokensOnBase:
        #                                 self.currentPlayer.tokensOnBase.remove(currentToken)
        #                             elif currentToken in self.currentPlayer.tokensOnHome:
        #                                 self.currentPlayer.tokensOnHome.remove(currentToken)
        #                     elif newTokenTilePosition.tileType == 'base':
        #                         if currentToken not in self.currentPlayer.tokensOnBase:
        #                             self.currentPlayer.tokensOnBase.append(currentToken)
        #                             if currentToken in self.currentPlayer.tokensOnHome:
        #                                 self.currentPlayer.tokensOnHome.remove(currentToken)
        #                             elif currentToken in self.currentPlayer.tokensOnPath:
        #                                 self.currentPlayer.tokensOnPath.remove(currentToken)

        #                     elif newTokenTilePosition.tileType == 'home':
        #                         if currentToken not in self.currentPlayer.tokensOnHome:
        #                             self.currentPlayer.tokensOnHome.append(currentToken)
        #                             if currentToken in self.currentPlayer.tokensOnPath:
        #                                 self.currentPlayer.tokensOnPath.remove(currentToken)
        #                             elif currentToken in self.currentPlayer.tokensOnBase:
        #                                 self.currentPlayer.tokensOnBase.remove(currentToken)
        #                     # TODO: remove to from previous tile
        #                     newTokenTilePosition.residents.append(currentToken)
        #                     self.updateBoardWithMovingToken(currentToken,currentRoll,newTokenTilePosition)

        #                     counter += 1
        #                     print("Next: {}".format(self.players[counter%4].colour))

        #                 else:
        #                     print("Player did not pick their own token")
        pygame.quit()
        quit()

    def updateBoardWithMovingToken(self,currentToken,currentRoll,newTokenTilePosition):
        tempPlayers = copy.copy(self.players)
        tempPlayers.remove(self.currentPlayer)        
        self.currentPlayer.moveChosenToken(self.board,currentToken,currentRoll,tempPlayers)
        currentToken.setTokenLocation(newTokenTilePosition.rangeCoordinates)
        self.currentPlayer.setAllTokens(self.currentPlayer.tokensOnBase+self.currentPlayer.tokensOnPath+self.currentPlayer.tokensOnHome)

playing = Game()
playing.main()
