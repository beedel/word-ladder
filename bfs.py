from Vertex import Vertex
from Graph import Graph
from Queue import Queue


def buildGraph():
	d = {}
	g = Graph()
	g.addVertex("hot")
	g.addVertex("dot")
	g.addVertex("dog")
	g.addVertex("lot")
	g.addVertex("log")
	g.addVertex("arm")
	g.addVertex("cat")
	g.addVertex("man")
	g.addVertex("hit")
	g.addVertex("cog")


	# create buckets of words that differ by one letter
	for word in g.vertList.keys():
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]

	# for x, y in d.items():
	# 	print(x + ": ", end="")
	# 	for z in y:
	# 		print(z, ", ", end="")
	# 	print()

	# print()


	# add vertices and edges for words in the same bucket
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2)

	# for v in g.vertList.values():
	# 	l = v.getConnections()
	# 	print(v.id + ": ", end="")
	# 	for z in l:
	# 		print(z.id + " ", end="")
	# 	print()

	# print("====")

	return g



def bfs(g, start):
	start.setDistance(0)
	start.setPred(None)
	vertQueue = Queue()
	vertQueue.enqueue(start)
	while (vertQueue.size() > 0):
		currentVert = vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if (nbr.getColor() == 'white'):
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance() + 1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)
		currentVert.setColor('black')

	# for v in g.vertList.values():
	# 	if v.getPred():
	# 		print(v.id + ": " + v.getPred().id)
	# 	else:
	# 		print(v.id + ": ")


def traverse(y):
	string = []
	x = y
	while (x.getPred()):
		string.append(x.getId())
		x = x.getPred()
	string.append(x.getId())

	reversed_string = string[::-1]

	print("->".join(reversed_string))

g = buildGraph()
bfs(g, g.getVertex("hit"))


traverse(g.getVertex('cog'))
