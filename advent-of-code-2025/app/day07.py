"""Advent of Code 2025: Day 7 - Laboratories"""

from advent import parse, grid_to_dict, defaultdict

grid = grid_to_dict(parse(7, list))
tachyons = defaultdict(int, {k: 1 for k, v in grid.items() if v == 'S'})
splits, total = 0, 0

while tachyons:
    for pos, n in list(tachyons.items()):
        del tachyons[pos]
        pos = pos + 1j

        match grid.get(pos):
            case '.':
                tachyons[pos] += n
            case '^':
                splits += 1
                for delta in [-1, 1]:
                    tachyons[pos + delta] += n
            case None:
                total += n

assert (splits, total) == (1662, 40941112789504)
