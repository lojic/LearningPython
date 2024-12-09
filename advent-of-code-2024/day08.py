from advent import parse, grid_to_hash, defaultdict, combinations, gcd

lines         = parse(8)
width, height = len(lines[0]), len(lines)
antennas      = defaultdict(set)
valid_index   = lambda i: 0 <= i.real < width and 0 <= i.imag < height
solve         = lambda get_nodes: len({ n
                                        for s in antennas.values()
                                        for i, j in combinations(s, 2)
                                        for n in get_nodes(i, j, i - j) })

for k, v in grid_to_hash(lines, elem_filter=lambda c: c != '.').items():
    antennas[v].add(k)

def part1(i, j, diff):
    return filter(valid_index, [ i + diff, j - diff ])

def part2(i, j, diff):
    step = diff / gcd(int(diff.real), int(diff.imag))
    return filter(valid_index, { n * step + i for n in range(-width, width) })

# ---------------------------------------------------------------------------------------------

assert solve(part1) == 398
assert solve(part2) == 1333
