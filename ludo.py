import pygame
import datetime
import copy
import os

from board import Board
from player import Player
from gameColours import GameColours
import button



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

        self.gamecolours = None

    def endGame(self):
        self.endTime = datetime.datetime.now()
        self.gameExit = True

    def showMainText(self):
        text = self.font.render(self.text, True, self.gamecolours.BLACK)
        textRect = text.get_rect()
        textRect.center = (700, 700)
        self.board.gameDisplay.blit(text, textRect)

    def showInvalidClickText(self):
        text = self.font.render(self.text, True, self.gamecolours.BLACK)
        textRect = text.get_rect()
        textRect.center = (700, 670)
        self.board.gameDisplay.blit(text, textRect)

    def showSubText(self):
        text = self.font.render(self.text, True, self.gamecolours.BLACK)
        textRect = text.get_rect()
        textRect.center = (700, 730)
        self.board.gameDisplay.blit(text, textRect)

    def showExtraTurnText(self):
        text = self.font.render(self.text, True, self.gamecolours.BLACK)
        textRect = text.get_rect()
        textRect.center = (700, 770)
        self.board.gameDisplay.blit(text, textRect)

    def isPlayerChoosingOwnToken(self, x, y):
        return self.currentPlayer.chooseToken(x, y)

    def createPlayers(self, playerNames):
        diceValues = self.board.generatePerson()

        self.playerRed = Player(playerNames[0], self.gamecolours.TEAM_RED2, [], self.board.redTokens, [],  self.board.redTokens)
        for token in self.board.redTokens:
            token.setPlayerOwner(self.playerRed)

        self.playerRed.myDice.setCoordinates(diceValues[0])

        self.playerYellow = Player(playerNames[1], self.gamecolours.YELLOW_TOKEN, [], self.board.yellowTokens, [],  self.board.yellowTokens)
        for token in self.board.yellowTokens:
            token.setPlayerOwner(self.playerYellow)

        self.playerYellow.myDice.setCoordinates(diceValues[2])

        self.playerBlue = Player(playerNames[2], self.gamecolours.BLUE_TOKEN, [], self.board.blueTokens, [],  self.board.blueTokens)
        for token in self.board.blueTokens:
            token.setPlayerOwner(self.playerBlue)

        self.playerBlue.myDice.setCoordinates(diceValues[1])

        self.playerGreen = Player(playerNames[3], self.gamecolours.GREEN_TOKEN, [], self.board.greenTokens, [],  self.board.greenTokens)

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
                    if not validDice:
                        if x in range(self.currentPlayer.myDice.coOrdinates[0], self.currentPlayer.myDice.coOrdinates[0]+80+1) and y in range(self.currentPlayer.myDice.coOrdinates[1], self.currentPlayer.myDice.coOrdinates[1]+80+1):
                            self.currentRoll = self.currentPlayer.rollDice()
                            self.produceDiceImage()
                            validDice = True
                        else:
                            self.text = "Not Dice"
                            self.showInvalidClickText()
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
                    currentToken = self.isPlayerChoosingOwnToken(x, y)
                    if currentToken is not None:
                        validToken = True
                    else:
                        self.text = "Not valid token"
                        text = self.font.render(self.text, True, self.gamecolours.BLACK)
                        self.showInvalidClickText()
        return currentToken

    def checkIfBlocked(self, tile):
        if tile.blockedBy is not None and self.currentPlayer != tile.blockedBy:
            self.text = "Choose another token, this tile is blocked by: {}".format(tile.blockedBy.playerName)
            self.showSubText()
            return True
        return False

    def checkIfCanFormBlock(self, tile):
        if len(tile.residents) > 1:
            if tile.checkResidents().count(self.currentPlayer) > 1 and not tile.isBlocked:
                self.text = tile.formBlock(self.currentPlayer)
                self.showMainText()

    def checkIfCanEatToken(self, tile):
        if len(tile.residents) == 2 and self.currentPlayer != tile.residents[0].playerOwner:
            eatenToken = tile.residents[0]
            if tile.tileType == "safe":
                return
            else:
                self.text = "{}'s token eats {}'s token".format(self.currentPlayer.playerName, eatenToken.playerOwner.playerName)
                self.showMainText()
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
        self.gamecolours = GameColours()
        pygame.init()
        size = width, height = 1400, 800
        screen = pygame.display.set_mode(size)
        image = pygame.image.load("images/background.jpg").convert()
        screen.blit(image, [0, 0])

        b1 = button.Button(screen, self.gamecolours.GREEN, 200, 300, 320, 65, "Create Game")
        b2 = button.Button(screen, self.gamecolours.YELLOW, 200, 450, 320, 65, "Join Game")

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

        heading = button.Button(screen, self.gamecolours.GREEN, 535, 225, 320, 65, "Start Game")
        player1 = button.Button(screen, self.gamecolours.RED, 370, 370, 200, 50, input("Please input a name of player 1\n"))
        player2 = button.Button(screen, self.gamecolours.BLUE, 710, 370, 200, 50, input("Please input a name of player 2\n"))
        player3 = button.Button(screen, self.gamecolours.YELLOW, 370, 510, 200, 50, input("Please input a name of player 3\n"))
        player4 = button.Button(screen, self.gamecolours.GREEN, 710, 510, 200, 50, input("Please input a name of player 4\n"))

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
        return [player1.text, player2.text, player3.text, player4.text]

    def main(self):
        pygame.init()
        counter = 0
        playerNames = self.loadStart()
        self.board = Board(playerNames)
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.board.createBoard()
        self.createPlayers(playerNames)
        validDice = False
        first = True
        self.currentPlayer = self.players[counter % 4]
        self.text = "Turn #{}: {}".format(counter, self.currentPlayer.playerName)
        self.showSubText()
        while not self.gameExit:
            self.currentPlayer = self.players[counter % 4]
            self.text = "Turn #{}: {}".format(counter, self.currentPlayer.playerName)
            self.showSubText()
            first = self.highlightPlayerTurn(first)
            # return here
            self.currentRoll, validDice = self.playerToRollDice()

            if len(self.currentPlayer.tokensOnHome) == 4:
                self.text = "{} won the game!!".format(self.currentPlayer.playerName)
                self.showMainText()
                self.gameExit = True

            elif len(self.currentPlayer.tokensOnBase) == 4 and self.currentRoll == 6:
                self.moveTokenFromBase(self.currentPlayer.tokensOnBase[0])
                self.text = "{} token #{} moved from base".format(self.currentPlayer.playerName, 4 - len(self.currentPlayer.tokensOnBase))
                self.showMainText()
            elif 0 < len(self.currentPlayer.tokensOnPath) <= 4:
                tokenChosen = False
                while not tokenChosen:
                    currentToken = self.playerChoosingToken()
                    if currentToken.currentTilePathPosition == 0:
                        if self.currentRoll != 6:
                            self.text = "Cannot move token from base."
                            self.showMainText()
                            continue
                        else:
                            self.moveTokenFromBase(currentToken)
                            self.text = "{} token #{} moved from base Gets another turn".format(self.currentPlayer.playerName, 4 - len(self.currentPlayer.tokensOnBase))
                            self.showExtraTurnText()
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
                            self.text = currentTilePosition.checkIfCanDestroyBlock(self.currentPlayer)
                            self.showMainText()
                            self.checkIfCanEatToken(newTokenTilePosition)
                        self.updateBoardWithMovingToken(currentToken, newTokenTilePosition)
                    elif currentToken.currentTilePathPosition + self.currentRoll >= 57:
                            tempPlayers = copy.copy(self.players)
                            tempPlayers.remove(self.currentPlayer)
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
                                forwardSteps = 57 - currentToken.currentTilePathPosition
                                backSteps = self.currentRoll-forwardSteps
                                self.updateBoardWithBackwardMovingToken(currentToken, forwardSteps, backSteps)

                self.text = "Next: {}".format(self.currentPlayer.playerName)

                self.showMainText()
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
