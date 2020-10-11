import sys 

class Vertex:
    def __init__(self, word):
        self.word = word
        self.connectedTo = {}
        self.colour = 'white'
        self.distance = sys.maxsize
        self.previous = None

    def addNeighbour(self, other_vertex):
        self.connectedTo[other_vertex] = 0

    def setColour(self, colour):
        self.colour = colour

    def setDistance(self, distance):
        self.distance = distance

    def setPrevious(self, previous):
        self.previous = previous

        
    def getPrevious(self):
        return self.previous
        
    def getDistance(self):
        return self.distance
        
    def getColour(self):
        return self.colour

    def getConnections(self):
        return self.connectedTo.keys()
