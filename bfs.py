from queue import Queue


def BFS(graph, start):
	start.setPrevious(None)
	q = Queue()
	q.enqueue(start)
	while (q.size() > 0):
		vertex = q.dequeue()
		for connection in vertex.getConnections():
			# see if it has not been visited yet
			if (connection.getColour() == 'white'):
				connection.setColour('gray')
				connection.setPrevious(vertex)
				q.enqueue(connection)
		# don't visit it again
		vertex.setColour('black')


def traverse(final):
	s = []
	vertex = final
	steps = 0
	while (vertex.getPrevious()):
		s.append(vertex.word)
		vertex = vertex.getPrevious()
		steps += 1
	s.append(vertex.word)

	reversed_string = s[::-1]

	print("->".join(reversed_string) + " (" + str(len(reversed_string)) + ")")

	return len(reversed_string)
