import pygame
import datetime
import copy
import os

from board import Board
from player import Player
import button

# team colours
TEAM_BLUE1 = 209, 230, 238
TEAM_BLUE2 = 65, 179, 226
BLUE_TOKEN = 77, 5, 232, 1

TEAM_YELLOW1 = 200, 189, 161
TEAM_YELLOW2 = 251, 217, 132
YELLOW_TOKEN = 247, 202, 24, 1

TEAM_RED1 = 245, 221, 219
TEAM_RED2 = 241, 120, 107
RED_TOKEN = 189, 9, 9

TEAM_GREEN1 = 190, 235, 224
TEAM_GREEN2 = 90, 200, 174
GREEN_TOKEN = 30, 130, 76, 1

tokenPoly = [[27.5, 30.5], [27.0, 30.5], [27.0, 26.5], [23.5, 14.5], [23.5, 14.5], [24.5, 13.5], [24.5, 13.0], [23.5, 12.0], [23.5, 12.0], [25.5, 7.0], [18.5, 0.0], [11.0, 7.0], [13.5, 12.0], [13.0, 12.0], [12.0, 13.0], [12.0, 13.5], [13.0, 14.5], [13.5, 14.5], [10.0, 26.5], [10.0, 30.5], [9.0, 30.5], [8.0, 31.5], [8.0, 34.0], [9.0, 35.0], [9.0, 35.0], [9.0, 37.0], [27.5, 37.0], [27.5, 35.0], [28.5, 34.0], [28.5, 31.5], [27.5, 30.5]]

BLACK = 0, 0, 0
BLUE = (12, 63, 186)
GREEN = (0, 179, 0)
YELLOW = (179, 179, 0)
RED = (242, 120, 107)

