from advent import parse, ints, combinations, sqrt, nx, prod


def distance(pair: tuple[tuple[int, int, int], tuple[int, int, int]]) -> float:
    ((x1, y1, z1), (x2, y2, z2)) = pair
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def solve_both_parts():
    remaining_boxes = set(parse(8, ints))
    closest_pairs = [
        pair[0]
        for pair in sorted(
            [(pair, distance(pair)) for pair in combinations(remaining_boxes, 2)],
            key=lambda pair: pair[1],
        )
    ]
    n = 1
    G = nx.Graph()

    for box1, box2 in closest_pairs:
        G.add_edge(box1, box2)
        remaining_boxes.discard(box1)
        remaining_boxes.discard(box2)

        if (n := n + 1) == 1000:
            yield prod(sorted([len(s) for s in nx.connected_components(G)], reverse=True)[:3])
        elif not remaining_boxes and nx.is_connected(G):
            yield box1[0] * box2[0]
            return


assert list(solve_both_parts()) == [103488, 8759985540]
