class Vertex:
    def __init__(self, word):
        self.word = word
        self.connectedWith = {}
        self.colour = 'white'
        self.previous = None

    def addNeighbour(self, other_vertex):
        self.connectedWith[other_vertex] = 0

    def setColour(self, colour):
        self.colour = colour

    def setPrevious(self, previous):
        self.previous = previous

       
    def getPrevious(self):
        return self.previous
        
    def getColour(self):
        return self.colour

    def getConnections(self):
        return self.connectedWith.keys()
