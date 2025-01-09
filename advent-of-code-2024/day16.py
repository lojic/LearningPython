from advent import parse, grid_to_hash, nx

grid      = grid_to_hash(parse(16, list))
(e,s,w,n) = dirs = (1, 1j, -1, -1j)
start     = (1+139j, e)
goal      = (139+1j, None)
G         = nx.DiGraph()

for pos, val in [ (pos, val) for pos, val in grid.items() if val != '#' ]:
    for dir in dirs:
        G.add_edge((pos, dir), (pos, dir *  1j), weight=1000) # rotate right
        G.add_edge((pos, dir), (pos, dir * -1j), weight=1000) # rotate left

        match grid.get(pos + dir):                            # move forward
            case '.': G.add_edge((pos, dir), (pos+dir, dir), weight=1)
            case 'E': G.add_edge((pos, dir), (pos+dir, None), weight=1)

def part1():
    return nx.shortest_path_length(G, source=start, target=goal, weight='weight')

def part2():
    return len({ pos
                 for path in nx.all_shortest_paths(G, start, goal, weight='weight')
                 for pos, _ in path })

# ---------------------------------------------------------------------------------------------

assert part1() == 72428
assert part2() == 456
