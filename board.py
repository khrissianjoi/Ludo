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

TEAM_BLUE1 = 209,230,238
TEAM_BLUE2 = 65, 179, 226

TEAM_YELLOW1 = 200,189,161
TEAM_YELLOW2 = 251, 217, 132

TEAM_RED1 = 245,221,219
TEAM_RED2 = 241, 120, 107

TEAM_GREEN1 = 190,235,224
TEAM_GREEN2 = 90, 200, 174

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

                    # pygame.draw.rect(self.gameDisplay, BLACK, [self.size*xCoord, self.size*yCoord, self.boardLength*self.size, self.boardLength*self.size], 3)
            else:
                for xCoord in range(1,self.boardLength+1):
                    # rect (left(x),top(y))
                    if (xCoord in range(0, 7) or xCoord in range(10, 16)):
                        # home base
                        tileType = "base"
                        
                        if yCoord in range(0, 7) and xCoord in range(0, 7):
                            # red base
                            pygame.draw.rect(self.gameDisplay, TEAM_RED1,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(0, 7) and xCoord in range(10, 16):
                            # blue base
                            pygame.draw.rect(self.gameDisplay, TEAM_BLUE1,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(10, 16) and xCoord in range(0, 7):
                            # yellow base
                            pygame.draw.rect(self.gameDisplay, TEAM_YELLOW1,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        else:
                            # green base
                            pygame.draw.rect(self.gameDisplay, TEAM_GREEN1,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                    else:
                        # path - vertical white spaces
                        tileType = "path"
                        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*xCoord, self.size*yCoord, self.size, self.size])
                        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord, self.size*yCoord, self.size, self.size], 1)

                    # add tiles to dictionary {tile: (range x coordinate, range y coordinate)}
                    currentTile = tile.Tile(range(self.size*xCoord,(self.size*xCoord)+61),range((self.size*yCoord),(self.size*yCoord)+61),tileType)
                    self.tiles[currentTile] = (range(self.size*xCoord,(self.size*xCoord)+61),range((self.size*yCoord),(self.size*yCoord)+61))

        # create triangle base
        pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[420, 420], [510, 510], [420, 600]])
        pygame.draw.polygon(self.gameDisplay, TEAM_GREEN2, [[600, 600], [510, 510], [600, 420]])
        pygame.draw.polygon(self.gameDisplay, TEAM_BLUE2, [[420, 420], [510, 510], [600, 420]])
        pygame.draw.polygon(self.gameDisplay, TEAM_YELLOW2, [[600, 600], [510, 510], [420, 600]])

        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (150,150),35) #top left, top right, bottom left, bottom right
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (330,150),35)

        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (330,330),35)
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (150,330),35)

        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (690,690),35)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (870,690),35)

        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (870,870),35)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (690,870),35)

        
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (150,690),35)
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (320,690),35)  

        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (150,870),35)
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (320,870),35)

        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (870,325),35)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (870,150),35)

        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (690,325),35)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (690,150),35)


        pygame.draw.rect(self.gameDisplay, BLACK, [self.size, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)

        pygame.display.update()
