from advent import parse, grid_to_hash, nx

lines       = parse(20, list)
width       = len(lines[0])
height      = len(lines)
grid        = grid_to_hash(lines)
start       = [ pos for pos, c in grid.items() if c == 'S' ][0]
end         = [ pos for pos, c in grid.items() if c == 'E' ][0]
grid[start] = grid[end] = '.'
candidates  = []

def gen_edges():
    for x in range(width):
        for y in range(height):
            pos     = complex(x, y)
            pos_c   = grid[pos]
            east    = pos + 1
            east_c  = grid.get(east,  None)
            south   = pos + 1j
            south_c = grid.get(south, None)

            if pos_c == '.':
                if east_c == '.':
                    yield (pos, east)
                if south_c == '.':
                    yield (pos, south)
            elif pos_c == '#':
                west    = pos -1
                west_c  = grid.get(west,  None)
                north   = pos - 1j
                north_c = grid.get(north, None)

                if (east_c == '.' and west_c == '.') or (north_c == '.' and south_c == '.'):
                    candidates.append(pos)

def remove_wall(g, pos):
    if grid.get(pos - 1, None) == '.' and grid.get(pos + 1, None) == '.':
        g.add_edge(pos - 1, pos)
        g.add_edge(pos, pos + 1)

    if grid.get(pos - 1j, None) == '.' and grid.get(pos + 1j, None) == '.':
        g.add_edge(pos - 1j, pos)
        g.add_edge(pos, pos + 1j)

def replace_wall(g, pos):
    g.remove_node(pos)

def part1():
    G = nx.Graph()
    G.add_edges_from(gen_edges())
    path_length = nx.shortest_path_length(G, start, end)

    def cheat_ok(pos):
        remove_wall(G, pos)
        cheat_length = nx.shortest_path_length(G, start, end)
        replace_wall(G, pos)
        return path_length - cheat_length >= 100

    return sum(1 for pos in candidates if cheat_ok(pos))

assert part1() == 1454
