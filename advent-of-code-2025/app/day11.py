"""Advent of Code 2025: Day 11 - Reactor"""

from advent import nx, prod, cache

G = nx.read_adjlist(open("app/day11.txt", "rb"), create_using=nx.DiGraph)


@cache
def dfs(node, dst):
    return 1 if node == dst else sum(dfs(n, dst) for n in G.neighbors(node))


def part1():
    return dfs('you', 'out')


def part2():
    return sum(
        prod(dfs(src, dst) for src, dst in zip(seq, seq[1:]))
        for seq in (('svr', 'fft', 'dac', 'out'), ('svr', 'dac', 'fft', 'out'))
    )


assert part1() == 640
assert part2() == 367579641755680
