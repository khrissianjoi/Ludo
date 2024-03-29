import pygame
import tile
import os
from tokencreate import TokenCreate
from gameColours import GameColours

class Board:
    def __init__(self, playerNames):
        self.tiles = {}
        self.size = 40
        self.display_size_x = 1400
        self.display_size_y = 800
        self.boardOverall = 365
        self.gameDisplay = pygame.display.set_mode((self.display_size_x, self.display_size_y))
        self.boardLength = 15  # 15*15 board

        # star points
        self.star_path = [[18.46125, 0.0], [22.736250000000002, 13.354500000000002], [36.5685, 13.354500000000002], [25.377750000000002, 21.608249999999998], [29.652, 34.96275], [18.46125, 26.709000000000003], [7.27125, 34.96275], [11.5455, 21.608249999999998], [0.35475, 13.354500000000002], [14.187000000000001, 13.354500000000002], [18.46125, 0.0]]
        # token points
        self.token_path = [[27.5, 30.5], [27.0, 30.5], [27.0, 26.5], [23.5, 14.5], [23.5, 14.5], [24.5, 13.5], [24.5, 13.0], [23.5, 12.0], [23.5, 12.0], [25.5, 7.0], [18.5, 0.0], [11.0, 7.0], [13.5, 12.0], [13.0, 12.0], [12.0, 13.0], [12.0, 13.5], [13.0, 14.5], [13.5, 14.5], [10.0, 26.5], [10.0, 30.5], [9.0, 30.5], [8.0, 31.5], [8.0, 34.0], [9.0, 35.0], [9.0, 35.0], [9.0, 37.0], [27.5, 37.0], [27.5, 35.0], [28.5, 34.0], [28.5, 31.5], [27.5, 30.5]]

        self.redTokens = []
        self.greenTokens = []
        self.blueTokens = []
        self.yellowTokens = []

        self.yellowPath = []
        self.redPath = []
        self.bluePath = []
        self.greenPath = []
        self.playerNames = playerNames

        self.redCounter = {2, 8, 9, 10, 11, 12}
        self.greenCounter = {7, 8, 9, 10, 11, 17}
        self.blueCounter = {5, 6, 8, 11, 14, 17}
        self.yellowCounter = {2, 5, 8, 11, 13, 14}

        self.greenCounter1 = {7, 8, 9, 10, 11}
        self.yellowCounter1 = {2, 5, 8, 11, 14}
        self.redCounter1 = {8, 9, 10, 11, 12}
        self.blueCounter1 = {5, 8, 11, 14, 17}
        self.colours = GameColours()

    def regenerateBoard(self, text=None):
        pygame.display.set_caption("Ludo")
        image = pygame.image.load(os.path.join("images", "background.png"))
        cropped_image = pygame.transform.scale(image, (1400, 400))
        self.gameDisplay.blit(cropped_image, (0, 0))
        self.gameDisplay.blit(cropped_image, (0, 400))
        self.generateTiles()
        self.createTriangleHome()
        self.createBaseCircles()
        self.generatePerson()
        pygame.draw.rect(self.gameDisplay, self.colours.BLACK, [self.size + self.boardOverall, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)

    def createBoard(self):
        '''create Ludo board'''
        pygame.display.set_caption("Ludo")
        image = pygame.image.load(os.path.join("images", "background.png"))
        cropped_image = pygame.transform.scale(image, (1400, 400))
        self.gameDisplay.blit(cropped_image, (0, 0))
        self.gameDisplay.blit(cropped_image, (0, 400))
        self.generateTiles()
        self.createTriangleHome()
        self.createBaseCircles()
        self.createTokens()
        self.generatePerson()

        # border around board
        pygame.draw.rect(self.gameDisplay, self.colours.BLACK, [self.size + self.boardOverall, self.size, self.boardLength*self.size, self.boardLength*self.size], 3)
        pygame.display.update()

    def createWhiteTile(self, xCoord, yCoord):
        # createself.colours.WHITE path
        pygame.draw.rect(self.gameDisplay,self.colours.WHITE, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
        pygame.draw.rect(self.gameDisplay, self.colours.BLACK, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size], 1)

    def createSafeTile(self, x_add, y_add, colour):
        tileType = 'safe'
        translated_star_path = [[x + x_add, y + y_add] for [x, y] in self.star_path]
        pygame.draw.polygon(self.gameDisplay, colour, translated_star_path)

    def generatePerson(self):
        font = pygame.font.Font('freesansbold.ttf', 40)
        image = pygame.image.load(os.path.join("images", "redPlayer.png"))
        cropped_image = pygame.transform.scale(image, (200, 200))

        self.gameDisplay.blit(cropped_image, (40, 60))
        text = font.render(self.playerNames[0], True,self.colours.WHITE)
        textRect = text.get_rect()
        textRect.center = (140, 295)
        self.gameDisplay.blit(text, textRect)

        image = pygame.image.load(os.path.join("images", "yellowPlayer.png"))
        cropped_image = pygame.transform.scale(image, (200, 200))
        self.gameDisplay.blit(cropped_image, (40, 420))

        self.gameDisplay.blit(cropped_image, (40, 60))
        text = font.render(self.playerNames[1], True,self.colours.WHITE)
        textRect = text.get_rect()
        textRect.center = (140, 660)
        self.gameDisplay.blit(text, textRect)

        image = pygame.image.load(os.path.join("images", "bluePlayer.png"))
        cropped_image = pygame.transform.scale(image, (200, 200))
        self.gameDisplay.blit(cropped_image, (1160, 60))

        self.gameDisplay.blit(cropped_image, (40, 60))
        text = font.render(self.playerNames[2], True,self.colours.WHITE)
        textRect = text.get_rect()
        textRect.center = (1260, 295)
        self.gameDisplay.blit(text, textRect)

        image = pygame.image.load(os.path.join("images", "greenPlayer.png"))
        cropped_image = pygame.transform.scale(image, (200, 200))
        self.gameDisplay.blit(cropped_image, (1160, 420))

        self.gameDisplay.blit(cropped_image, (40, 60))
        text = font.render(self.playerNames[3], True,self.colours.WHITE)
        textRect = text.get_rect()
        textRect.center = (1260, 660)
        self.gameDisplay.blit(text, textRect)

        return [(275, 105), (1050, 105), (275, 470), (1050, 470)]

    def generateTiles(self):
        redLayer = greenLayer = blueLayer = yellowLayer = 0
        for yCoord in range(1, self.boardLength + 1):
            if yCoord in range(self.boardLength//2, 10):
                for xCoord in range(1, self.boardLength + 1):
                    # avoiding the base
                    if xCoord*self.size not in range(self.size*7, self.size*10):
                        tileType = "path"
                        # path - horizontal spaces
                        if xCoord*self.size in range(self.size, self.size*7):
                            redLayer += 1
                            if redLayer in self.redCounter:
                                self.createWhiteTile(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, self.colours.TEAM_RED2, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, self.colours.BLACK, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if redLayer == 2:
                                tileType = "safe"
                                self.createSafeTile(445, 281, self.colours.TEAM_RED2)
                            if redLayer == 15:
                                tileType = "safe"
                                self.createSafeTile(485, 360,self.colours.WHITE)
                            self.addTile(self.size*xCoord + self.boardOverall, self.size*xCoord + self.boardOverall + (self.size + 1), self.size*yCoord, self.size*yCoord + (self.size + 1), tileType, self.redPath, redLayer)

                        else:
                            greenLayer += 1
                            if greenLayer in self.greenCounter:
                                self.createWhiteTile(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, self.colours.TEAM_GREEN2, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, self.colours.BLACK, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if greenLayer == 17:
                                tileType = "safe"
                                self.createSafeTile(925, 360, self.colours.TEAM_GREEN2)
                            if greenLayer == 4:
                                tileType = "safe"
                                self.createSafeTile(885, 280,self.colours.WHITE)

                            self.addTile(self.size*xCoord + self.boardOverall, self.size*xCoord + self.boardOverall + (self.size + 1), self.size*yCoord, self.size*yCoord + (self.size + 1), tileType, self.greenPath, greenLayer)

            else:
                for xCoord in range(1, self.boardLength + 1):
                    if xCoord in range(0, self.boardLength//2) or xCoord in range(self.boardLength//2 + 3, self.boardLength + 1):
                        # home base
                        tileType = "base"
                        if yCoord in range(0, self.boardLength//2) and xCoord in range(0, self.boardLength//2):
                            # red base
                            pygame.draw.rect(self.gameDisplay, self.colours.TEAM_RED1, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(0, self.boardLength//2) and xCoord in range(self.boardLength//2 + 3, self.boardLength + 1):
                            # blue base
                            pygame.draw.rect(self.gameDisplay, self.colours.TEAM_BLUE1, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
                        elif yCoord in range(self.boardLength//2 + 3, self.boardLength + 1) and xCoord in range(0, self.boardLength//2):
                            # yellow base
                            pygame.draw.rect(self.gameDisplay, self.colours.TEAM_YELLOW1, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
                        else:
                            # green base
                            pygame.draw.rect(self.gameDisplay, self.colours.TEAM_GREEN1, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
                    else:
                        # path - verticalself.colours.WHITE spaces
                        tileType = "path"
                        if yCoord*self.size in range(self.size, self.size*7):
                            blueLayer += 1
                            if blueLayer in self.blueCounter:
                                self.createWhiteTile(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, self.colours.TEAM_BLUE2, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, self.colours.BLACK, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size], 1)
                            if blueLayer == 7:
                                tileType = "safe"
                                self.createSafeTile(650, 200,self.colours.WHITE)

                            if blueLayer == 6:
                                tileType = "safe"
                                self.createSafeTile(725, 80, self.colours.TEAM_BLUE2)
                            self.addTile(self.size*xCoord + self.boardOverall, self.size*xCoord + self.boardOverall + (self.size + 1), self.size*yCoord, self.size*yCoord + (self.size + 1), tileType, self.bluePath, blueLayer)

                        else:
                            yellowLayer += 1
                            if yellowLayer in self.yellowCounter:
                                self.createWhiteTile(xCoord, yCoord)
                            else:
                                pygame.draw.rect(self.gameDisplay, self.colours.TEAM_YELLOW2, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size])
                                pygame.draw.rect(self.gameDisplay, self.colours.BLACK, [self.size*xCoord + self.boardOverall, self.size*yCoord, self.size, self.size], 1)

                            if yellowLayer == 13:
                                tileType = "safe"
                                self.createSafeTile(645, 560, self.colours.TEAM_YELLOW2)
                            if yellowLayer == 12:
                                tileType = "safe"
                                self.createSafeTile(725, 520,self.colours.WHITE)
                            self.addTile(self.size*xCoord + self.boardOverall, self.size*xCoord + self.boardOverall + (self.size + 1), self.size*yCoord, self.size*yCoord + (self.size + 1), tileType, self.yellowPath, yellowLayer)

    def addTile(self, xStartCoord, xEndCoord, yStartCoord, yEndCoord, tileType, path=[], myLayer=1):
        '''add tiles to dictionary {tile: (range x coordinate, range y coordinate)}'''
        currentTile = tile.Tile(range(xStartCoord, xEndCoord), range(yStartCoord, yEndCoord), tileType)
        path.append((currentTile, myLayer))
        self.tiles[currentTile] = (range(xStartCoord, xEndCoord), range(yStartCoord, yEndCoord))

    def createTriangleHome(self):
        # create triangle home
        pygame.draw.polygon(self.gameDisplay, self.colours.TEAM_RED2, [[self.size*7 + self.boardOverall, self.size*7], [705, 340], [self.size*7 + self.boardOverall, self.size*10]])
        pygame.draw.line(self.gameDisplay, self.colours.BLACK, (self.size*7 + self.boardOverall, self.size*10), (self.size*7 + self.boardOverall, self.size*7), 3)

        pygame.draw.polygon(self.gameDisplay, self.colours.TEAM_GREEN2, [[self.size*10 + self.boardOverall, self.size*10], [705, 340], [self.size*10 + self.boardOverall, self.size*7]])
        pygame.draw.line(self.gameDisplay, self.colours.BLACK, (self.size*10 + self.boardOverall, self.size*7), (self.size*10 + self.boardOverall, self.size*10), 3)

        pygame.draw.polygon(self.gameDisplay, self.colours.TEAM_BLUE2, [[self.size*7 + self.boardOverall, self.size*7], [705, 340], [self.size*10 + self.boardOverall, self.size*7]])
        pygame.draw.line(self.gameDisplay, self.colours.BLACK, (self.size*10 + self.boardOverall, self.size*7), (self.size*7 + self.boardOverall, self.size*7), 3)

        pygame.draw.polygon(self.gameDisplay, self.colours.TEAM_YELLOW2, [[self.size*10 + self.boardOverall, self.size*10], [705, 340], [self.size*7 + self.boardOverall, self.size*10]])
        pygame.draw.line(self.gameDisplay, self.colours.BLACK, (self.size*7 + self.boardOverall, self.size*10), (self.size*10 + self.boardOverall, self.size*10), 3)

    def createTokens(self):
        # RED

        redPathWithoutWhite = [(tile, count) for tile, count in self.redPath if count not in self.redCounter1]
        yellowPathWithoutWhite = [(tile, count) for tile, count in self.yellowPath if count not in self.yellowCounter1]
        greenPathWithoutWhite = [(tile, count) for tile, count in self.greenPath if count not in self.greenCounter1]
        bluePathWithoutWhite = [(tile, count) for tile, count in self.bluePath if count not in self.blueCounter1]

        # The [0] represents the base
        trueRedPath = [0] + redPathWithoutWhite[1:6] + bluePathWithoutWhite[::-1][1:len(bluePathWithoutWhite)-3:2] + bluePathWithoutWhite[0:3] + bluePathWithoutWhite[4::2] + greenPathWithoutWhite[:7] + greenPathWithoutWhite[7:][::-1] + yellowPathWithoutWhite[1:-1:2][0:-1] + yellowPathWithoutWhite[12:13] + yellowPathWithoutWhite[11:12] + yellowPathWithoutWhite[::-2][1:] + self.redPath[::-1][:7] + self.redPath[7:13]
        trueYellowPath = [0] + yellowPathWithoutWhite[::-1][4:][::2] + redPathWithoutWhite[::-1][:6] + redPathWithoutWhite[6:7] + redPathWithoutWhite[:6] + bluePathWithoutWhite[::-1][1:len(bluePathWithoutWhite)-3:2] + bluePathWithoutWhite[0:3] + bluePathWithoutWhite[4::2] + greenPathWithoutWhite[:7] + greenPathWithoutWhite[7:][::-1] + self.yellowPath[2:][::3] + self.yellowPath[1::3][::-1]
        trueGreenPath = [0] + greenPathWithoutWhite[::-1][1:6] + yellowPathWithoutWhite[1:-1:2][0:-1] + yellowPathWithoutWhite[12:13] + yellowPathWithoutWhite[11:12] + yellowPathWithoutWhite[::-2][1:] + redPathWithoutWhite[::-1][:6] + redPathWithoutWhite[6:7] + redPathWithoutWhite[:6] + bluePathWithoutWhite[3::2][::-1] + bluePathWithoutWhite[:4] + bluePathWithoutWhite[::2][2:] + self.greenPath[:6] + self.greenPath[6:12][::-1]
        trueBluePath = [0] + bluePathWithoutWhite[4::2] + greenPathWithoutWhite[:7] + greenPathWithoutWhite[7:][::-1] + yellowPathWithoutWhite[1:-1:2][0:-1] + yellowPathWithoutWhite[12:13] + yellowPathWithoutWhite[11:12] + yellowPathWithoutWhite[::-2][1:] + redPathWithoutWhite[::-1][:6] + redPathWithoutWhite[6:7] + redPathWithoutWhite[:6] + self.bluePath[::3][::-1] + self.bluePath[1::3]
        
        translated_token_path = [[x + 515, y + 60] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.RED_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        R1 = TokenCreate(1, self.colours.RED_TOKEN, None, (range(515, 515 + 61), range(60, 60 + 61)), (515, 60), trueRedPath, (645, 280))

        translated_token_path = [[x + 430, y + 150] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.RED_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        R2 = TokenCreate(2, self.colours.RED_TOKEN, None, (range(430, 430 + 61), range(150, 150 + 61)), (430, 150), trueRedPath, (650, 315))

        translated_token_path = [[x + 585,  y + 150] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.RED_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        R3 = TokenCreate(3, self.colours.RED_TOKEN, None, (range(585, 585 + 61), range(150, 150 + 61)), (585, 150), trueRedPath, (645, 350))

        translated_token_path = [[x + 515, y + 220] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.RED_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        R4 = TokenCreate(4, self.colours.RED_TOKEN, None, (range(515, 515 + 61), range(220, + 220 + 61)), (515, 220), trueRedPath, (675, 315))

        self.redTokens = [R1, R2, R3, R4]

        # YELLOW

        translated_token_path = [[x + 510, y + 420] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.YELLOW_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        Y1 = TokenCreate(1, self.colours.YELLOW_TOKEN,  None, (range(510, 510 + 61), range(420, 420 + 61)), (510, 420), trueYellowPath, (690, 340))

        translated_token_path = [[x + 430, y + 500] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay,  self.colours.YELLOW_TOKEN,  translated_token_path)
        pygame.draw.polygon(self.gameDisplay,  self.colours.BLACK,  translated_token_path, 1)
        Y2 = TokenCreate(2, self.colours.YELLOW_TOKEN,  None, (range(430, 430 + 61), range(500, 500 + 61)), (430, 500), trueYellowPath, (665, 365))

        translated_token_path = [[x + 590, y + 500] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.YELLOW_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        Y3 = TokenCreate(3, self.colours.YELLOW_TOKEN, None, (range(590, 590 + 61), range(500, 500 + 61)), (590, 500), trueYellowPath, (690, 365))

        translated_token_path = [[x + 514, y + 580] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.YELLOW_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        Y4 = TokenCreate(4, self.colours.YELLOW_TOKEN, None, (range(514, 514 + 61), range(580, 580 + 61)), (514, 580), trueYellowPath, (715, 370))

        self.yellowTokens = [Y1, Y2, Y3, Y4]

        translated_token_path = [[x + 860, y + 60] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.BLUE_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        B1 = TokenCreate(1, self.colours.BLUE_TOKEN, None, (range(860, 860 + 61), range(60, 60 + 61)), (860, 60), trueBluePath, (690, 300))

        translated_token_path = [[x + 785, y + 140] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.BLUE_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        B2 = TokenCreate(2, self.colours.BLUE_TOKEN, None, (range(785, 785 + 61), range(140, 140 + 61)), (785, 140), trueBluePath, (665, 280))

        translated_token_path = [[x + 940, y + 145] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.BLUE_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        B3 = TokenCreate(3, self.colours.BLUE_TOKEN, None, (range(940, 940 + 61), range(145, 145 + 61)), (940, 145), trueBluePath, (715, 280))

        translated_token_path = [[x + 860, y + 220] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.BLUE_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        B4 = TokenCreate(4, self.colours.BLUE_TOKEN, None, (range(860, 860 + 61), range(220, 220 + 61)), (860, 220), trueBluePath, (690, 280))

        self.blueTokens = [B1, B2, B3, B4]

        # GREEN
        translated_token_path = [[x + 860, y + 420] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.GREEN_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        G1 = TokenCreate(1, self.colours.GREEN_TOKEN, None, (range(860, 860 + 61), range(420, 420 + 61)), (860, 420), trueGreenPath, (740, 280))

        translated_token_path = [[x + 790, y + 500] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.GREEN_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        G2 = TokenCreate(2, self.colours.GREEN_TOKEN, None, (range(790, 790 + 61), range(500, 500 + 61)), (790, 500), trueGreenPath, (740, 315))

        translated_token_path = [[x + 940, y + 500] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.GREEN_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        G3 = TokenCreate(3, self.colours.GREEN_TOKEN, None, (range(940, 940 + 61), range(500, 500 + 61)), (940, 500), trueGreenPath, (740, 350))

        translated_token_path = [[x + 860, y + 570] for [x, y] in self.token_path]
        pygame.draw.polygon(self.gameDisplay, self.colours.GREEN_TOKEN, translated_token_path)
        pygame.draw.polygon(self.gameDisplay, self.colours.BLACK, translated_token_path, 1)
        G4 = TokenCreate(4, self.colours.GREEN_TOKEN, None, (range(860, 860 + 61), range(570, 570 + 61)), (860, 570), trueGreenPath, (715, 315))

        self.greenTokens = [G1, G2, G3, G4]

    def createBaseCircles(self):
        # create base circles
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_RED2, (530, 80), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_RED2, (450, 170), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_RED2, (605, 170), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_RED2, (530, 240), 25)

        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_GREEN2, (880, 440), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_GREEN2, (805, 515), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_GREEN2, (960, 515), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_GREEN2, (880, 590), 25)

        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_YELLOW2, (530, 440), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_YELLOW2, (450, 515), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_YELLOW2, (605, 515), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_YELLOW2, (530, 600), 25)

        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_BLUE2, (880, 80), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_BLUE2, (805, 160), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_BLUE2, (960, 160), 25)
        pygame.draw.circle(self.gameDisplay, self.colours.TEAM_BLUE2, (880, 240), 25)
