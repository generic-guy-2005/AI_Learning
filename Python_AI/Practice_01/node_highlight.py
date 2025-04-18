import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

highlighted_nodes = ['A', 'E']

G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E')
])

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_nodes(G, pos, nodelist=highlighted_nodes, node_color='red', node_size=700)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos)

plt.show()