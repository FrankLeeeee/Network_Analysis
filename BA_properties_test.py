import networkx as nx
import BA_properties as p
import matplotlib.pyplot as plt

n = 100
m = 10

g = p.generate_BA_graph(n,m)

nx.draw(g)
plt.show()

print("Number of nodes: ", p.get_BA_num_of_nodes(g))
print("Number of links: ", p.get_BA_num_of_links(g))
print("Average degree: ", p.get_BA_avg_degree(m))
print("Average distance: ", p.get_BA_avg_distance(g))
print("Plot degree distribution.")
p.plot_BA_degreee_distribution(g)
