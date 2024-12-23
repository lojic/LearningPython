from advent import nx, plt

G = nx.Graph([ ('A','B'), ('A','C'), ('A','D'),
               ('A','E'), ('B','D'), ('B','E'),
               ('C','F'), ('D','E'), ('E','F') ])

clique_edges = [ ('A','B'), ('A','D'), ('A','E'), ('B','D'), ('B','E'), ('D','E') ]

pos = { 'A' : (-1, -5), 'B' : (0, 10), 'C' : (-1, -10),
        'D' : ( 0,  0), 'E' : (1, -5), 'F':  ( 1, -10) }
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=5000, font_size=30)
nx.draw_networkx_edges(G, pos, edgelist=clique_edges, edge_color="green", width=4)
plt.show()
