import pygame
import board
import datetime

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

        ludo = board.Board()
        
        ludo.createBoard()

        while not self.gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    print(x,y)
                    for tile in ludo.tiles:
                        if x in ludo.tiles[tile][0] and y in ludo.tiles[tile][1]:
                            print(tile.tileType)
                            break
                        
        pygame.quit()
        quit()

playing = Game()
playing.main()