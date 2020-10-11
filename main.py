from vertex import Vertex
from graph import Graph
from bfs import BFS, traverse


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


def main(dictionary, from_word, to_word):
	words = dictionary.split(",")

	words.append(from_word)
	words.append(to_word)

	graph = constructGraph(words)

	BFS(graph, graph.getVertex(from_word))

	return traverse(graph.getVertex(to_word))