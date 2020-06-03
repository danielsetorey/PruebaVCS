import networkx as nx
import matplotlib.pyplot as plt

G = nx.barbell_graph(4, 2)

nx.draw(G)

plt.show()


def suma(a, b):

    return a + b
