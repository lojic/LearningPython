"""Advent of Code 2025: Day 9 - Movie Theater (using shapely)"""

from advent import parse, ints, combinations
from shapely.geometry import Polygon, box


def solve():
    def area(edge) -> int:
        ((x1, y1), (x2, y2)) = edge
        return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

    input = list(parse(9, ints))
    polygon = Polygon(input)

    for (x1, y1), (x2, y2) in sorted(combinations(input, 2), key=area, reverse=True):
        if polygon.contains(box(x1, y1, x2, y2)):
            return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


assert solve() == 1644094530
