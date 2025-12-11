"""Advent of Code 2025: Day 11 - Reactor"""

from advent import parse, atoms, nx, prod, cache

G = nx.DiGraph()

for source, *sinks in parse(11, atoms, print_lines=3):
    for sink in sinks:
        G.add_edge(source, sink)


def part1():
    return len(list(nx.all_simple_paths(G, 'you', 'out')))


def part2():
    @cache
    def dfs(node, sink):
        return 1 if node == sink else sum(dfs(n, sink) for n in G.neighbors(node))

    return sum(
        prod(dfs(src, dst) for src, dst in zip(seq, seq[1:]))
        for seq in (('svr', 'fft', 'dac', 'out'), ('svr', 'dac', 'fft', 'out'))
    )


assert part1() == 640
assert part2() == 367579641755680
