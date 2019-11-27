import pygame
import datetime

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

    def endGame(self):
        self.endTime = datetime.datetime.now()
        self.gameExit = True

    def main(self):
        pygame.init()

        ludo = Board()
        ludo.createBoard()

        playerRed = Player("Dale",RED_TOKEN,[],ludo.redTokens,[])
        for token in ludo.redTokens:
            token.setPlayerOwner(playerRed)
        playerYellow = Player("John",YELLOW_TOKEN,[],ludo.yellowTokens,[])
        playerBlue = Player("Alex",BLUE_TOKEN,[],ludo.blueTokens,[])
        playerGreen = Player("Joi",GREEN_TOKEN,[],ludo.greenTokens,[])
        players = [playerRed,playerYellow,playerBlue,playerGreen]

        testPlayer = players[0]

        while not self.gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    print(x,y)
                    # for tile in ludo.tiles:
                    #     if x in ludo.tiles[tile][0] and y in ludo.tiles[tile][1]:
                    #         print("x : {}, y : {}, type: {}".format(x,y,tile.tileType))
                    #         break
                        
                    currentRoll = testPlayer.rollDice()
                    currentToken = ludo.redTokens[0] #selectedToken
                    for token in ludo.redTokens:
                        if x in token.tokenLocation[0] and y in token.tokenLocation[1]:
                            currentToken = token
                            break

                    if x in currentToken.tokenLocation[0] and y in currentToken.tokenLocation[1]:
                        # TODO: get rid of tuple and keep only index [0] (below)
                        # -> index[1] is a counter I previously needed
                        newTokenTilePosition = currentToken.moveToken(ludo,currentRoll)[0]
                        # set new location of token
                        currentToken.setTokenLocation(newTokenTilePosition.rangeCoordinates)

                        # TODO: need to do this for all tile types
                        if newTokenTilePosition.tileType == 'path':
                        #     # TODO: change tokenOnTrack to tokenOnPath for consistency
                            if newTokenTilePosition not in testPlayer.tokensOnTrack:
                                testPlayer.tokensOnTrack.append(currentToken)
                                # TODO: remove token if its in the home or base player list
                        elif newTokenTilePosition.tileType == 'base':
                            if newTokenTilePosition not in testPlayer.tokensOnBase:
                                testPlayer.tokensOnBase.append(currentToken)
                        elif newTokenTilePosition.tileType == 'home':
                            if newTokenTilePosition not in testPlayer.tokensOnHome:
                                testPlayer.tokensOnHome.append(currentToken)

        pygame.quit()
        quit()

playing = Game()
playing.main()
