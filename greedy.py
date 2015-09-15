# :::::: activity selection problem ::::::::::: 
# you are given n activities with their start adn finish times.
# Select the maximum number of activities that can be performed
# by a single person, assuming that a person can only work on a
# single activity at a time.

# the greedy choice is to always pick the next activity whose 
# finish time is least among the remaining activities and the
# start time is mothe than or equal to the finish time of previously
# selected activity.

def activitySelection(start,finish,n):
	print "Following activities are selected"
	i = 0
	print i,
	for j in range(1,n):
		if start[j] >= finish[i]:
			print j,
			i = j

start = [1,3,0,5,8,5]
finish = [2,4,6,7,9,9]

activitySelection(start,finish,len(start))


# ::::::::: Kruskal's Minimun Spanning Tree :::::::::
# given a connected and undirected graph, a spanning tree of that
# graph is a subgraph that is a tree and connects all the vertices 
# together. 
# A single graph can have many different spanning trees. A MST for 
# a weighted, connected and undirected graph is a spanning tree 
# with weight less than or equal to the weight of every 
# other spanning tree. The weight(MST) = weight(sum of weights of edges of MST)



