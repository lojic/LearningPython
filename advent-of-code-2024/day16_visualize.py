from advent import nx, plt

## NOTE: this does not visualize the Day 16 graph. It's simply an
##       example of visualizing *a* graph I got from ChatGPT :)

# Create a graph
G = nx.Graph()

# Add edges and weights
edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 5),
    ("B", "D", 10),
    ("C", "D", 3),
    ("D", "E", 7),
    ("C", "E", 8)
]
G.add_weighted_edges_from(edges)

# Find the shortest path
source = "A"
target = "E"
shortest_path = nx.shortest_path(G, source=source, target=target, weight="weight")

# Get the positions of the nodes
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)

# Highlight the shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

# Add edge labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.title(f"Shortest Path from {source} to {target}: {shortest_path}")
plt.show()
