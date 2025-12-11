"""Advent of Code 2025: Day 11 - Reactor (alt version)"""

from advent import nx, cache

G = nx.read_adjlist(open("app/day11.txt", "rb"), create_using=nx.DiGraph)


@cache
def dfs(node, fft, dac):
    match node:
        case 'out':
            return 1 if fft and dac else 0
        case 'fft':
            fft = True
        case 'dac':
            dac = True

    return sum(dfs(n, fft, dac) for n in G.neighbors(node))


assert dfs('you', True, True) == 640
assert dfs('svr', False, False) == 367579641755680
