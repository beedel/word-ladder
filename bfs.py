import sys

from vertex import Vertex
from graph import Graph
from queue import Queue


def constructGraph(words):
	possibilities = {}
	graph = Graph()

	for word in words:
		graph.addVertex(word)

	# find all matches with len(word)-1 letters that are the same
	for word in graph.vertices.keys():
		for i in range(len(word)):
			label = word[:i] + '*' + word[i+1:]
			if label in possibilities:
				possibilities[label].append(word)
			else:
				possibilities[label] = [word]

	# connect the vertices that can be swapped
	for collection in possibilities.keys():
		for wordA in possibilities[collection]:
			for wordB in possibilities[collection]:
				if wordA != wordB:
					graph.addEdge(wordA, wordB)

	return graph



def BFS(g, start):
	start.setDistance(0)
	start.setPrevious(None)
	vertQueue = Queue()
	vertQueue.enqueue(start)
	while (vertQueue.size() > 0):
		currentVert = vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if (nbr.getColour() == 'white'):
				nbr.setColour('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPrevious(currentVert)
				vertQueue.enqueue(nbr)
		currentVert.setColour('black')


def traverse(final):
	string = []
	vertex = final
	steps = 0
	while (vertex.getPrevious()):
		string.append(vertex.word)
		vertex = vertex.getPrevious()
		steps += 1
	string.append(vertex.word)

	reversed_string = string[::-1]

	print("->".join(reversed_string))
	print(len(reversed_string))



def main():
	words = sys.argv[1].split(",")
	from_word = sys.argv[2]
	to_word = sys.argv[3]

	words.append(from_word)
	words.append(to_word)

	graph = constructGraph(words)

	BFS(graph, graph.getVertex(from_word))


	traverse(graph.getVertex(to_word))


if __name__ == "__main__":
	main()
