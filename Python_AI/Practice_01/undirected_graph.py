import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E')
])

nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()

plt.savefig("Graph_Visual.png", format="PNG")
plt.close()