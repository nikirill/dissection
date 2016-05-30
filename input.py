try:
	import networkx as nx
except:
	raise

Gph = nx.Graph()

Gph.add_nodes_from(['A', 'B1', 'B2', 'B3', 'B4', 'Kb', 'C1', 'C2', 'C3', 'C4', 'Kc', 'D'])

# Indicate degree of freedom for every vertex
nx.set_node_attributes(Gph, 'df', {'A':1, 'B1':2, 'B2':2, 'B3':2, 'B4':2, 'Kb':1, 'C1':2, 'C2':2, 
									'C3':2, 'C4':2, 'Kc':1, 'D':1})

# Decribe edges in the graph
Gph.add_edges_from([('A','B1'), ('A','B2'), ('A','B3'), ('A','B4'), ('B1','Kb'), ('B2','Kb'),
				 ('B3','Kb'), ('B4','Kb'), ('B1','C1'), ('B2','C2'), ('B3','C3'), ('B4','C4'), 
				 ('C1','Kc'), ('C2','Kc'), ('C3','Kc'), ('C4','Kc'), ('C1','D'), ('C2','D'), 
				 ('C3','D'), ('C4','D')])

# Gph.add_nodes_from(['A1', 'A2', 'A3', 'A4', 'Ka', 'B1', 'B2', 'B3', 'B4', 'Kb', 'C1', 'C2', 'C3', 'C4', 'Kc', 'D'])

# # Indicate degree of freedom for every vertex
# nx.set_node_attributes(Gph, 'df', {'A1':1, 'A2':1, 'A3':1, 'A4':1, 'Ka':1, 'B1':2, 'B2':2, 'B3':2, 'B4':2, 'Kb':1, 'C1':2, 'C2':2, 
# 									'C3':2, 'C4':2, 'Kc':1, 'D':1})

# # Decribe edges in the graph
# Gph.add_edges_from([('A1','B1'), ('A2','B2'), ('A3','B3'), ('A4','B4'), ('A1','Ka'), ('A2','Ka'),
# 				 ('A3','Ka'), ('A4','Ka'), ('B1','Kb'), ('B2','Kb'),
# 				 ('B3','Kb'), ('B4','Kb'), ('B1','C1'), ('B2','C2'), ('B3','C3'), ('B4','C4'), 
# 				 ('C1','Kc'), ('C2','Kc'), ('C3','Kc'), ('C4','Kc'), ('C1','D'), ('C2','D'), 
# 				 ('C3','D'), ('C4','D')])

# nx.write_gml(Gph, '4graph_reduced.gml')