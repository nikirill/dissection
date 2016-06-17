try:
	import networkx as nx
except:
	raise

# 3-block encryption cipher
# 		A - B - C
G3 = nx.Graph()

G3.add_nodes_from(['A', 'B1', 'B2', 'B3', 'Kb', 'C'])

# Indidate degree of freedom for every vertex
nx.set_node_attributes(G3, 'df', {'A':1, 
									'B1':2, 'B2':2, 'B3':2, 'Kb':1, 
									'C':1})

# Dedribe edges in the graph
G3.add_edges_from([('A','B1'), ('A','B2'), ('A','B3'), 
						('B1','Kb'), ('B2','Kb'), ('B3','Kb'),
						('B1','C'), ('B2','C'), ('B3','C')])


# 3-block encryption cipher with only two keys
# 		A - B - A'
G3R = nx.Graph()

G3R.add_nodes_from(['A1', 'A2', 'A3', 'Kac', 'B1', 'B2', 'B3', 'Kb', 'C1', 'C2', 'C3'])

# Indidate degree of freedom for every vertex
nx.set_node_attributes(G3R, 'df', {'A1':1, 'A2':1, 'A3':2, 'Kac':1, 
									'B1':2, 'B2':2, 'B3':2, 'Kb':1, 
									'C1':1, 'C2':1, 'C3':1})

# Dedribe edges in the graph
G3R.add_edges_from([('A1','B1'), ('A2','B2'), ('A3','B3'), 
						('A1','Kac'), ('A2','Kac'), ('A3','Kac'),
						('B1','Kb'), ('B2','Kb'), ('B3','Kb'),
						('B1','C1'), ('B2','C2'), ('B3','C3'),
						('Kac','C1'), ('Kac','C2'), ('Kac','C3')])

# 4-block encryption cipher
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


# 5-block enrcyption cipher
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


# 5-block enrcyption cipher with keys merged
# 		A - B - C - D - E
G5M = nx.Graph()

G5M.add_nodes_from(['A', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5',  
						'D1', 'D2', 'D3', 'D4', 'D5', 'E'])

# Indidate degree of freedom for every vertex
nx.set_node_attributes(G5M, 'df', {'A':1,
									'B1':2, 'B2':2, 'B3':2, 'B4':2, 'B5':2, 
									'C1':2, 'C2':2, 'C3':2, 'C4':2, 'C5':2, 
									'D1':2, 'D2':2, 'D3':2, 'D4':2, 'D5':2, 
									'E':1})

# Dedribe edges in the graph
G5M.add_edges_from([('A','B1'), ('A','B2'), ('A','B3'), ('A','B4'), ('A','B5'), 
						('B1','B2'), ('B1','B3'), ('B1','B4'), ('B1','B5'), 
						('B1','C1'), ('B2','C2'), ('B3','C3'), ('B4','C4'), ('B5','C5'),
				 		('C1','C2'), ('C1','C3'), ('C1','C4'), ('C1','C5'),
				 		('C1','D1'), ('C2','D2'), ('C3','D3'), ('C4','D4'), ('C5','D5'),
				 		('D1','D2'), ('D1','D3'), ('D1','D4'), ('D1','D5'),
				 		('D1','E'), ('D2','E'), ('D3','E'), ('D4','E'), ('D5', 'E')])