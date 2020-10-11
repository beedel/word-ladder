from vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, word):
        v = Vertex(word)
        self.vertices[word] = v

    def getVertex(self, word):
        if word in self.vertices:
            return self.vertices[word]
        else:
            return None

    def addEdge(self, from_v, to_v):
        if from_v not in self.vertices:
            nv = self.addVertex(from_v)
        if to_v not in self.vertices:
            nv = self.addVertex(to_v)
        self.vertices[from_v].addNeighbour(self.vertices[to_v])

