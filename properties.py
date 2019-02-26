import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter


# Argument 'g' is the networkx Graph object
# Argument 'node' is the name of the node of your choice
# Argument 'save' is a flag to decide whether to save the plot locally
def read_network(file_dir):
    g = nx.read_edgelist(file_dir)
    return g

def get_num_of_links(g):
    return g.number_of_edges()

def get_num_of_nodes(g):
    return g.number_of_nodes()

def get_max_degree(g):
    return max(nx.degree(g))

def get_min_degree(g):
    return min(nx.degree(g))

def get_average_degree(g):
    average_degree = 2*g.number_of_edges()/g.number_of_nodes()
    return average_degree

def get_largest_hub(g):
    dmax = get_max_degree(g)
    hubs = []
    for node, val in g.degree():
        if val == dmax:
            hubs.append(node)
    return hubs

def plot_largest_hub(g, node, save=False):
    neighbors = g.neighbors(node)
    hub = nx.Graph()
    for neighbor in neighbors:
        hub.add_edge(node, neighbor)
    nx.draw(hub)
    if save:
        plt.savefig("hub.png")
    plt.show()


def plot_degree_histogram(g, save=False):
    plt.hist(plt.hist(list(nx.degree(g).values())))
    plt.xlabel('Degree')
    plt.ylabel('Number of Nodes')
    if save:
        plt.savefig("Degree Histogram")
    plt.show()

def plot_degree_distribution(g, save=False):
    total_nodes = g.number_of_nodes()

    count = Counter(g.degree().values())
    count = {k: v/total_nodes for k, v in count.items()}
    k = list(count.keys())
    pk = list(count.values())

    plt.plot(k, pk,marker = '0')
    plt.xlabel("k")
    plt.ylabel("P(k)")
    plt.title("Degree Distribution")
    if save:
        plt.savefig("Degree Distribution")
    plt.show()

def get_node_clustering_coef(g, node):
    clustering_coef = nx.clustering(g, node)
    return clustering_coef

def get_avg_cluster_coef(g):
    return nx.average_clustering(g)

def get_avg_distance(g):
    return nx.algorithms.average_shortest_path_length(g)