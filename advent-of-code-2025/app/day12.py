"""Advent of Code 2025: Day 12 - Tree Farm"""

from advent import parse, ints

regions = [ints(r) for r in parse(12, sep='\n\n')[-1].split('\n')]


def fits(w, h, *quantities):
    return 1 if sum(quantities) <= (w // 3) * (h // 3) else 0


assert sum(fits(*region) for region in regions) == 528
