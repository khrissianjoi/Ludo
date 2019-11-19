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

red_counter = {2,8,9,10,11,12}
green_counter = {7,8,9,10,11,17}
blue_counter = {5,6,8,11,14,17}
yellow_counter = {2,5,8,11,13,14}

# star points
star_path = [[24.615, 0.000], [30.315, 17.806], [48.758, 17.806], [33.837, 28.811], [39.536, 46.617], [24.615, 35.612], [9.695, 46.617], [15.394, 28.811], [0.473, 17.806], [18.916, 17.806], [24.615, 0.000]]

pawn_path = [[44.0, 54.0], [44.0, 54.0], [45.0, 51.0], [43.0, 44.0], [40.0, 33.0], [41.0, 23.0], [43.0, 20.0], [40.0, 17.0], [38.0, 17.0], [42.0, 9.0], [32.0, 0.0], [22.0, 9.0], [26.0, 17.0], [25.0, 17.0], [21.0, 20.0], [25.0, 24.0], [36.0, 24.0], [37.0, 22.0], [36.0, 21.0], [25.0, 21.0], [24.0, 20.0], [25.0, 19.0], [40.0, 19.0], [41.0, 20.0], [40.0, 21.0], [40.0, 21.0], [40.0, 21.0], [40.0, 21.0], [39.0, 22.0], [39.0, 22.0], [39.0, 22.0], [39.0, 22.0], [39.0, 22.0], [38.0, 33.0], [41.0, 45.0], [43.0, 51.0], [40.0, 54.0], [29.0, 54.0], [28.0, 55.0], [29.0, 56.0], [44.0, 56.0], [48.0, 60.0], [48.0, 63.0], [17.0, 63.0], [17.0, 60.0], [20.0, 56.0], [25.0, 56.0], [26.0, 55.0], [25.0, 54.0], [21.0, 51.0], [23.0, 45.0], [27.0, 33.0], [26.0, 27.0], [25.0, 26.0], [24.0, 27.0], [25.0, 33.0], [21.0, 44.0], [19.0, 51.0], [20.0, 54.0], [20.0, 54.0], [15.0, 60.0], [15.0, 64.0], [16.0, 65.0], [49.0, 65.0], [50.0, 64.0], [50.0, 60.0], [44.0, 54.0]]

