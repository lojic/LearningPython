"""Advent of Code 2025: Day 8 - Playground (using a graph)"""

from advent import parse, ints, combinations, dist, nx, prod


def solve_both_parts():
    boxes = set(parse(8, ints))
    G = nx.Graph()

    for n, (box1, box2) in enumerate(sorted(combinations(boxes, 2), key=lambda pair: dist(*pair)), 1):
        G.add_edge(box1, box2)
        boxes.discard(box1)
        boxes.discard(box2)

        if n == 1000:
            yield prod(sorted([len(s) for s in nx.connected_components(G)], reverse=True)[:3])
        elif not boxes and nx.is_connected(G):
            yield box1[0] * box2[0]
            return


assert list(solve_both_parts()) == [103488, 8759985540]