class Game:
    def __init__(self):
        self.startTime = datetime.datetime.now()
        self.endTime = None
        self.gameExit = False

        self.players = None

        self.playerRed = None
        self.playerBlue = None
        self.playerGreen = None
        self.playerYellow = None

        self.board = None
        self.currentPlayer = None
        self.currentRoll = None
        self.diceDict = {1: "one.png", 2: "two.png", 3: "three.png", 4: "four.png", 5: "five.png", 6: "six.png"}
        self.text = None
        self.font = None

    def endGame(self):
        self.endTime = datetime.datetime.now()
        self.gameExit = True

    def isPlayerChoosingOwnToken(self, x, y):
        print(x, y)
        return self.currentPlayer.chooseToken(x, y)

    def createPlayers(self, playerNames=["joi","alex","john","dale"]):
        diceValues = self.board.generatePerson()

        self.playerRed = Player(playerNames[0], RED_TOKEN, [], self.board.redTokens, [],  self.board.redTokens)
        for token in self.board.redTokens:
            token.setPlayerOwner(self.playerRed)

        self.playerRed.myDice.setCoordinates(diceValues[0])


        self.playerYellow = Player(playerNames[1], YELLOW_TOKEN, [], self.board.yellowTokens, [],  self.board.yellowTokens)
        for token in self.board.yellowTokens:
            token.setPlayerOwner(self.playerYellow)

        self.playerYellow.myDice.setCoordinates(diceValues[2])

        self.playerBlue = Player(playerNames[2], BLUE_TOKEN, [], self.board.blueTokens, [],  self.board.blueTokens)
        for token in self.board.blueTokens:
            token.setPlayerOwner(self.playerBlue)

        self.playerBlue.myDice.setCoordinates(diceValues[1])


        self.playerGreen = Player(playerNames[3], GREEN_TOKEN, [], self.board.greenTokens, [],  self.board.greenTokens)

        for token in self.board.greenTokens:
            token.setPlayerOwner(self.playerGreen)

        self.playerGreen.myDice.setCoordinates(diceValues[3])

        self.players = [self.playerRed, self.playerBlue, self.playerGreen, self.playerYellow]

    def produceDiceImage(self):
        for dice in self.diceDict.values():
            self.board.regenerateBoard(self.text)
            image = pygame.image.load(os.path.join("images", "dice", dice))
            cropped_image = pygame.transform.scale(image, (80, 80))
            self.board.gameDisplay.blit(cropped_image, (self.currentPlayer.myDice.coOrdinates[0], self.currentPlayer.myDice.coOrdinates[1]))
            for player in self.players:
                for token in player.allTokens:
                    token.drawToken(self.board)
            pygame.time.delay(40)
            pygame.display.update()

        self.board.regenerateBoard(self.text)
        image = pygame.image.load(os.path.join("images", "dice", self.diceDict[self.currentRoll]))
        cropped_image = pygame.transform.scale(image, (80, 80))
        self.board.gameDisplay.blit(cropped_image, (self.currentPlayer.myDice.coOrdinates[0], self.currentPlayer.myDice.coOrdinates[1]))

        for player in self.players:
            for token in player.allTokens:
                token.drawToken(self.board)
        pygame.display.update()

    def highlightPlayerTurn(self, first=None):
        cropped_image = pygame.image.load(os.path.join("images", "dice", "theirTurn.jpg"))
        cropped_image = pygame.transform.scale(cropped_image, (80, 80))
        if self.currentPlayer is not None:
            self.board.gameDisplay.blit(cropped_image, (self.currentPlayer.myDice.coOrdinates[0], self.currentPlayer.myDice.coOrdinates[1]))
        else:
            self.board.gameDisplay.blit(cropped_image, (self.players[0].myDice.coOrdinates[0], self.players[0].myDice.coOrdinates[1]))
        if not first:
            for player in self.players:
                for token in player.allTokens:
                    token.drawToken(self.board)

        pygame.display.update()

    def playerToRollDice(self):
        validDice = False
        while not validDice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    if not validDice:
                        if x in range(self.currentPlayer.myDice.coOrdinates[0], self.currentPlayer.myDice.coOrdinates[0]+80+1) and y in range(self.currentPlayer.myDice.coOrdinates[1], self.currentPlayer.myDice.coOrdinates[1]+80+1):
                            self.currentRoll = self.currentPlayer.rollDice()
                            self.produceDiceImage()
                            validDice = True
                            # print("success")
                        else:
                            self.text = "Not Dice"
                            print(self.text)
                            text = self.font.render(self.text, True, BLACK)
                            textRect = text.get_rect()
                            textRect.center = (700, 750)
                            self.board.gameDisplay.blit(text, textRect)
                            pygame.display.update()
        return self.currentRoll, validDice

    def playerChoosingToken(self):
        validToken = False
        while not validToken:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # print(x, y)
                    currentToken = self.isPlayerChoosingOwnToken(x, y)
                    if currentToken is not None:
                        validToken = True
                    else:
                        self.text = "Not valid token"
                        text = self.font.render(self.text, True, BLACK)
                        textRect = text.get_rect()
                        textRect.center = (700, 750)
                        self.board.gameDisplay.blit(text, textRect)
                        pygame.display.update()
        return currentToken

    def checkIfBlocked(self, tile):
        if tile.blockedBy is not None and self.currentPlayer != tile.blockedBy:
            self.text = "Choose another token, this tile is blocked by: {}".format(tile.blockedBy.playerName)
            text = self.font.render(self.text, True, BLACK)
            textRect = text.get_rect()
            textRect.center = (700, 750)
            self.board.gameDisplay.blit(text, textRect)
            return True
        return False

    def checkIfCanFormBlock(self, tile):
        if len(tile.residents) > 1:
            if tile.checkResidents().count(self.currentPlayer) > 1 and not tile.isBlocked:
                tile.formBlock(self.currentPlayer)

    def checkIfCanEatToken(self, tile):
        if len(tile.residents) == 2 and self.currentPlayer != tile.residents[0].playerOwner:
            eatenToken = tile.residents[0]
            if tile.tileType == "safe":
                return
            else:
                self.text = "{}'s token eats {}'s token".format(self.currentPlayer.playerName, eatenToken.playerOwner.playerName)
                tile.residents.remove(eatenToken)
                eatenToken.playerOwner.tokensOnBase.append(eatenToken)
                eatenToken.playerOwner.tokensOnPath.remove(eatenToken)
                eatenToken.setCurrentTilePathPosition(0)
                eatenToken.setTokenLocation((range(eatenToken.xBaseCoord, eatenToken.xBaseCoord+61), range(eatenToken.yBaseCoord, eatenToken.yBaseCoord+61)))
                eatenToken.drawToken(self.board)

    def adjustTokenLocations(self, newTokenTilePosition, currentToken):
        if newTokenTilePosition != "home":
            if newTokenTilePosition.tileType == 'path' or newTokenTilePosition.tileType == 'safe':
                if currentToken not in self.currentPlayer.tokensOnPath:
                    self.currentPlayer.tokensOnPath.append(currentToken)
                    if currentToken in self.currentPlayer.tokensOnBase:
                        self.currentPlayer.tokensOnBase.remove(currentToken)
                    elif currentToken in self.currentPlayer.tokensOnHome:
                        self.currentPlayer.tokensOnHome.remove(currentToken)

            elif newTokenTilePosition.tileType == 'base':
                if currentToken not in self.currentPlayer.tokensOnBase:
                    self.currentPlayer.tokensOnBase.append(currentToken)
                    if currentToken in self.currentPlayer.tokensOnHome:
                        self.currentPlayer.tokensOnHome.remove(currentToken)
                    elif currentToken in self.currentPlayer.tokensOnPath:
                        self.currentPlayer.tokensOnPath.remove(currentToken)

        else:
            if currentToken not in self.currentPlayer.tokensOnHome:
                self.currentPlayer.tokensOnHome.append(currentToken)
                if currentToken in self.currentPlayer.tokensOnPath:
                    self.currentPlayer.tokensOnPath.remove(currentToken)

    def moveTokenFromBase(self, token):
        self.currentRoll = 1
        newPos = token.tokenNewTile(self.currentRoll)
        self.updateTokenTilePos(token, newPos)
        self.updateBoardWithMovingToken(token, newPos)

    def updateTokenTilePos(self, currentToken, tile):
        self.adjustTokenLocations(tile, currentToken)
        try:
            tile.residents.append(currentToken)
        except:
            pass

    def loadStart(self):
        pygame.init()
        size = width, height = 1400, 800
        screen = pygame.display.set_mode(size)
        image = pygame.image.load("images/background.jpg").convert()
        screen.blit(image, [0, 0])

        b1 = button.Button(screen, GREEN, 200, 300, 320, 65, "Create Game")
        b2 = button.Button(screen, YELLOW, 200, 450, 320, 65, "Join Game")

        running = True
        while running:
            pygame.display.update()
            pos = pygame.mouse.get_pos()
            b1.isOver(pos)
            b2.isOver(pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if b1.click_b(event, pos):
                    running = False
                if b2.click_b(event, pos):
                    running = False
        # pregame page
        screen = pygame.display.set_mode(size)
        image = pygame.image.load("images/background.jpg").convert()
        screen.blit(image, [0, 0])

        heading = button.Button(screen, GREEN, 535, 225, 320, 65, "Start Game")
        player1 = button.Button(screen, RED, 370, 370, 200, 50, input("Please input a name of player 1\n"))
        player2 = button.Button(screen, BLUE, 710, 370, 200, 50, input("Please input a name of player 2\n"))
        player3 = button.Button(screen, YELLOW, 370, 510, 200, 50, input("Please input a name of player 3\n"))
        player4 = button.Button(screen, GREEN, 710, 510, 200, 50, input("Please input a name of player 4\n"))

        running = True
        while running:
            pygame.display.update()
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (191, 191, 191), (350, 200, 700, 400))
            heading.isOver(pos)
            player1.isOver(pos)
            player2.isOver(pos)
            player3.isOver(pos)
            player4.isOver(pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if heading.click_b(event, pos):
                    running = False
        return [player1.text,player2.text,player3.text,player4.text]

    def main(self):
        pygame.init()
        counter = 0
        # playerNames = self.loadStart()
        self.board = Board()
        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.board.createBoard()
        self.createPlayers()
        validDice = False
        first = True
        self.currentPlayer = self.players[counter % 4]
        self.text = "Turn #{}: {}".format(counter, self.currentPlayer.playerName)
        text = self.font.render(self.text, True, BLACK)
        textRect = text.get_rect()
        textRect.center = (700, 700)
        self.board.gameDisplay.blit(text, textRect)
        while not self.gameExit:
            self.currentPlayer = self.players[counter % 4]
            self.text = "Turn #{}: {}".format(counter, self.currentPlayer.playerName)
            text = self.font.render(self.text, True, BLACK)
            textRect = text.get_rect()
            textRect.center = (700, 700)
            first = self.highlightPlayerTurn(first)
            # return here
            self.currentRoll, validDice = self.playerToRollDice()

            if len(self.currentPlayer.tokensOnHome) == 4:
                self.text = "{} won the game!!".format(self.currentPlayer.playerName)
                self.gameExit = True

            elif len(self.currentPlayer.tokensOnBase) == 4 and self.currentRoll == 6:
                self.moveTokenFromBase(self.currentPlayer.tokensOnBase[0])
                self.text = "{} token #{} moved from base".format(self.currentPlayer.playerName, 4 - len(self.currentPlayer.tokensOnBase))
                text = self.font.render(self.text, True, BLACK)
                textRect = text.get_rect()
                textRect.center = (700, 700)
                self.board.gameDisplay.blit(text, textRect)
            elif 0 < len(self.currentPlayer.tokensOnPath) <= 4:
                tokenChosen = False
                while not tokenChosen:
                    currentToken = self.playerChoosingToken()
                    if currentToken.currentTilePathPosition == 0:
                        if self.currentRoll != 6:
                            self.text = "Cannot move token from base."
                            text = self.font.render(self.text, True, BLACK)
                            textRect = text.get_rect()
                            textRect.center = (700, 700)
                            self.board.gameDisplay.blit(text, textRect)
                            continue
                        else:
                            self.moveTokenFromBase(currentToken)
                            self.text = "{} token #{} moved from base\nGets another turn".format(self.currentPlayer.playerName, 4 - len(self.currentPlayer.tokensOnBase))
                            text = self.font.render(self.text, True, BLACK)
                            textRect = text.get_rect()
                            textRect.center = (700, 700)
                            self.board.gameDisplay.blit(text, textRect)
                            counter -= 1
                            break

                    currentTilePosition = None
                    if currentToken.currentTilePathPosition > 0:
                        currentTilePosition = currentToken.tokenTilesPath[currentToken.currentTilePathPosition][0]
                        if currentTilePosition is not None and self.checkIfBlocked(currentTilePosition):
                            continue
                        currentTilePosition.residents.remove(currentToken)

                    tokenChosen = True
                if tokenChosen:
                    if currentToken.currentTilePathPosition + self.currentRoll < 57:
                        newTokenTilePosition = currentToken.tokenNewTile(self.currentRoll)
                        self.updateTokenTilePos(currentToken, newTokenTilePosition)
                        self.checkIfCanFormBlock(newTokenTilePosition)
                        if currentTilePosition is not None:
                            currentTilePosition.checkIfCanDestroyBlock(self.currentPlayer)
                            self.checkIfCanEatToken(newTokenTilePosition)
                        self.updateBoardWithMovingToken(currentToken, newTokenTilePosition)
                    elif currentToken.currentTilePathPosition + self.currentRoll >= 57:
                            print("teST")
                            tempPlayers = copy.copy(self.players)
                            tempPlayers.remove(self.currentPlayer)
                            print("CURRENT:", currentToken.currentTilePathPosition)
                            self.currentRoll = 3
                            if currentToken.currentTilePathPosition + self.currentRoll == 57:
                                currentToken.drawTokenOnHome(self.board, currentToken.currentTilePathPosition, self.currentRoll, tempPlayers)
                                currentToken.setTokenLocation(None)
                                if currentToken not in self.currentPlayer.tokensOnHome:
                                    self.currentPlayer.tokensOnHome.append(currentToken)
                                    if currentToken in self.currentPlayer.tokensOnPath:
                                        self.currentPlayer.tokensOnPath.remove(currentToken)
                                self.currentPlayer.setAllTokens(self.currentPlayer.tokensOnBase+self.currentPlayer.tokensOnPath+self.currentPlayer.tokensOnHome)
                            elif currentToken.currentTilePathPosition + self.currentRoll > 57:
                                print("NEWTILE: ", self.currentRoll+currentToken.currentTilePathPosition)
                                forwardSteps = 57 - currentToken.currentTilePathPosition
                                print("FORWARD STEPS:", forwardSteps)
                                # TODO: forward steps +1 because home
                                print("BACK STEPS:", self.currentRoll-forwardSteps)
                                backSteps = self.currentRoll-forwardSteps
                                self.updateBoardWithBackwardMovingToken(currentToken, forwardSteps, backSteps)

                self.text = "Next: {}".format(self.currentPlayer.playerName)

                text = self.font.render(self.text, True, BLACK)
                textRect = text.get_rect()
                textRect.center = (700, 700)
                self.board.gameDisplay.blit(text, textRect)
            counter += 1

        pygame.quit()
        quit()

    def updateBoardWithMovingToken(self, currentToken, newTokenTilePosition):
        tempPlayers = copy.copy(self.players)
        tempPlayers.remove(self.currentPlayer)
        self.currentPlayer.moveChosenToken(self.board, currentToken, self.currentRoll, tempPlayers)
        currentToken.setTokenLocation(newTokenTilePosition.rangeCoordinates)
        self.currentPlayer.setAllTokens(self.currentPlayer.tokensOnBase+self.currentPlayer.tokensOnPath+self.currentPlayer.tokensOnHome)

    def updateBoardWithBackwardMovingToken(self, currentToken, forwardSteps, backSteps):
        tempPlayers = copy.copy(self.players)
        tempPlayers.remove(self.currentPlayer)
        newTile = self.currentPlayer.moveBackwardChosenToken(self.board, currentToken, forwardSteps, backSteps, tempPlayers)
        self.currentPlayer.setAllTokens(self.currentPlayer.tokensOnBase+self.currentPlayer.tokensOnPath+self.currentPlayer.tokensOnHome)
        if newTile.tileType == "path" or newTile.tileType == "safe":
            if currentToken not in self.currentPlayer.tokensOnPath:
                self.currentPlayer.tokensOnPath.append(currentToken)


playing = Game()
playing.main()
