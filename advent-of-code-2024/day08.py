from advent import parse, grid_to_hash, defaultdict, combinations, gcd

lines         = parse(8, print_lines=None)
width, height = len(lines[0]), len(lines)
antennas      = defaultdict(set)
valid_index   = lambda i: 0 <= i.real < width and 0 <= i.imag < height
solve         = lambda get_nodes: len({ n
                                        for _, s in antennas.items()
                                        for i, j in combinations(s, 2)
                                        for n in get_nodes(i, j) })

for k, v in grid_to_hash(lines, elem_filter=lambda c: c != '.').items():
    antennas[v].add(k)

def part1(i, j):
    return [ n for n in [ i + (i - j), j + (j - i) ] if valid_index(n) ]

def part2(i, j):
    step = (i-j) / gcd(int((i-j).real), int((i-j).imag))
    return { n * step + i for n in range(-width, width) if valid_index(n * step + i) }

# ---------------------------------------------------------------------------------------------

assert solve(part1) == 398
assert solve(part2) == 1333
