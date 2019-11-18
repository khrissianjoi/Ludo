import pygame


WHITE = 200,200,200
BLACK = 0,0,0
RED = 255, 0, 0, 0.8
YELLOW = 236, 183, 24, 1
BLUE = 24, 116, 236, 1
GREEN = 102, 236, 24, 1
class Board:
    def __init__(self):
        self.size = 30
        self.x = 1100
        self.y = 1100
        self.gameDisplay = pygame.display.set_mode((self.x,self.y))

    def generate_tiles(self):
        pygame.display.set_caption("Board")

        self.gameDisplay.fill(YELLOW)

        boardLength = 15
        for i in range(1,boardLength+1):
            if i in range(7,10):
                for z in range(1,boardLength+1):
                    pygame.draw.rect(self.gameDisplay, WHITE,[self.size*z,self.size*i,self.size,self.size])
            else:
                for z in range(1,boardLength+1):
                    if (z in range(0,7) or z in range(10,16)):
                        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*z,self.size*i,self.size,self.size])
                    else:
                        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*z,self.size*i,self.size,self.size])
        pygame.draw.rect(self.gameDisplay,BLACK,[self.size,self.size,boardLength*self.size,boardLength*self.size],1)

        pygame.display.update()