"""Advent of Code 2025: Day 8 - Playground

The key elements of this solution are:
1. Form the combinations of all junction boxes, and pair with the distance between them
2. Use a set to represent a circuit

Since part 2 is a continuation of part 1, I use a generator function to yield the
answer for part 1, and then continue processing to yield the answer for part 2. The
condition for yielding part 1 is when 1,000 pairs of boxes have been connected. The
condition for yielding part 2 is when there is a single circuit, and there are no
remaining boxes to process.

There are four main cases to consider when connecting two junction boxes:
1. If both boxes already exist in separate circuits, we merge the two circuits
2. If only box1 is in a circuit, we add box2 to that circuit
3. If only box2 is in a circuit, we add box1 to that circuit
4. Neither box is in a circuit, add the pair as a new circuit"""

from advent import parse, ints, combinations, sqrt


def distance(pair: tuple[tuple[int, int, int], tuple[int, int, int]]) -> float:
    """Return the Euclidean distance between two 3D points"""
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
    circuits = [{box for box in closest_pairs[0]}]
    n = 1

    for box1, box2 in closest_pairs:
        remaining_boxes.discard(box1)
        remaining_boxes.discard(box2)
        circuit1 = next((c for c in circuits if box1 in c), None)
        circuit2 = next((c for c in circuits if box2 in c), None)

        if circuit1 and circuit2:
            if circuit1 == circuit2:
                pass  # boxes already in same circuit
            else:
                circuits.remove(circuit1)
                circuits.remove(circuit2)
                circuits.append(circuit1 | circuit2)
        elif circuit1:
            circuit1.add(box2)
        elif circuit2:
            circuit2.add(box1)
        else:
            circuits.append(set((box1, box2)))

        if (n := n + 1) == 1000:
            circuits.sort(key=lambda s: len(s), reverse=True)
            yield len(circuits[0]) * len(circuits[1]) * len(circuits[2])
        elif len(circuits) == 1 and not remaining_boxes:
            yield box1[0] * box2[0]
            return


assert list(solve_both_parts()) == [103488, 8759985540]
