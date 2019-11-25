import pygame
import tile
from tokencreate import TokenCreate

WHITE = 255,255,255
BLACK = 0,0,0

# interface colours
BLUE_BACKGROUND = 209, 230, 238

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

red_counter = {2,8,9,10,11,12}
green_counter = {7,8,9,10,11,17}
blue_counter = {5,6,8,11,14,17}
yellow_counter = {2,5,8,11,13,14}

# star points
star_path = [[24.615, 0.000], [30.315, 17.806], [48.758, 17.806], [33.837, 28.811], [39.536, 46.617], [24.615, 35.612], [9.695, 46.617], [15.394, 28.811], [0.473, 17.806], [18.916, 17.806], [24.615, 0.000]]
# token points
token_path = [[55.0, 61.0], [54.0, 61.0], [54.0, 53.0], [47.0, 29.0], [47.0, 29.0], [49.0, 27.0], [49.0, 26.0], [47.0, 24.0], [47.0, 24.0], [51.0, 14.0], [37.0, 0.0], [22.0, 14.0], [27.0, 24.0], [26.0, 24.0], [24.0, 26.0], [24.0, 27.0], [26.0, 29.0], [27.0, 29.0], [20.0, 53.0], [20.0, 61.0], [18.0, 61.0], [16.0, 63.0], [16.0, 68.0], [18.0, 70.0], [18.0, 70.0], [18.0, 74.0], [55.0, 74.0], [55.0, 70.0], [57.0, 68.0], [57.0, 63.0], [55.0, 61.0]]


