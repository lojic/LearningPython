from advent import nx, plt

G = nx.Graph([ ('A','B', { 'weight' : 5 }), ('A','C', { 'weight' : 50 }), ('A','D', { 'weight' : 25 }), ('A','E', { 'weight' : 25 }),
               ('B','D', { 'weight' : 20 }), ('B','E', { 'weight' : 5 }),
               ('C','F', { 'weight' : 55 }),
               ('D','E', { 'weight' : 25 }),
               ('E','F', { 'weight' : 50 }) ])

pos = { 'A' : (-1, -5), 'B' : (0,10), 'C' : (-1,-10), 'D' : (0,0), 'E' : (1,-5), 'F': (1,-10) }
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=5000, font_size=30)
plt.show()
