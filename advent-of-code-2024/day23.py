from advent import parse, words, nx, combinations

G = nx.Graph(parse(23, words))

part1 = lambda: len({ tuple(sorted((v, neighbors[0], neighbors[1])))
                      for v, _ in nx.triangles(G).items() if v[0] == 't'
                      for neighbors in combinations(G[v], 2) if G.has_edge(neighbors[0], neighbors[1]) })

part2 = lambda: ",".join(sorted(nx.max_weight_clique(G, weight=None)[0]))

# ---------------------------------------------------------------------------------------------

assert part1() == 1151
assert part2() == 'ar,cd,hl,iw,jm,ku,qo,rz,vo,xe,xm,xv,ys'
