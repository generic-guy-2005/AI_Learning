import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E')
])

pos = nx.shell_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()