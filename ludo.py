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
        playerRed = Player("Dale",(125,125,125),[],ludo.redTokens,[])
        playerYellow = Player("John",(125,125,125),[],ludo.yellowTokens,[])
        playerBlue = Player("Alex",(125,125,125),[],ludo.blueTokens,[])
        playerGreen = Player("Joi",(125,125,125),[],ludo.greenTokens,[])
        
        playerRed.rollDice()

        while not self.gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    for tile in ludo.tiles:
                        if x in ludo.tiles[tile][0] and y in ludo.tiles[tile][1]:
                            print("x : {}, y : {}, type: {}".format(x,y,tile.tileType))
                            break
                        
        pygame.quit()
        quit()

playing = Game()
playing.main()
