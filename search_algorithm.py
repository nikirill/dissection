try:
	import multiprocessing as mp
	from itertools import chain, combinations
	import networkx as nx
	from pygraphviz import *
	import input
	from datetime import datetime
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

# Returns a string of concatenated vertex names in U
def vlist(U):
	if type(U) == tuple:
		return "".join(sorted(U))
	else:
		return "".join(U)

# Recovers an optimal solution by finding the highest tree
def recoverTree(parent):
	for child in Resolution.successors_iter(parent):
		solList.append(child)
		if len(child) > 1:
			recoverTree(child)

def levelSearch(H):
	best = []
	dfH = computedf(H)
	ciH = Ci[vlist(H)]
	Js = list(chain.from_iterable(combinations(H, r) for r in range(1, len(H))))
	for J in Js:
			for L in filter(lambda y: set(y + J) == set(H), Js):
				if ciH > max(Ci[vlist(J)], Ci[vlist(L)], dfH):
					ciH = max(Ci[vlist(J)], Ci[vlist(L)], dfH)
					best = [vlist(J), vlist(L)]
	return (vlist(H), best[0], best[1], ciH)


# Choose a graph from the input file to be evaluated
G = input.G5M

# Generate all possible subsets of vertices and form subgraphs out of them
subsets = list(chain.from_iterable(combinations(G.nodes(), r) for r in range(1, len(G) + 1)))

Ci = {vlist(subset): float("inf") for subset in subsets}	# Create dict with complexities for all subsets set to infinity
Resolution = nx.DiGraph()
for vertex in G:								# Then set complexities of trivial subsets (vertices) equal to their dfs
	Ci[vertex] = G.node[vertex]['df']
	Resolution.add_node(vertex)

for k in range (2, len(G)+1):  # size of a subset
	# print(k)
	fprog = open("progress.txt", "a")
	fprog.write(str(datetime.now()) + " : " + str(k) + "/" + str(len(G)) + "\n")
	fprog.close()
	levelsets = []
	pool = mp.Pool(processes=mp.cpu_count())
	levelsets = pool.map(levelSearch, filter(lambda x: len(x) == k, subsets))
	pool.close()
	pool.join()
	# Adding obtained optimal strategies to the solution graph
	for (parent, child1, child2, cmplx) in levelsets:
		Ci[parent] = cmplx
		Resolution.add_node(parent)
		Resolution.add_edge(parent, child1)
		Resolution.add_edge(parent, child2)

print('The optimal complexity is N^%d' % Ci[vlist(tuple(G.nodes()))])
solList = [vlist(tuple(G.nodes()))]
recoverTree(vlist(tuple(G.nodes())))	# Retrieving resolution algortihm with minimal complexity
solGraph = nx.subgraph(Resolution, solList)

ToPlot = nx.nx_agraph.to_agraph(solGraph)	# Plotting the resolution algorithm
ToPlot.layout(prog='dot')
ToPlot.draw('resolution.eps')
# ToPlot = nx.nx_agraph.to_agraph(solGraph.reverse())
# ToPlot.write("test.dot")
