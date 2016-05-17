try:
	import numpy as np
	from itertools import chain, combinations
	import networkx as nx
	import matplotlib.pyplot as plt
	from pygraphviz import *
except:
	raise


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


# Generate all possible subsets of vertices
# and form subgraphs out of them
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
	for vertex in U:
		dfU += U.node[vertex]['df']
	dfU -= U.number_of_edges()
	return dfU

# Returns a string of nodes in U
def nodeslist(U):
	return "".join(sorted(U.nodes()))

def recoverTree(parent):
	for child in Resolution.successors_iter(parent):
		solList.append(child)
		if len(child) > 1:
			recoverTree(child)


# Create dict with complexities for all subsets set to infinity
# Then set complexities of trivial subsets (vertices) equal to
# their dfs
Ci = {nodeslist(subgr): float("inf") for subgr in subgrs}
Resolution = nx.DiGraph()
for vertex in G:
	Ci[vertex] = G.node[vertex]['df']
	Resolution.add_node(vertex)

best = []
for w in range (2, len(G)+1):  # size of a subset
	for K in filter(lambda x: len(x) == w, subgrs): # all possible subsets of a given size
		dfK = computedf(K)
		halves = chain.from_iterable(combinations(K.nodes(), r) for r in range(1, int(len(K)/2) + 1))
		Resolution.add_node(nodeslist(K))
		for halve in halves:
			J = nx.subgraph(K, halve)
			L = nx.subgraph(K, list(set(K.nodes()) - set(halve)))
			if Ci[nodeslist(K)] > max(Ci.get(nodeslist(J)), Ci.get(nodeslist(L)), dfK):
				Ci[nodeslist(K)] = max(Ci.get(nodeslist(J)), Ci.get(nodeslist(L)), dfK)
				best = [J, L]
		Resolution.add_edge(nodeslist(K), nodeslist(best[0]))
		Resolution.add_edge(nodeslist(K), nodeslist(best[1]))

print("Complexity is", Ci[nodeslist(G)])
solList = [nodeslist(G)]
recoverTree(nodeslist(G))
solGraph = nx.subgraph(Resolution, solList)


ToPlot = nx.nx_agraph.to_agraph(solGraph)
# A = nx.nx_agraph.to_agraph(solGraph.reverse())
# A.write("test.dot")
ToPlot.layout(prog='dot')
ToPlot.draw('resolution.png')
# nx.draw(solGraph,pos,with_labels=False,arrows=False)
