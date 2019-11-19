import pygame
import tile

WHITE = 255,255,255
BLACK = 0,0,0

# interface colours
BLUE_BACKGROUND = 209, 230, 238

# team colours
TEAM_BLUE1 = 209,230,238 #dark
TEAM_BLUE2 = 65, 179, 226 #light

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
                pygame.draw.rect(self.gameDisplay, BLACK, [self.size, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)
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
                    # pygame.draw.rect(self.gameDisplay, BLACK, [self.size*xCoord, self.size*yCoord, self.boardLength*self.size, self.boardLength*self.size], 3)
        # create triangle home
        pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[420, 420], [510, 510], [420, 600]])
        pygame.draw.polygon(self.gameDisplay, TEAM_GREEN2, [[600, 600], [510, 510], [600, 420]])
        pygame.draw.polygon(self.gameDisplay, TEAM_BLUE2, [[420, 420], [510, 510], [600, 420]])
        pygame.draw.polygon(self.gameDisplay, TEAM_YELLOW2, [[600, 600], [510, 510], [420, 600]])

        # base circles
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (240,120),45) #top left, top right, bottom left, bottom right
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (120,240),45)
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (360,240),45)
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (240,360),45)

        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (780,660),45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (660,780),45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (900,780),45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (780,890),45)

        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (240,660),45)
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (120,780),45)  
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (360,780),45)
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (240,900),45)

        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (780,120),45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (670,240),45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (900,240),45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (780,360),45)


        pygame.draw.rect(self.gameDisplay, BLACK, [self.size, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)

        pygame.display.update()
