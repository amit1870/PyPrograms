V = 3
E = 3
class Edge(object):
	def __init__(self,src,dest):
		self.src = src
		self.dest = dest

class Graph(object):
	def __init__(self,V,E):
		self.edge = Edge(None,None)
		self.V = V
		self.E = E


# a utility function to find the subset of an element i 
def find(parent, i):
	if parent[i] == -1:
		return i
	return find(parent,parent[i])

# a utility function to do union of two subsets

def Union(parent, x, y):
	xset = find(parent,x)
	yset = find(parent,y)
	parent[xset] = yset

def isCycle(graph):
	global V,E
	parent = [-1] * V
	for i in range(0,graph.E) :
		x = find(parent, graph.edge.src)
		y = find(parent,graph.edge.dest)

		if x == y:
			return True
		Union(parent,x,y)

	return False

def main():
	global V, E
	graph = Graph(V,E)

	# add edge 0-1
	graph.edge.src = 0
	graph.edge.dest = 1

	# # add edge 1-2
	graph.edge.src = 1
	graph.edge.dest = 2

	# # add edge 0-2
	graph.edge.src = 0
	graph.edge.dest = 2

	if isCycle(graph):
		print "Graph contains cycle"
	else:
		print "Graph doesn't contain cycle"


main()

