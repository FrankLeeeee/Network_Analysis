import networkx as nx
from networkx.generators.random_graphs import barabasi_albert_graph
from math import log10, log, pow
import matplotlib.pyplot as plt

def generate_BA_graph(n, m):
    # The initialization is a graph with with m nodes and no edges.
    return barabasi_albert_graph(n, m)

def get_BA_num_of_nodes(g):
    return g.number_of_nodes()

def get_BA_num_of_links(g):
    return g.number_of_edges()

def get_BA_avg_degree(m):
    return 2*m

def get_BA_avg_distance(g):
    n = g.number_of_nodes()
    return log10(n)/log10(log10(n))
    
def get_BA_avg_clustering_coef(g, m):
    n = g.number_of_nodes()
    return (m/8) * pow(log(n),2) / n

def plot_BA_degreee_distribution(g, save=False):
    n = g.number_of_nodes()
    k_ls = list(range(1,n))
    pk_ls = []

    for k in k_ls:
        pk = k**-3
        pk_ls.append(pk)
    plt.plot(k_ls, pk_ls,marker = 'o')
    plt.xlabel("k")
    plt.ylabel("P(k)")
    plt.title("Degree Distribution")
    if save:
        plt.savefig("Degree Distribution")
    plt.show()
