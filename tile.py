class Tile:
    def __init__(self, x, y, tileType, residents=[], colour=None):
        self.rangeCoordinates = (x, y)
        self.startCoordinates = self.rangeCoordinates[0][0], self.rangeCoordinates[1][0]
        self.endCoordinates = self.rangeCoordinates[0][1], self.rangeCoordinates[1][1]
        self.tileType = tileType
        self.residents = []
        self.colour = colour
        self.isBlocked = False
        self.blockedBy = None

    def checkResidents(self):
        if len(self.residents) == 0:
            return []

        playersOnTile = [token.playerOwner for token in self.residents]
        return playersOnTile

    def formBlock(self, playerOwner):
        self.isBlocked = True
        self.blockedBy = playerOwner
        print("Tile is blocked by: {}".format(playerOwner.playerName))

    def checkIfCanDestroyBlock(self, player):
        if self.checkResidents().count(player) == 1:
            self.destroyBlock()

    def destroyBlock(self):
        self.isBlocked = False
        self.blockedBy = None
        print("Tile is unblocked.")

    def __str__(self):
        return str(self.startCoordinates) + " " + self.tileType
