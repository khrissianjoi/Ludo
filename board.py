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
TEAM_BLUE1 = 65, 179, 226
TEAM_BLUE2 = 209,230,238
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
        self.boardLength = 15 #15*15 board

    def create_board(self):
        pygame.display.set_caption("Ludo")

        self.gameDisplay.fill(BLUE_BACKGROUND)

    def generate_tiles(self):

        for yCoord in range(1, self.boardLength+1):
            if yCoord in range(7,10):
                for xCoord in range(1, self.boardLength+1):
                    # avoiding the base
                    if xCoord*self.size not in range(420,580):
                        # path - horizontal white spaces
                        tileType = "path"
                        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord, self.size*yCoord, self.size, self.size], 1)
                        # add tiles to dictionary {tile: (range x coordinate, range y coordinate)}
                        currentTile = tile.Tile(range(self.size*xCoord,(self.size*xCoord)+61),range(self.size*yCoord,(self.size*yCoord)+61),tileType)
                        self.tiles[currentTile] = (range(self.size*xCoord,(self.size*xCoord)+61),range(self.size*yCoord,(self.size*yCoord)+61))
            else:
                for xCoord in range(1,self.boardLength+1):
                    # rect (left(x),top(y))
                    if (xCoord in range(0, 7) or xCoord in range(10, 16)):
                        # home base
                        tileType = "base"
                        if yCoord in range(0, 7) and xCoord in range(0, 7):
                            # red base
                            pygame.draw.rect(self.gameDisplay, TEAM_RED,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(0, 7) and xCoord in range(10, 16):
                            # blue base
                            pygame.draw.rect(self.gameDisplay, TEAM_BLUE1,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(10, 16) and xCoord in range(0, 7):
                            # yellow base
                            pygame.draw.rect(self.gameDisplay, TEAM_YELLOW,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        else:
                            # green base
                            pygame.draw.rect(self.gameDisplay, TEAM_GREEN,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                    else:
                        # path - vertical white spaces
                        tileType = "path"
                        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord, self.size*yCoord, self.size, self.size], 1)
                    
                    # add tiles to dictionary {tile: (range x coordinate, range y coordinate)}
                    currentTile = tile.Tile(range(self.size*xCoord,(self.size*xCoord)+61),range((self.size*yCoord),(self.size*yCoord)+61),tileType)
                    self.tiles[currentTile] = (range(self.size*xCoord,(self.size*xCoord)+61),range((self.size*yCoord),(self.size*yCoord)+61))
        
        # create triangle base
        pygame.draw.polygon(self.gameDisplay, TEAM_RED, [[420, 420], [510, 510], [420, 600]])
        pygame.draw.polygon(self.gameDisplay, TEAM_GREEN, [[600, 600], [510, 510], [600, 420]])
        pygame.draw.polygon(self.gameDisplay, TEAM_BLUE1, [[420, 420], [510, 510], [600, 420]])
        pygame.draw.polygon(self.gameDisplay, TEAM_YELLOW, [[600, 600], [510, 510], [420, 600]])


        pygame.draw.rect(self.gameDisplay, BLACK, [self.size, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)

        pygame.display.update()