class Board:
    def __init__(self):
        self.tiles = {}
        self.size = 60
        self.display_size_x = 1800
        # 225 each for the player sides
        # 450 for board
        self.boardOverall = 400
        self.playerSides = 225
        self.display_size_y = 1000
        self.gameDisplay = pygame.display.set_mode((self.display_size_x, self.display_size_y))
        self.boardLength = 15 #15*15 board

    def create_board(self):
        pygame.display.set_caption("Ludo")
        self.gameDisplay.fill(BLUE_BACKGROUND)
        self.generate_tiles()

    def createWhitePath(self,xCoord,yCoord):
        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)

    def createSafeTile(self, x_add, y_add, colour):
        tileType = 'safe'
        translated_star_path = [[x + x_add, y + y_add] for [x, y] in star_path]
        pygame.draw.polygon(self.gameDisplay, colour, translated_star_path)

    def generate_tiles(self):
        redLayer = 0
        greenLayer = 0
        blueLayer = 0
        yellowLayer = 0
        
        for yCoord in range(1, self.boardLength+1):
            if yCoord in range(self.boardLength//2,10):
                for xCoord in range(1, self.boardLength+1):
                    # avoiding the base
                    if xCoord*self.size not in range(420,580):
                        tileType="path"
                        # path - horizontal spaces
                        if xCoord*self.size in range(60,420):
                            redLayer += 1
                            if redLayer in red_counter:
                                self.createWhitePath(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_RED2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if redLayer==2:
                                tileType = "safe"
                                self.createSafeTile(525,425, TEAM_RED2)
                            if redLayer == 15:
                                tileType = "safe"
                                self.createSafeTile(585,545, WHITE)
                        else:
                            greenLayer += 1
                            if greenLayer in green_counter:
                                self.createWhitePath(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_GREEN2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if greenLayer == 17:
                                tileType = "safe"
                                self.createSafeTile(1245,545, TEAM_GREEN2)
                            if greenLayer == 4:
                                tileType = "safe"
                                self.createSafeTile(1185,425, WHITE)
                        # add tiles to dictionary {tile: (range x coordinate, range y coordinate)}
                    currentTile = tile.Tile(range(self.size*xCoord+self.boardOverall,self.size*xCoord+self.boardOverall+(self.size+1)),range(self.size*yCoord,self.size*yCoord+(self.size+1)),tileType)
                    self.tiles[currentTile] = (range(self.size*xCoord+self.boardOverall,self.size*xCoord+self.boardOverall+(self.size+1)),range(self.size*yCoord,self.size*yCoord+(self.size+1)))
            else:
                for xCoord in range(1,self.boardLength+1):
                    if xCoord in range(0, self.boardLength//2) or xCoord in range(self.boardLength//2+3, self.boardLength+1):
                        # home base
                        tileType = "base"
                        if yCoord in range(0, self.boardLength//2) and xCoord in range(0, self.boardLength//2):
                            # red base
                            pygame.draw.rect(self.gameDisplay, TEAM_RED1,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(0, self.boardLength//2) and xCoord in range(self.boardLength//2+3, self.boardLength+1):
                            # blue base
                            pygame.draw.rect(self.gameDisplay, TEAM_BLUE1,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(self.boardLength//2+3, self.boardLength+1) and xCoord in range(0, self.boardLength//2):
                            # yellow base
                            pygame.draw.rect(self.gameDisplay, TEAM_YELLOW1,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                        else:
                            # green base
                            pygame.draw.rect(self.gameDisplay, TEAM_GREEN1,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                    else:
                        # path - vertical white spaces
                        tileType = "path"
                        if yCoord*self.size in range (60,421):
                            blueLayer += 1
                            if blueLayer in blue_counter:
                                self.createWhitePath(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_BLUE2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if blueLayer == 7:
                                tileType = "safe"
                                self.createSafeTile(825,185, WHITE)
                            if blueLayer == 6:
                                tileType = "safe"
                                self.createSafeTile(945,125, TEAM_BLUE2)
                        else:
                            yellowLayer += 1
                            if yellowLayer in yellow_counter:
                                self.createWhitePath(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_YELLOW2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)

                            if yellowLayer== 13:
                                tileType = "safe"
                                translated_star_path = [[x + 825, y + 845] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, TEAM_YELLOW2, translated_star_path)
                            if yellowLayer == 12:
                                tileType = "safe"
                                translated_star_path = [[x + 945, y + 785] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, WHITE, translated_star_path)
                    
                    # add tiles to dictionary {tile: (range x coordinate, range y coordinate)}
                    #plus 61 because size of tile
                    currentTile = tile.Tile(range(self.size*xCoord+self.boardOverall,self.size*xCoord+self.boardOverall+(self.size+1)),range(self.size*yCoord,self.size*yCoord+(self.size+1)),tileType)
                    self.tiles[currentTile] = (range(self.size*xCoord+self.boardOverall,self.size*xCoord+self.boardOverall+(self.size+1)),range((self.size*yCoord),self.size*yCoord+(self.size+1)))
        
        self.createTriangleHome()
        self.createBaseCircles()

        translated_pawn_path = [[x + 610, y +85] for [x, y] in pawn_path]
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_pawn_path)

        pygame.draw.rect(self.gameDisplay, BLACK, [self.size+self.boardOverall, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)

        pygame.display.update()

    def createTriangleHome(self):
        # create triangle home
        pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[420+self.boardOverall, 420], [510+self.boardOverall, 510], [420+self.boardOverall, 600]])
        pygame.draw.line(self.gameDisplay, BLACK, (420+self.boardOverall, 600), (420+self.boardOverall,420),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_GREEN2, [[600+self.boardOverall, 600], [510+self.boardOverall, 510], [600+self.boardOverall, 420]])
        pygame.draw.line(self.gameDisplay, BLACK, (600+self.boardOverall, 420), (600+self.boardOverall,600),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_BLUE2, [[420+self.boardOverall, 420], [510+self.boardOverall, 510], [600+self.boardOverall, 420]])
        pygame.draw.line(self.gameDisplay, BLACK, (600+self.boardOverall, 420), (420+self.boardOverall,420),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_YELLOW2, [[600+self.boardOverall, 600], [510+self.boardOverall, 510], [420+self.boardOverall, 600]])
        pygame.draw.line(self.gameDisplay, BLACK, (420+self.boardOverall, 600), (600+self.boardOverall,600),3)


    def createBaseCircles(self):
        # base circles
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (240+self.boardOverall,120),45) #top left, top right, bottom left, bottom right
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (120+self.boardOverall,240),45)
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (360+self.boardOverall,240),45)
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (240+self.boardOverall,360),45)

        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (780+self.boardOverall,660),45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (660+self.boardOverall,780),45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (900+self.boardOverall,780),45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (780+self.boardOverall,890),45)

        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (240+self.boardOverall,660),45)
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (120+self.boardOverall,780),45)  
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (360+self.boardOverall,780),45)
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (240+self.boardOverall,900),45)

        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (780+self.boardOverall,120),45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (670+self.boardOverall,240),45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (900+self.boardOverall,240),45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (780+self.boardOverall,360),45)