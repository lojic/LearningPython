from advent import parse, ints, nx, binary_search

blocks = [ complex(x,y) for x, y in parse(18, ints) ]
dim    = 71
goal   = 70+70j

def create_graph(blocks):
    def gen_edges(blocks):
        for x in range(dim):
            for y in range(dim):
                if (pos := complex(x, y)) not in blocks:
                    if (x + 1) < dim and (east := pos + 1) not in blocks:
                        yield (pos, east)
                    if (y + 1) < dim and (south := pos + 1j) not in blocks:
                        yield (pos, south)

    G = nx.Graph()
    G.add_edges_from(gen_edges(blocks))
    return G

def part1():
    return nx.shortest_path_length(create_graph(set(blocks[:1024])), 0, goal)

def part2():
    def predicate(n):
        G = create_graph(set(blocks[:n+1]))
        return not(goal in G and nx.has_path(G, 0, goal))

    return blocks[binary_search(predicate, 1024, len(blocks))]

# ---------------------------------------------------------------------------------------------

assert part1() == 344
assert part2() == complex(46, 18)