class Board:
    def __init__(self):
        self.tiles = {}
        self.size = 60
        self.display_size_x = 1800
        self.display_size_y = 1000
        self.boardOverall = 400 # 400 for board
        self.playerSides = 225 # 225 each for the player sides
        self.gameDisplay = pygame.display.set_mode((self.display_size_x, self.display_size_y))
        self.boardLength = 15 #15*15 board


    def createBoard(self):
        '''create Ludo board'''
        pygame.display.set_caption("Ludo")
        self.gameDisplay.fill(BLUE_BACKGROUND)
        self.generateTiles()
        self.createTriangleHome()
        self.createBaseCircles()
        self.createTokens() 
        # border around board
        pygame.draw.rect(self.gameDisplay, BLACK, [self.size+self.boardOverall, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)
        pygame.display.update()


    def createWhiteTile(self, xCoord, yCoord):
        # create white path
        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)


    def createSafeTile(self, x_add, y_add, colour):
        tileType = 'safe'
        translated_star_path = [[x + x_add, y + y_add] for [x, y] in star_path]
        pygame.draw.polygon(self.gameDisplay, colour, translated_star_path)


    def generateTiles(self):
        redLayer = greenLayer = blueLayer = yellowLayer = 0
        for yCoord in range(1, self.boardLength+1):
            if yCoord in range(self.boardLength//2, 10):
                for xCoord in range(1, self.boardLength+1):
                    # avoiding the base
                    if xCoord*self.size not in range(self.size*7, self.size*10):
                        tileType = "path"
                        # path - horizontal spaces
                        if xCoord*self.size in range(self.size, self.size*7):
                            redLayer += 1
                            if redLayer in red_counter:
                                self.createWhiteTile(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_RED2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if redLayer == 2:
                                tileType = "safe"
                                self.createSafeTile(525,425, TEAM_RED2)
                            if redLayer == 15:
                                tileType = "safe"
                                self.createSafeTile(585,545, WHITE)
                        else:
                            greenLayer += 1
                            if greenLayer in green_counter:
                                self.createWhiteTile(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_GREEN2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if greenLayer == 17:
                                tileType = "safe"
                                self.createSafeTile(1245,545, TEAM_GREEN2)
                            if greenLayer == 4:
                                tileType = "safe"
                                self.createSafeTile(1185,425, WHITE)
                                
                    self.addTile(self.size*xCoord+self.boardOverall, self.size*xCoord+self.boardOverall+(self.size+1), self.size*yCoord, self.size*yCoord+(self.size+1), tileType)

            else:
                for xCoord in range(1, self.boardLength+1):
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
                        if yCoord*self.size in range (self.size, self.size*7):
                            blueLayer += 1
                            if blueLayer in blue_counter:
                                self.createWhiteTile(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_BLUE2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if blueLayer == 7:
                                tileType = "safe"
                                self.createSafeTile(825, 185, WHITE)
                            if blueLayer == 6:
                                tileType = "safe"
                                self.createSafeTile(945, 125, TEAM_BLUE2)
                        else:
                            yellowLayer += 1
                            if yellowLayer in yellow_counter:
                                self.createWhiteTile(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_YELLOW2, [self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK, [self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)

                            if yellowLayer == 13:
                                tileType = "safe"
                                self.createSafeTile(825, 845, TEAM_YELLOW2)
                            if yellowLayer == 12:
                                tileType = "safe"
                                self.createSafeTile(945, 785, WHITE)
                    
                    # add tiles to dictionary {tile: (range x coordinate, range y coordinate)}
                    #plus 61 because size of tile
                    self.addTile(self.size*xCoord+self.boardOverall, self.size*xCoord+self.boardOverall+(self.size+1), self.size*yCoord, self.size*yCoord+(self.size+1), tileType)


    def addTile(self,xStartCoord, xEndCoord, yStartCoord, yEndCoord, tileType):
        '''add tiles to dictionary {tile: (range x coordinate, range y coordinate)}'''
        currentTile = tile.Tile(range(xStartCoord,xEndCoord),range(yStartCoord,yEndCoord),tileType)
        self.tiles[currentTile] = (range(xStartCoord,xEndCoord),range(yStartCoord,yEndCoord))


    def createTriangleHome(self):
        '''create triangle home'''
        pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[self.size*7+self.boardOverall, self.size*7], [510+self.boardOverall, 510], [self.size*7+self.boardOverall, self.size*10]])
        pygame.draw.line(self.gameDisplay, BLACK, (self.size*7+self.boardOverall, self.size*10), (self.size*7+self.boardOverall,self.size*7),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_GREEN2, [[self.size*10+self.boardOverall, self.size*10], [510+self.boardOverall, 510], [self.size*10+self.boardOverall, self.size*7]])
        pygame.draw.line(self.gameDisplay, BLACK, (self.size*10+self.boardOverall, self.size*7), (self.size*10+self.boardOverall,self.size*10),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_BLUE2, [[self.size*7+self.boardOverall, self.size*7], [510+self.boardOverall, 510], [self.size*10+self.boardOverall, self.size*7]])
        pygame.draw.line(self.gameDisplay, BLACK, (self.size*10+self.boardOverall, self.size*7), (self.size*7+self.boardOverall,self.size*7),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_YELLOW2, [[self.size*10+self.boardOverall, self.size*10], [510+self.boardOverall, 510], [self.size*7+self.boardOverall, self.size*10]])
        pygame.draw.line(self.gameDisplay, BLACK, (self.size*7+self.boardOverall, self.size*10), (self.size*10+self.boardOverall,self.size*10),3)


    def createTokens(self):
        '''create Tokens'''

        #RED
        translated_token_path = [[x + 605, y +80] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, RED_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        R1 = TokenCreate(translated_token_path,RED_TOKEN, (605,80))

        translated_token_path = [[x + 485, y +200] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, RED_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        R2 = TokenCreate(translated_token_path,RED_TOKEN,(485,200))

        translated_token_path = [[x + 725, y +200] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, RED_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        R3 = TokenCreate(translated_token_path,RED_TOKEN,(725,200))

        translated_token_path = [[x + 605, y +320] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, RED_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        R4 = TokenCreate(translated_token_path,RED_TOKEN,(605,320))


        #YELLOW
        translated_token_path = [[x + 605, y +620] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, YELLOW_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        Y1 = TokenCreate(translated_token_path,YELLOW_TOKEN,(605,620))

        translated_token_path = [[x + 485, y +740] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, YELLOW_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        Y2 = TokenCreate(translated_token_path,YELLOW_TOKEN,(485,740))
        
        translated_token_path = [[x + 725, y +740] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, YELLOW_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        Y3 = TokenCreate(translated_token_path,YELLOW_TOKEN,(725,740))
        
        translated_token_path = [[x + 605, y +860] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, YELLOW_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        Y4 = TokenCreate(translated_token_path,YELLOW_TOKEN,(605,860))
        

        #BLUE
        translated_token_path = [[x + 1145, y + 80] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, BLUE_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        B1 = TokenCreate(translated_token_path,BLUE_TOKEN,(1145,80))

        translated_token_path = [[x + 1035, y +200] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, BLUE_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        B2 = TokenCreate(translated_token_path,BLUE_TOKEN,(1035,200))

        translated_token_path = [[x + 1265, y +200] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, BLUE_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        B3 = TokenCreate(translated_token_path,BLUE_TOKEN,(1265,200))

        translated_token_path = [[x + 1145, y +320] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, BLUE_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)  
        B4 = TokenCreate(translated_token_path,BLUE_TOKEN,(1145,320))


        #GREEN
        translated_token_path = [[x + 1145, y + 620] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, GREEN_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        G1 = TokenCreate(translated_token_path,GREEN_TOKEN,(1145,620))

        translated_token_path = [[x + 1025, y + 740] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, GREEN_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        G2 = TokenCreate(translated_token_path,GREEN_TOKEN,(1025,740))

        translated_token_path = [[x + 1265, y + 740] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, GREEN_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        G3 = TokenCreate(translated_token_path,GREEN_TOKEN,(1265,740))

        translated_token_path = [[x + 1145, y + 850] for [x, y] in token_path]
        pygame.draw.polygon(self.gameDisplay, GREEN_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, BLACK, translated_token_path,1)
        G4 = TokenCreate(translated_token_path,GREEN_TOKEN,(1145,850))


    def createBaseCircles(self):
        '''create base circles'''
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (240+self.boardOverall, 120), 45) #top
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (120+self.boardOverall, 240), 45) #left
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (360+self.boardOverall, 240), 45) #right
        pygame.draw.circle(self.gameDisplay, TEAM_RED2, (240+self.boardOverall, 360), 45) #bottom

        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (780+self.boardOverall, 660), 45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (660+self.boardOverall, 780), 45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (900+self.boardOverall, 780), 45)
        pygame.draw.circle(self.gameDisplay, TEAM_GREEN2, (780+self.boardOverall, 890), 45)

        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (240+self.boardOverall, 660), 45)
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (120+self.boardOverall, 780), 45)  
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (360+self.boardOverall, 780), 45)
        pygame.draw.circle(self.gameDisplay, TEAM_YELLOW2, (240+self.boardOverall, 900), 45)

        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (780+self.boardOverall, 120), 45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (670+self.boardOverall, 240), 45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (900+self.boardOverall, 240), 45)
        pygame.draw.circle(self.gameDisplay, TEAM_BLUE2, (780+self.boardOverall, 360), 45)
