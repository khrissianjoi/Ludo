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

    def endGame(self):
        self.endTime = datetime.datetime.now()
        self.gameExit = True



    def main(self):
        pygame.init()

        ludo = Board()
        ludo.createBoard()

        playerRed = Player("Dale",RED_TOKEN,[],ludo.redTokens,[], ludo.redTokens)

        for token in ludo.redTokens:
            token.setPlayerOwner(playerRed)

        playerYellow = Player("John",YELLOW_TOKEN,[],ludo.yellowTokens,[], ludo.yellowTokens)

        for token in ludo.yellowTokens:
            token.setPlayerOwner(playerYellow)

        playerBlue = Player("Alex",BLUE_TOKEN,[],ludo.blueTokens,[], ludo.blueTokens)

        for token in ludo.blueTokens:
            token.setPlayerOwner(playerBlue)

        playerGreen = Player("Joi",GREEN_TOKEN,[],ludo.greenTokens,[], ludo.greenTokens)
        
        for token in ludo.greenTokens:
            token.setPlayerOwner(playerGreen)

        players = [playerRed,playerYellow,playerBlue,playerGreen]


        # testPlayer = players
        counter = 0
        while not self.gameExit:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.endGame()
                    if event.type == pygame.MOUSEBUTTONUP:
                        # so it doesn't index out of range
                        currentPlayer = players[counter % 4]
                        print("Turn: {}".format(currentPlayer.colour))
                        x,y = pygame.mouse.get_pos()
                        print(x,y)

                        currentRoll = currentPlayer.rollDice()
                        currentToken = None
                        for token in currentPlayer.allTokens: 
                            if x in token.tokenLocation[0] and y in token.tokenLocation[1]:
                                currentToken = token
                                break

                        if currentToken:
                            if x in currentToken.tokenLocation[0] and y in currentToken.tokenLocation[1]:
                                tempPlayers = copy.copy(players)
                                tempPlayers.remove(currentPlayer)                                
                                # TODO: get rid of tuple and keep only index [0] (below)
                                # -> index[1] is a counter I previously needed
                                newTokenTilePosition = currentToken.moveToken(ludo,currentRoll,tempPlayers)[0]
                                currentToken.setTokenLocation(newTokenTilePosition.rangeCoordinates)

                                # TODO: need to do this for all tile types
                                if newTokenTilePosition.tileType == 'path':
                                #     # TODO: change tokenOnTrack to tokenOnPath for consistency
                                    if newTokenTilePosition not in currentPlayer.tokensOnTrack:
                                        currentPlayer.tokensOnTrack.append(currentToken)
                                    if currentToken in currentPlayer.tokensOnBase:
                                        currentPlayer.tokensOnBase.remove(currentToken)
                                    if currentToken in currentPlayer.tokensOnHome:
                                        currentPlayer.tokensOnHome.remove(currentToken)    
                                        # TODO: remove token if its in the home or base player list
                                elif newTokenTilePosition.tileType == 'base':
                                    if newTokenTilePosition not in currentPlayer.tokensOnBase:
                                        currentPlayer.tokensOnBase.append(currentToken)
                                    if currentToken in currentPlayer.tokensOnHome:
                                        currentPlayer.tokensOnHome.remove(currentToken)
                                    if currentToken in currentPlayer.tokensOnTrack:
                                        currentPlayer.tokensOnTrack.remove(currentToken)
                                elif newTokenTilePosition.tileType == 'home':
                                    if newTokenTilePosition not in currentPlayer.tokensOnHome:
                                        currentPlayer.tokensOnHome.append(currentToken)
                                    if currentToken in currentPlayer.tokensOnTrack:
                                        currentPlayer.tokensOnTrack.remove(currentToken)
                                    if currentToken in currentPlayer.tokensOnBase:
                                        currentPlayer.tokensOnBase.remove(currentToken)
                                counter += 1
                                print(counter)
                                print("Next: {}".format(players[counter%4].colour))
                        else:
                            print("Player did not pick their own token")

        pygame.quit()
        quit()

playing = Game()
playing.main()
