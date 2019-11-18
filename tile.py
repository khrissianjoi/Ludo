class Tile:
    def __init__(self, x, y, tileType, residents=[]):
        self.coordinate = (x,y)
        self.tileType = tileType
        self.residents = []