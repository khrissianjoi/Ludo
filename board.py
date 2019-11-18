import pygame
import tile


WHITE = 255,255,255
BLACK = 0,0,0
RED = 255, 0, 0, 0.8
YELLOW = 236, 183, 24, 1
GREEN = 102, 236, 24, 1

BLUE_BACKGROUND = 209,230,238

TEAM_BLUE = 65, 179, 226
TEAM_YELLOW = 251,217,132
TEAM_RED = 241, 120, 107
TEAM_GREEN = 90,200,174

class Board:
    def __init__(self):
        self.size = 60
        self.x = 1100
        self.y = 1100
        self.gameDisplay = pygame.display.set_mode((self.x,self.y))

    def generate_tiles(self):
        pygame.display.set_caption("Board")

        self.gameDisplay.fill(BLUE_BACKGROUND)
        boardLength = 15 # 15*15 board
        for i in range(1,boardLength+1):
            if i in range(7,10):
                for z in range(1,boardLength+1):
                    # path - horizontal white spaces
                    pygame.draw.rect(self.gameDisplay, WHITE,[self.size*z,self.size*i,self.size,self.size])
                    pygame.draw.rect(self.gameDisplay, BLACK,[self.size*z,self.size*i,self.size,self.size],1)
            else:
                for z in range(1,boardLength+1):
                    if (z in range(0,7) or z in range(10,16)):
                        # home base
                        if i in range(0,7) and z in range(0,7):
                            pygame.draw.rect(self.gameDisplay, TEAM_RED,[self.size*z,self.size*i,self.size,self.size])
                        elif i in range(0,7) and z in range(10,16):
                            pygame.draw.rect(self.gameDisplay, TEAM_BLUE,[self.size*z,self.size*i,self.size,self.size])
                        elif i in range(10,16) and z in range(0,7):
                            pygame.draw.rect(self.gameDisplay, TEAM_YELLOW,[self.size*z,self.size*i,self.size,self.size])
                        else:
                            pygame.draw.rect(self.gameDisplay, TEAM_GREEN,[self.size*z,self.size*i,self.size,self.size])
                    else:
                        # path - vertical white spaces
                        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*z,self.size*i,self.size,self.size])
                        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*z,self.size*i,self.size,self.size],1)

        pygame.draw.rect(self.gameDisplay,BLACK,[self.size,self.size,boardLength*self.size,boardLength*self.size],3)

        pygame.display.update()