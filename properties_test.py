import networkx as nx
import properties as p
import matplotlib.pyplot as plt

g = nx.read_edgelist("sample_graph.txt")

nx.draw(g)
plt.show()
print("number of links: ", p.get_num_of_links(g))
print("number of nodes: ", p.get_num_of_nodes(g))
print("max degree: ", p.get_max_degree(g))
print("min degree: ", p.get_min_degree(g))
print("average degree: ", p.get_average_degree(g))
print("largest hub: ", p.get_largest_hub(g))
print("plot hub.")
p.plot_largest_hub(g, '3')
p.plot_degree_distribution(g)
print("node 3 clustering coef: ", p.get_node_clustering_coef(g, '3'))
print("avg clustering coef: ", p.get_avg_cluster_coef(g))
print("avg distance: ", p.get_avg_distance(g))
print("diameter: ", p.get_diameter(g))
