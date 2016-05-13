import numpy as np
from itertools import chain, combinations
import networkx as nx
import matplotlib.pyplot as plt

# Complexity limit for a subset
limit = 2

G = nx.Graph()
G.add_nodes_from(['A', 'B1', 'B2', 'B3', 'B4', 'Kb', 'C1', 'C2', 'C3', 'C4', 'Kc', 'D'])

# Indicate degree of freedom for every vertex
nx.set_node_attributes(G, 'df', {'A':1, 'B1':2, 'B2':2, 'B3':2, 'B4':2, 'Kb':1, 'C1':2, 'C2':2, 
									'C3':2, 'C4':2, 'Kc':1, 'D':1})

# Decribe edges in the graph
G.add_edges_from([('A','B1'), ('A','B2'), ('A','B3'), ('A','B4'), ('B1','Kb'), ('B2','Kb'),
				 ('B3','Kb'), ('B4','Kb'), ('B1','C1'), ('B2','C2'), ('B3','C3'), ('B4','C4'), 
				 ('C1','Kc'), ('C2','Kc'), ('C3','Kc'), ('C4','Kc'), ('C1','D'), ('C2','D'), 
				 ('C3','D'), ('C4','D')])

# nx.draw(G)
# plt.show()
# Generate all possible subsets of vertices
subsets = chain.from_iterable(combinations(G.nodes(), r) for r in range(1, len(G.nodes()) + 1))
subgrs = []

# Find all possible joints with defined complexity
for subset in subsets:
	sbgr = nx.subgraph(G, subset)
	if nx.is_connected(sbgr):
		fdegree = 0
		for vertex in sbgr.nodes():
			fdegree += sbgr.node[vertex]['df']
		fdegree -= sbgr.number_of_edges()
		if fdegree <= limit:
			subgrs.append(sbgr)


# for i in range (2, G.number_of_nodes()+1):  #levels of the tree
# 	pairs = list(combinations(filter(lambda x: x.number_of_nodes()<i, subgrs), 2)) #all possible pairs below the level
# 	for h in filter(lambda igr: igr.number_of_nodes()==i, subgrs): #all subsets on the level
# 		reachability = False
# 		for pair in pairs:
# 			if (sorted(pair[0].nodes() + pair[1].nodes()) == sorted(h.nodes())):
# 				reachability = True
# 				# print(pair[0].nodes(), pair[1].nodes())
# 		if reachability == False:
# 			subgrs.remove(h)
# 			if i == G.number_of_nodes():
# 				print("Complexity = ", limit, "is NOT achievable for key recovery")
# 		elif i == G.number_of_nodes():
# 			print("Complexity = ", limit, "is achievable for key recovery")


solution = [[G]]
reachability = True
while len(subgrs) >= G.number_of_nodes():
	level = []
	for leaf in solution[-1]:   # access last discovered level of solution
		if leaf.number_of_nodes() == 1:
			level.append(leaf)
			continue
		# find possible pairs of subgraphs to construct current graph
		pairs = list(combinations(filter(lambda x: x.number_of_nodes()<leaf.number_of_nodes(), subgrs), 2)) #all possible pairs below the level
		optimum = (pairs[0], 0)
		for pair in pairs:
			if (sorted(pair[0].nodes() + pair[1].nodes()) == sorted(leaf.nodes())):
				# we want the most balanced pair so find a pair with maximal min
				local_min = min(pair, key=lambda t: t.number_of_nodes()).number_of_nodes()
				if optimum[1] < local_min:
					optimum = (pair, local_min)
		# check if there has been a partition and add it
		if optimum[1] != 0:
			level.append(optimum[0][0])
			level.append(optimum[0][1])
		else:
			print("The following component is NOT reachable\n", sorted(leaf.nodes()))
			reachability = False

	# add the new tree level
	solution.append(level)
	if reachability != True:
		break
	# remove all the subgrs bigger than biggest at current level
	size_limit = max(level, key=lambda t: t.number_of_nodes()).number_of_nodes()
	subgrs = [x for x in subgrs if x.number_of_nodes() < size_limit]


# Writing solution to a file
f = open("solution.txt", 'w')
for line in solution:
	first = True
	for element in line:
		if first == True:
			first = False
		else:
			f.write("   |   ")
		f.write(" ".join(sorted(element.nodes())))
	f.write("\n")
f.close()

