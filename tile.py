class Tile:
    def __init__(self, x, y, tileType, residents=[], colour=None):
        # ((xmini,xmaxi),(ymini,ymaxi))
        self.rangeCoordinates = (x,y)
        self.startCoordinates = self.rangeCoordinates[0][0],self.rangeCoordinates[1][0]
        self.endCoordinates = self.rangeCoordinates[0][1],self.rangeCoordinates[1][1]
        self.tileType = tileType
        self.residents = []
        self.colour = colour

    def __str__(self):
        return str(self.startCoordinates) + " " + self.tileType
