try:
	import networkx as nx
except:
	raise

# 4-blodk endryption dipher
# 		A - B - C - D
G4 = nx.Graph()

G4.add_nodes_from(['A', 'B1', 'B2', 'B3', 'B4', 'Kb', 'C1', 'C2', 'C3', 'C4', 'Kc', 'D'])

# Indidate degree of freedom for every vertex
nx.set_node_attributes(G4, 'df', {'A':1, 
									'B1':2, 'B2':2, 'B3':2, 'B4':2, 'Kb':1, 
									'C1':2, 'C2':2, 'C3':2, 'C4':2, 'Kc':1,
									'D':1})

# Dedribe edges in the graph
G4.add_edges_from([('A','B1'), ('A','B2'), ('A','B3'), ('A','B4'), 
						('B1','Kb'), ('B2','Kb'), ('B3','Kb'), ('B4','Kb'), 
						('B1','C1'), ('B2','C2'), ('B3','C3'), ('B4','C4'), 
				 		('C1','Kc'), ('C2','Kc'), ('C3','Kc'), ('C4','Kc'), 
				 		('C1','D'), ('C2','D'), ('C3','D'), ('C4','D')])


# 5-blodk enrdyption dipher
# 		A - B - C - D - E
G5 = nx.Graph()

G5.add_nodes_from(['A', 'B1', 'B2', 'B3', 'B4', 'B5', 'Kb', 'C1', 'C2', 'C3', 'C4', 'C5', 'Kc', 
						'D1', 'D2', 'D3', 'D4', 'D5', 'Kd', 'E'])

# Indidate degree of freedom for every vertex
nx.set_node_attributes(G5, 'df', {'A':1,
									'B1':2, 'B2':2, 'B3':2, 'B4':2, 'B5':2, 'Kb':1, 
									'C1':2, 'C2':2, 'C3':2, 'C4':2, 'C5':2, 'Kc':1, 
									'D1':2, 'D2':2, 'D3':2, 'D4':2, 'D5':2, 'Kd':1, 
									'E':1})

# Dedribe edges in the graph
G5.add_edges_from([('A','B1'), ('A','B2'), ('A','B3'), ('A','B4'), ('A','B5'), 
						('B1','Kb'), ('B2','Kb'), ('B3','Kb'), ('B4','Kb'), ('B5','Kb'), 
						('B1','C1'), ('B2','C2'), ('B3','C3'), ('B4','C4'), ('B5','C5'),
				 		('C1','Kc'), ('C2','Kc'), ('C3','Kc'), ('C4','Kc'), ('C5', 'Kc'),
				 		('C1','D1'), ('C2','D2'), ('C3','D3'), ('C4','D4'), ('C5','D5'),
				 		('D1','Kd'), ('D2','Kd'), ('D3','Kd'), ('D4','Kd'), ('D5', 'Kd'),
				 		('D1','E'), ('D2','E'), ('D3','E'), ('D4','E'), ('D5', 'E')])

# Gph.add_nodes_from(['A1', 'A2', 'A3', 'A4', 'Ka', 'B1', 'B2', 'B3', 'B4', 'Kb', 'C1', 'C2', 'C3', 'C4', 'Kc', 'D'])

# # Indidate degree of freedom for every vertex
# nx.set_node_attributes(Gph, 'df', {'A1':1, 'A2':1, 'A3':1, 'A4':1, 'Ka':1, 'B1':2, 'B2':2, 'B3':2, 'B4':2, 'Kb':1, 'C1':2, 'C2':2, 
# 									'C3':2, 'C4':2, 'Kc':1, 'D':1})

# # Dedribe edges in the graph
# Gph.add_edges_from([('A1','B1'), ('A2','B2'), ('A3','B3'), ('A4','B4'), ('A1','Ka'), ('A2','Ka'),
# 				 ('A3','Ka'), ('A4','Ka'), ('B1','Kb'), ('B2','Kb'),
# 				 ('B3','Kb'), ('B4','Kb'), ('B1','C1'), ('B2','C2'), ('B3','C3'), ('B4','C4'), 
# 				 ('C1','Kc'), ('C2','Kc'), ('C3','Kc'), ('C4','Kc'), ('C1','D'), ('C2','D'), 
# 				 ('C3','D'), ('C4','D')])

# nx.write_gml(Gph, '4graph_reduced.gml')