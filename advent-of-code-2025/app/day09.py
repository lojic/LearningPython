"""Advent of Code 2025: Day 9 - Movie Theater"""

from advent import parse, ints, combinations, defaultdict


def area(edge) -> int:
    ((x1, y1), (x2, y2)) = edge
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


input = list(parse(9, ints))
pairs = sorted(combinations(input, 2), key=area, reverse=True)
edges = list(zip(input, input[1:] + [input[0]]))


def add_outside_border(edges, outside) -> None:
    """Walk the border of the polygon, and for every point,
    add one to the right to represent the outside."""
    for edge in edges:
        ((x1, y1), (x2, y2)) = edge
        hdelta = x2 - x1
        vdelta = y2 - y1

        if abs(hdelta) == 0:
            if vdelta > 0:
                for y in range(y1, y2 + 1):
                    outside[x1 + 1].add(y)
            else:
                for y in range(y2, y1 + 1):
                    outside[x1 - 1].add(y)
        else:
            if hdelta > 0:
                for x in range(x1, x2 + 1):
                    outside[x].add(y1 - 1)
            else:
                for x in range(x2, x1 + 1):
                    outside[x].add(y1 + 1)


def remove_poly_border(edges, outside) -> None:
    """Walk the border of the polygon, and remove every
    point that was erroneously added to the outside dict."""
    for edge in edges:
        ((x1, y1), (x2, y2)) = edge

        hdelta = x2 - x1
        vdelta = y2 - y1

        if abs(hdelta) == 0:
            if vdelta > 0:
                for y in range(y1, y2 + 1):
                    outside[x1].discard(y)
            else:
                for y in range(y2, y1 + 1):
                    outside[x1].discard(y)
        else:
            if hdelta > 0:
                for x in range(x1, x2 + 1):
                    outside[x].discard(y1)
            else:
                for x in range(x2, x1 + 1):
                    outside[x].discard(y1)


def is_valid(x1, y1, x2, y2, outside) -> bool:
    """Indicate whether the rectangle is valid by checking if any
    outside points exist between y1 & y2 for every x coordinate."""
    miny, maxy = min(y1, y2), max(y1, y2)

    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in outside[x]:
            if miny <= y <= maxy:
                return False

    return True


def solve(is_valid):
    """Return the area of the first valid rectangle,
    since we're checking in descending order by size."""
    outside = defaultdict(set)
    add_outside_border(edges, outside)
    remove_poly_border(edges, outside)

    for (x1, y1), (x2, y2) in pairs:
        if is_valid(x1, y1, x2, y2, outside):
            return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


assert solve(lambda *_: True) == 4737096935
assert solve(is_valid) == 1644094530
