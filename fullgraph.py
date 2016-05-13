import numpy as np
from itertools import chain, combinations
import networkx as nx
import matplotlib.pyplot as plt


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
for subset in subsets:
	subgrs.append(nx.subgraph(G, subset))

# Find all possible joints with defined complexity
# for subset in subsets:
# 	sbgr = nx.subgraph(G, subset)
# 	if nx.is_connected(sbgr):
# 		fdegree = 0
# 		for vertex in sbgr.nodes():
# 			fdegree += sbgr.node[vertex]['df']
# 		fdegree -= sbgr.number_of_edges()
# 		if fdegree <= limit:
# 			subgrs.append(sbgr)

# A function for computing a degree of freedom of a vertex subset
def computedf(U):
	dfU = 0
	for vertex in U.nodes():
		dfU += U.node[vertex]['df']
	dfU -= U.number_of_nodes()
	return dfU

def AlgorithmRecovery(K, f):
	f.write(" ".join(sorted(K.nodes())))
	# if len(Best.get(K)[0]) > 1:
	# 	AlgorithmRecovery(Best.get(K)[0], f)


Ci = {}
Best = {}
for subgr in subgrs:
	Ci[sorted(subgr.nodes())] = float("inf")
for vertex in G.nodes():
	Ci[vertex] = G.node[vertex]['df']  # complexity for each vertex is its df

for w in range (2, G.number_of_nodes()+1):  # size of a subset
	for K in filter(lambda x: len(x) == w, subsets): # all possible subsets of a given size
		dfK = computedf(nx.subgraph(G, K))
		listJ = chain.from_iterable(combinations(K, r) for r in range(1, int(len(K)/2) + 1))
		for J in listJ:
			L = list(set(K) - set(J))
			if Ci[K] > max(Ci.get(J), Ci.get(L), dfK):
				Ci[K] = max(Ci.get(J), Ci.get(L), dfK)
				Best[K] = [J, L] 

print(Best.get(G.nodes))

fi = open("solution.txt", 'w')
AlgorithmRecovery(G.nodes(), fi)
fi.close()




# Writing solution to a file
# f = open("solution.txt", 'w')
# for line in solution:
# 	first = True
# 	for element in line:
# 		if first == True:
# 			first = False
# 		else:
# 			f.write("   |   ")
# 		f.write(" ".join(sorted(element.nodes())))
# 	f.write("\n")
# f.close()

