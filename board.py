import pygame
import tile

WHITE = 255,255,255
BLACK = 0,0,0
RED = 255, 0, 0, 0.8
YELLOW = 236, 183, 24, 1
GREEN = 102, 236, 24, 1

# interface colours
BLUE_BACKGROUND = 209, 230, 238

# team colours
TEAM_BLUE = 65, 179, 226
TEAM_YELLOW = 251, 217, 132
TEAM_RED = 241, 120, 107
TEAM_GREEN = 90, 200, 174

class Board:
    def __init__(self):
        self.tiles = {}
        self.size = 60
        self.display_size_x = 1500
        self.display_size_y = 1000
        self.gameDisplay = pygame.display.set_mode((self.display_size_x, self.display_size_y))

    def generate_tiles(self):
        pygame.display.set_caption("Board")

        self.gameDisplay.fill(BLUE_BACKGROUND)
        boardLength = 15 # 15*15 board
        for yCoord in range(1, boardLength+1):
            if yCoord in range(7,10):
                for xCoord in range(1, boardLength+1):
                    # path - horizontal white spaces
                    tileType = "path"
                    pygame.draw.rect(self.gameDisplay, WHITE,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                    pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord, self.size*yCoord, self.size, self.size], 1)
                    currentTile = tile.Tile(range(self.size*xCoord,(self.size*xCoord)+61),range(self.size*yCoord,(self.size*yCoord)+61),tileType)
                    self.tiles[currentTile] = (range(self.size*xCoord,(self.size*xCoord)+61),range(self.size*yCoord,(self.size*yCoord)+61))
            else:
                for xCoord in range(1,boardLength+1):
                    # rect (left(x),top(y))
                    if (xCoord in range(0, 7) or xCoord in range(10, 16)):
                        # home base
                        tileType = "base"
                        if yCoord in range(0, 7) and xCoord in range(0, 7):
                            pygame.draw.rect(self.gameDisplay, TEAM_RED,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(0, 7) and xCoord in range(10, 16):
                            pygame.draw.rect(self.gameDisplay, TEAM_BLUE,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(10, 16) and xCoord in range(0, 7):
                            pygame.draw.rect(self.gameDisplay, TEAM_YELLOW,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        else:
                            pygame.draw.rect(self.gameDisplay, TEAM_GREEN,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                    else:
                        # path - vertical white spaces
                        tileType = "path"
                        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord, self.size*yCoord, self.size, self.size], 1)
                    # append tiles to list
                    currentTile = tile.Tile(range(self.size*xCoord,(self.size*xCoord)+61),range((self.size*yCoord),(self.size*yCoord)+61),tileType)
                    self.tiles[currentTile] = (range(self.size*xCoord,(self.size*xCoord)+61),range((self.size*yCoord),(self.size*yCoord)+61))

        pygame.draw.rect(self.gameDisplay, BLACK, [self.size, self.size, boardLength*self.size, boardLength*self.size], 3)

        pygame.display.update()
