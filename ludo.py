import pygame
import datetime
import copy

from board import Board
from player import Player
import startup_page

import os
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
        self.diceDict = {1:"one.png",2:"two.png",3:"three.png",4:"four.png",5:"five.png",6:"six.png"}

    def endGame(self):
        self.endTime = datetime.datetime.now()
        self.gameExit = True

    def isPlayerChoosingOwnToken(self,x,y):
        return self.currentPlayer.chooseToken(x,y)

    def createPlayers(self):
        diceValues = self.board.generatePerson()

        self.playerRed = Player("Red",RED_TOKEN,[],self.board.redTokens,[], self.board.redTokens)
        for token in self.board.redTokens:
            token.setPlayerOwner(self.playerRed)

        self.playerRed.myDice.setCoordinates(diceValues[0])
        
        self.playerBlue = Player("Blue",BLUE_TOKEN,[],self.board.blueTokens,[], self.board.blueTokens)
        for token in self.board.blueTokens:
            token.setPlayerOwner(self.playerBlue)
        
        self.playerBlue.myDice.setCoordinates(diceValues[1])

        self.playerYellow = Player("Yellow",YELLOW_TOKEN,[],self.board.yellowTokens,[], self.board.yellowTokens)
        for token in self.board.yellowTokens:
            token.setPlayerOwner(self.playerYellow)

        self.playerYellow.myDice.setCoordinates(diceValues[2])

        self.playerGreen = Player("Green",GREEN_TOKEN,[],self.board.greenTokens,[], self.board.greenTokens)

        for token in self.board.greenTokens:
            token.setPlayerOwner(self.playerGreen)

        self.playerGreen.myDice.setCoordinates(diceValues[3])

        self.players = [self.playerRed,self.playerBlue,self.playerGreen,self.playerYellow]

    def produceDiceImage(self):
        self.board.regenerateBoard()
        image = pygame.image.load(os.path.join("dice",self.diceDict[self.currentRoll]))
        cropped_image = pygame.transform.scale(image,(80,80))
        # image = pygame.image.load(os.path.join("dice",self.diceDict[self.currentRoll]))
        self.board.gameDisplay.blit(cropped_image,(self.currentPlayer.myDice.coOrdinates[0],self.currentPlayer.myDice.coOrdinates[1]))

        for player in self.players:
            for token in player.allTokens:
                token.drawToken(self.board)
        pygame.display.update()


    def highlightPlayerTurn(self,first=None):
        image = pygame.image.load(os.path.join("dice","theirTurn.jpg"))
        cropped_image = pygame.transform.scale(image,(80,80))
        if self.currentPlayer != None:
            self.board.gameDisplay.blit(cropped_image,(self.currentPlayer.myDice.coOrdinates[0],self.currentPlayer.myDice.coOrdinates[1]))
        else:
            self.board.gameDisplay.blit(cropped_image,(self.players[0].myDice.coOrdinates[0],self.players[0].myDice.coOrdinates[1]))
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
                    x,y = pygame.mouse.get_pos()
                    if not validDice:
                        if x in range(self.currentPlayer.myDice.coOrdinates[0],self.currentPlayer.myDice.coOrdinates[0]+80+1) and y in range(self.currentPlayer.myDice.coOrdinates[1],self.currentPlayer.myDice.coOrdinates[1]+80+1):
                            self.currentRoll = self.currentPlayer.rollDice()
                            self.produceDiceImage()
                            validDice = True
                            print("success")
                        else:
                            print("Not Dice")

        return self.currentRoll, validDice

    def playerChoosingToken(self):
        validToken = False
        while not validToken:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    print(x,y)
                    currentToken = self.isPlayerChoosingOwnToken(x,y)
                    if currentToken != None:
                        validToken = True
                        print("success")
                    else:
                        print("Not valid token")
        return currentToken

    def main(self):
        pygame.init()

        counter = 0
        startup_page.loadStart()
        self.board = Board()
        self.board.createBoard()
        self.createPlayers()
        validDice = False
        first = True
        while not self.gameExit:

            
            self.currentPlayer = self.players[counter%4]

            first = self.highlightPlayerTurn(first)
            self.currentRoll, validDice = self.playerToRollDice()
            currentToken =self.playerChoosingToken()
            if currentToken.currentTilePathPosition > 0:
                # TODO: fix this tuple
                currentTilePosition = currentToken.tokenTilesPath[currentToken.currentTilePathPosition][0]
                currentTilePosition.residents.remove(currentToken)

            newTokenTilePosition = currentToken.tokenNewTile(self.currentRoll)
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

            elif newTokenTilePosition.tileType == 'home':
                if currentToken not in self.currentPlayer.tokensOnHome:
                    self.currentPlayer.tokensOnHome.append(currentToken)
                    if currentToken in self.currentPlayer.tokensOnPath:
                        self.currentPlayer.tokensOnPath.remove(currentToken)
                    elif currentToken in self.currentPlayer.tokensOnBase:
                        self.currentPlayer.tokensOnBase.remove(currentToken)
            newTokenTilePosition.residents.append(currentToken)
            self.updateBoardWithMovingToken(currentToken,newTokenTilePosition)

            counter += 1
            print("Next: {}".format(self.players[counter%4].colour))
        pygame.quit()
        quit()

    def updateBoardWithMovingToken(self,currentToken,newTokenTilePosition):
        tempPlayers = copy.copy(self.players)
        tempPlayers.remove(self.currentPlayer)
        self.currentPlayer.moveChosenToken(self.board,currentToken,self.currentRoll,tempPlayers)
        currentToken.setTokenLocation(newTokenTilePosition.rangeCoordinates)
        self.currentPlayer.setAllTokens(self.currentPlayer.tokensOnBase+self.currentPlayer.tokensOnPath+self.currentPlayer.tokensOnHome)


playing = Game()
playing.main()
