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

    def endGame(self):
        self.endTime = datetime.datetime.now()
        self.gameExit = True

    def isPlayerChoosingOwnToken(self, currentPlayer,x,y):
        for token in currentPlayer.allTokens:
            if x in token.tokenLocation[0] and y in token.tokenLocation[1]:
                return token

    def createPlayers(self,ludo):
        self.playerRed = Player("Dale",RED_TOKEN,[],ludo.redTokens,[], ludo.redTokens)

        for token in ludo.redTokens:
            token.setPlayerOwner(self.playerRed)

        self.playerYellow = Player("John",YELLOW_TOKEN,[],ludo.yellowTokens,[], ludo.yellowTokens)

        for token in ludo.yellowTokens:
            token.setPlayerOwner(self.playerYellow)

        self.playerBlue = Player("Alex",BLUE_TOKEN,[],ludo.blueTokens,[], ludo.blueTokens)

        for token in ludo.blueTokens:
            token.setPlayerOwner(self.playerBlue)

        self.playerGreen = Player("Joi",GREEN_TOKEN,[],ludo.greenTokens,[], ludo.greenTokens)
        
        for token in ludo.greenTokens:
            token.setPlayerOwner(self.playerGreen)

        self.players = [self.playerRed,self.playerYellow,self.playerBlue,self.playerGreen]

    def main(self):
        pygame.init()

        ludo = Board()
        ludo.createBoard()

        self.createPlayers(ludo)

        counter = 0
        while not self.gameExit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.endGame()
                    if event.type == pygame.MOUSEBUTTONUP:
                        # so it doesn't index out of range
                        currentPlayer = self.players[counter % 4]
                        print("Turn: {}".format(currentPlayer.colour))
                        x,y = pygame.mouse.get_pos()
                        print(x,y)
                        currentRoll = currentPlayer.rollDice()
                        currentToken = self.isPlayerChoosingOwnToken(currentPlayer,x,y)
                        
                        if currentToken:
                            newTokenTilePosition = currentToken.tokenNewTile(currentRoll)

                            if newTokenTilePosition.tileType == 'path' or newTokenTilePosition.tileType == 'safe':
                            #     # TODO: change tokenOnTrack to tokenOnPath for consistency
                                if currentToken not in currentPlayer.tokensOnTrack:
                                    currentPlayer.tokensOnTrack.append(currentToken)
                                    if currentToken in currentPlayer.tokensOnBase:
                                        currentPlayer.tokensOnBase.remove(currentToken)
                                    elif currentToken in currentPlayer.tokensOnHome:
                                        currentPlayer.tokensOnHome.remove(currentToken)
                            elif newTokenTilePosition.tileType == 'base':
                                if currentToken not in currentPlayer.tokensOnBase:
                                    currentPlayer.tokensOnBase.append(currentToken)
                                    if currentToken in currentPlayer.tokensOnHome:
                                        currentPlayer.tokensOnHome.remove(currentToken)
                                    elif currentToken in currentPlayer.tokensOnTrack:
                                        currentPlayer.tokensOnTrack.remove(currentToken)

                            elif newTokenTilePosition.tileType == 'home':
                                if currentToken not in currentPlayer.tokensOnHome:
                                    currentPlayer.tokensOnHome.append(currentToken)
                                    if currentToken in currentPlayer.tokensOnTrack:
                                        currentPlayer.tokensOnTrack.remove(currentToken)
                                    elif currentToken in currentPlayer.tokensOnBase:
                                        currentPlayer.tokensOnBase.remove(currentToken)

                            tempPlayers = copy.copy(self.players)
                            tempPlayers.remove(currentPlayer)        
                            currentToken.moveToken(ludo,currentRoll,tempPlayers)
                            currentToken.setTokenLocation(newTokenTilePosition.rangeCoordinates)

                            # currentPlayer.allTokens.append(currentToken)
                            currentPlayer.setAllTokens(currentPlayer.tokensOnBase+currentPlayer.tokensOnTrack+currentPlayer.tokensOnHome)

                            counter += 1
                            print("Next: {}".format(self.players[counter%4].colour))
                        else:
                            print("Player did not pick their own token")

        pygame.quit()
        quit()

playing = Game()
playing.main()
