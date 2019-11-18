import pygame


WHITE = 200,200,200
BLACK = 0,0,0

class Board:
    def __init__(self):
        self.size = 100
        self.x = 1000
        self.y = 1000
        self.gameDisplay = pygame.display.set_mode((self.x,self.y))

    def generate_tiles(self):
        pygame.display.set_caption("Board")

        self.gameDisplay.fill(WHITE)

        boardLength = 8
        cnt = 0
        for i in range(1,boardLength+1):
            for z in range(1,boardLength+1):
                if cnt % 2 == 0:
                    pygame.draw.rect(self.gameDisplay, WHITE,[self.size*z,self.size*i,self.size,self.size])
                else:
                    pygame.draw.rect(self.gameDisplay, BLACK, [self.size*z,self.size*i,self.size,self.size])
                cnt +=1
            cnt-=1

        pygame.draw.rect(self.gameDisplay,BLACK,[self.size,self.size,boardLength*self.size,boardLength*self.size],1)

        pygame.display.update()