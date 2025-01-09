from advent import parse, grid_to_hash, nx

def gen_edges(grid):
    for pos, c in grid.items():
        if c in '.SE':
            if grid.get(pos + 1) in '.SE':
                yield (pos, pos + 1)
            if grid.get(pos + 1j)in '.SE':
                yield (pos, pos + 1j)

def solve():
    grid        = grid_to_hash(parse(20, list))
    start       = [ pos for pos, c in grid.items() if c == 'S' ][0]
    goal        = [ pos for pos, c in grid.items() if c == 'E' ][0]
    G           = nx.Graph(gen_edges(grid))
    path_d      = { pos : i for i, pos in enumerate(nx.shortest_path(G, start, goal)) }
    min_savings = 100
    part1       = 0
    part2       = 0

    for pos, i in path_d.items():
        for dx in range(-20, 20 + 1):
            for dy in range(-(20 - abs(dx)), (20 - abs(dx)) + 1):
                pos2 = pos + (dx + dy * 1j)
                if pos2 in path_d:
                    dist = abs(dx) + abs(dy)
                    if (path_d[pos2] - i) - dist >= min_savings:
                        part2 += 1
                        part1 += 1 if dist <= 2 else 0
    return part1, part2

# ---------------------------------------------------------------------------------------------

assert solve() == (1454, 997879) # 2.2 seconds
