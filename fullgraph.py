try:
	import numpy
	import multiprocessing as mp
	from itertools import chain, combinations
	import networkx as nx
	import matplotlib.pyplot as plt
	from pygraphviz import *
except:
	raise


# A function for computing a degree of freedom of a vertex subset
def computedf(U):
	dfU = 0
	UG = nx.subgraph(G, U)
	for vertex in UG:
		dfU += UG.node[vertex]['df']
	dfU -= UG.number_of_edges()
	return dfU

# Returns a string of nodes in U
def vlist(U):
	if len(U) > 1:
		return "".join(sorted(U))
	else:
		return "".join(U)

def recoverTree(parent):
	for child in Resolution.successors_iter(parent):
		solList.append(child)
		if len(child) > 1:
			recoverTree(child)

def setOverlap(T):
	Js = list(chain.from_iterable(combinations(T, r) for r in range(1, len(T))))
	for x,y in Js, Js:
		if set(x+y) == set(T):
			return x,y

def levelSearch(K):
	# print(K)
	global Ci, Resolution
	best = []
	dfK = computedf(K)
	Resolution.add_node(vlist(K))
	# Js = list(chain.from_iterable(combinations(K, r) for r in range(1, len(K))))
	# print(K, "and", Js)
	# for J, L in filter(lambda x,y: set(x+y) == set(K), Js):
	for J, L in setOverlap(K):
		# print(K, Ci[vlist(J)], Ci[vlist(L)], dfK)
		if Ci[vlist(K)] > max(Ci[vlist(J)], Ci[vlist(L)], dfK):
			Ci[vlist(K)] = max(Ci[vlist(J)], Ci[vlist(L)], dfK)
			best = [vlist(J), vlist(L)]
			# print("best", K, max(Ci[vlist(J)], Ci[vlist(L)], dfK))
	# print(Resolution.nodes())
	Resolution.add_edge(vlist(K), vlist(best[0]))
	Resolution.add_edge(vlist(K), vlist(best[1]))


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

# G.add_nodes_from(['A1', 'A2', 'A3', 'A4', 'Ka', 'B1', 'B2', 'B3', 'B4', 'Kb', 'C1', 'C2', 'C3', 'C4', 'Kc', 'D'])

# # Indicate degree of freedom for every vertex
# nx.set_node_attributes(G, 'df', {'A1':1, 'A2':1, 'A3':1, 'A4':1, 'Ka':1, 'B1':2, 'B2':2, 'B3':2, 'B4':2, 'Kb':1, 'C1':2, 'C2':2, 
# 									'C3':2, 'C4':2, 'Kc':1, 'D':1})

# # Decribe edges in the graph
# G.add_edges_from([('A1','B1'), ('A2','B2'), ('A3','B3'), ('A4','B4'), ('A1','Ka'), ('A2','Ka'),
# 				 ('A3','Ka'), ('A4','Ka'), ('B1','Kb'), ('B2','Kb'),
# 				 ('B3','Kb'), ('B4','Kb'), ('B1','C1'), ('B2','C2'), ('B3','C3'), ('B4','C4'), 
# 				 ('C1','Kc'), ('C2','Kc'), ('C3','Kc'), ('C4','Kc'), ('C1','D'), ('C2','D'), 
# 				 ('C3','D'), ('C4','D')])

# nx.write_gml(G, '4graph_reduced.gml')


# Generate all possible subsets of vertices and form subgraphs out of them
subsets = list(chain.from_iterable(combinations(G.nodes(), r) for r in range(1, len(G) + 1)))

Ci = {vlist(subset): float("inf") for subset in subsets}	# Create dict with complexities for all subsets set to infinity
Resolution = nx.DiGraph()
for vertex in G:								# Then set complexities of trivial subsets (vertices) equal to their dfs
	Ci[vertex] = G.node[vertex]['df']
	Resolution.add_node(vertex)

for w in range (2, len(G)+1):  # size of a subset
	# jobs = []
	# lsets = list(filter(lambda x: len(x) == w, subsets))
	# p1 = mp.Process(target=levelSearch, args=(lsets[:int(len(lsets)/ncores)],))
	# p2 = mp.Process(target=levelSearch, args=(lsets[int(len(lsets)/ncores):],))
	# for p in [p1, p2]: p.start()
	# for p in [p1, p2]: p.join()
	pool = mp.Pool(processes=4)
	# pool.apply(levelSearch, args=(x, Ci, Resolution,) for x in filter(lambda x: len(x) == w, subsets))
	pool.map(levelSearch, filter(lambda x: len(x) == w, subsets))
	pool.close()
	pool.join()


print('The optimal complexity is N^%d' % Ci[vlist(G.nodes())])
solList = [vlist(G.nodes())]
recoverTree(vlist(G.nodes()))	# Retrieving resolution algortihm with minimal complexity
solGraph = nx.subgraph(Resolution, solList)

ToPlot = nx.nx_agraph.to_agraph(solGraph)	# Plotting the resolution algorithm
ToPlot.layout(prog='dot')
ToPlot.draw('resolution.png')
# ToPlot = nx.nx_agraph.to_agraph(solGraph.reverse())
# ToPlot.write("test.dot")
# nx.draw(solGraph,pos,with_labels=False,arrows=False)
