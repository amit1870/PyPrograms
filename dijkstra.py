# implementing dijkstra using greedy algorithm 
# a utility function to find the vertex with minimum distance value, 
# from the set of vertices not yet included in shortest path tree

V = 9 
Path = []
INF = 999999

def minDistance(dist,sptSet):
	global V,INF
	min = INF
	min_index = None 

	for v in range(0,V):
		if sptSet[v] == False and dist[v] <= min:
			min = dist[v]
			min_index = v

	return min_index

# a utility function to print the constructed distance array 

def printSolution(dist, n):
	print "Vertex 	Distance  from Source \n"
	for i in range(0,n):
		print "%d \t\t %d\n" % (i , dist[i])


def dijkstra(graph,src):
	global V,Path,INF
	dist = [None]*V
	sptSet = [None]*V

	for i in range(0,V):
		dist[i] = INF
		sptSet[i] = False

	Path.append(src)
	dist[src] = 0

	for count in range(0,V-1):
		u = minDistance(dist, sptSet)
		sptSet[u] = True

		for v in range(0,V):
			if not sptSet[v] and graph[u][v] and dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
				dist[v] = dist[u] + graph[u][v]
				Path.append(v)

	printSolution(dist,V)

def main():
	graph = [[0,4,0,0,0,0,0,8,0],\
			[4,0,8,0,0,0,0,11,0],\
			[0,8,0,7,0,4,0,0,2],\
			[0,0,7,0,9,14,0,0,0],\
			[0,0,0,9,0,10,0,0,0],\
			[0,0,4,0,10,0,2,0,0],\
			[0,0,0,14,0,2,0,1,6],\
			[8,11,0,0,0,0,1,0,7],\
			[0,0,2,0,0,0,6,7,0]]
	dijkstra(graph,0)
	print Path

main()