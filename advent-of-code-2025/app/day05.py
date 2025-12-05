"""Advent of Code 2025: Day 5 - Cafeteria"""

from advent import parse, positive_ints

Ingredient = int
Range = tuple[int, int]

section1, section2 = parse(5, str.split, sep='\n\n')
fresh: list[Range] = [positive_ints(r) for r in section1]  # type: ignore
ingredients: list[Ingredient] = [int(i) for i in section2]


def merge_ranges(fresh: list[Range]) -> set[Range]:
    """Compute a set of disjoint fresh ranges by merging overlapping ranges.
    We first sort the ranges so overlapping ranges are contiguous."""
    fresh = sorted(fresh)
    ranges_overlap = lambda p1, p2: p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[1]
    merge_ranges = lambda pair, p: (min(pair[0], p[0]), max(pair[1], p[1]))
    disjoint_ranges = set()

    while fresh:
        a_range = fresh.pop(0)

        while fresh and ranges_overlap(a_range, fresh[0]):
            other_range = fresh.pop(0)
            a_range = merge_ranges(a_range, other_range)

        disjoint_ranges.add(a_range)

    return disjoint_ranges


def part1(fresh: list[Range], ingredients: list[Ingredient]):
    """Return the number of fresh ingredients by counting the number of ingredients
    in any fresh range."""
    is_fresh = lambda ingredient: any(low <= ingredient <= high for low, high in fresh)

    return sum(1 for ingredient in ingredients if is_fresh(ingredient))


def part2(fresh: list[Range]):
    """Return the total possible fresh ingredient IDs by summing the length of
    each range after merging overlapping ranges."""
    return sum(high - low + 1 for low, high in merge_ranges(fresh))


assert part1(fresh, ingredients) == 707
assert part2(fresh) == 361615643045059
