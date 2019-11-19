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
    def createWhitePath(self,xCoord,yCoord):
        pygame.draw.rect(self.gameDisplay, WHITE,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
        pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
    def generate_tiles(self):
        redLayer= 0
        greenLayer =0
        blueLayer=0
        yellowLayer = 0

        star_path = [[24.615, 0.000], [30.315, 17.806], [48.758, 17.806], [33.837, 28.811], [39.536, 46.617], [24.615, 35.612], [9.695, 46.617], [15.394, 28.811], [0.473, 17.806], [18.916, 17.806], [24.615, 0.000]]
        for yCoord in range(1, self.boardLength+1):
            if yCoord in range(self.boardLength//2,10):
                for xCoord in range(1, self.boardLength+1):
                    # avoiding the base
                    if xCoord*self.size not in range(420,580):
                        tileType="path"
                        # path - horizontal spaces
                        if xCoord*self.size in range(60,420):
                            if redLayer:
                                translated_star_path = [[x + 525, y + 425] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, TEAM_RED2, translated_star_path)
                            #     pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[120+self.boardOverall, 445], [180+self.boardOverall, 445], [130+self.boardOverall, 480],[165+self.boardOverall,480], [150+self.boardOverall,480], [150+self.boardOverall,420]])
                                pass
                            redLayer += 1
                            if redLayer in red_counter:
                                self.createWhitePath(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_RED2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if redLayer == 15:
                                translated_star_path = [[x + 585, y + 545] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, WHITE, translated_star_path)
                        else:
                            if greenLayer:
                                translated_star_path = [[x + 1245, y + 545] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, TEAM_GREEN2, translated_star_path)
                            #     pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[120+self.boardOverall, 445], [180+self.boardOverall, 445], [130+self.boardOverall, 480],[165+self.boardOverall,480], [150+self.boardOverall,480], [150+self.boardOverall,420]])
                                pass
                            greenLayer += 1
                            if greenLayer in green_counter:
                                self.createWhitePath(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_GREEN2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if greenLayer == 4:
                                translated_star_path = [[x + 1185, y + 425] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, WHITE, translated_star_path)
                        # add tiles to dictionary {tile: (range x coordinate, range y coordinate)}
                        currentTile = tile.Tile(range(self.size*xCoord,(self.size*xCoord+self.boardOverall)+61),range(self.size*yCoord,(self.size*yCoord)+61),tileType)
                        self.tiles[currentTile] = (range(self.size*xCoord,(self.size*xCoord)+61),range(self.size*yCoord,(self.size*yCoord)+61))
                # pygame.draw.rect(self.gameDisplay, BLACK, [self.size, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)
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
                            if blueLayer:
                                translated_star_path = [[x + 945, y + 125] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, TEAM_BLUE2, translated_star_path)
                            #     pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[120+self.boardOverall, 445], [180+self.boardOverall, 445], [130+self.boardOverall, 480],[165+self.boardOverall,480], [150+self.boardOverall,480], [150+self.boardOverall,420]])
                                pass
                            blueLayer += 1
                            if blueLayer in blue_counter:
                                self.createWhitePath(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_BLUE2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if blueLayer == 12:
                                translated_star_path = [[x + 825, y + 185] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, WHITE, translated_star_path)
                        else:
                            if yellowLayer:
                                translated_star_path = [[x + 825, y + 845] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, TEAM_YELLOW2, translated_star_path)
                            #     pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[120+self.boardOverall, 445], [180+self.boardOverall, 445], [130+self.boardOverall, 480],[165+self.boardOverall,480], [150+self.boardOverall,480], [150+self.boardOverall,420]])
                                pass
                            yellowLayer += 1
                            if yellowLayer in yellow_counter:
                                self.createWhitePath(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, TEAM_YELLOW2,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, BLACK,[self.size*xCoord+self.boardOverall, self.size*yCoord, self.size, self.size], 1)

                            if yellowLayer == 12:
                                translated_star_path = [[x + 945, y + 785] for [x, y] in star_path]
                                pygame.draw.polygon(self.gameDisplay, WHITE, translated_star_path)
                    # add tiles to dictionary {tile: (range x coordinate, range y coordinate)}
                    currentTile = tile.Tile(range(self.size*xCoord,(self.size*xCoord)+61),range((self.size*yCoord),(self.size*yCoord)+61),tileType)
                    self.tiles[currentTile] = (range(self.size*xCoord,(self.size*xCoord)+61),range((self.size*yCoord),(self.size*yCoord)+61))
                    # pygame.draw.rect(self.gameDisplay, BLACK, [self.size*xCoord, self.size*yCoord, self.boardLength*self.size, self.boardLength*self.size], 3)
        # create triangle home
        pygame.draw.polygon(self.gameDisplay, TEAM_RED2, [[420+self.boardOverall, 420], [510+self.boardOverall, 510], [420+self.boardOverall, 600]])
        pygame.draw.line(self.gameDisplay, BLACK, (420+self.boardOverall, 600), (420+self.boardOverall,420),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_GREEN2, [[600+self.boardOverall, 600], [510+self.boardOverall, 510], [600+self.boardOverall, 420]])
        pygame.draw.line(self.gameDisplay, BLACK, (600+self.boardOverall, 420), (600+self.boardOverall,600),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_BLUE2, [[420+self.boardOverall, 420], [510+self.boardOverall, 510], [600+self.boardOverall, 420]])
        pygame.draw.line(self.gameDisplay, BLACK, (600+self.boardOverall, 420), (420+self.boardOverall,420),3)

        pygame.draw.polygon(self.gameDisplay, TEAM_YELLOW2, [[600+self.boardOverall, 600], [510+self.boardOverall, 510], [420+self.boardOverall, 600]])
        pygame.draw.line(self.gameDisplay, BLACK, (420+self.boardOverall, 600), (600+self.boardOverall,600),3)

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


        pygame.draw.rect(self.gameDisplay, BLACK, [self.size+self.boardOverall, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)

        pygame.display.update()