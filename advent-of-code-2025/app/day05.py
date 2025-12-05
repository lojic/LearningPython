"""Advent of Code 2025: Day 5 - Cafeteria"""

from advent import parse, positive_ints

Ingredient = int
Range = tuple[int, int]

section1, section2 = parse(5, str.split, sep='\n\n')
fresh_ranges: list[Range] = [positive_ints(r) for r in section1]  # type: ignore
ingredients: list[Ingredient] = [int(i) for i in section2]


def merge_overlapping_ranges(fresh_ranges: list[Range]) -> set[Range]:
    """Compute a set of disjoint fresh ranges by merging overlapping ranges.
    We first sort the ranges so overlapping ranges are contiguous."""
    fresh_ranges = sorted(fresh_ranges)
    ranges_overlap = lambda p1, p2: p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[1]
    merge_ranges = lambda pair, p: (min(pair[0], p[0]), max(pair[1], p[1]))
    disjoint_ranges = set()

    while fresh_ranges:
        a_range = fresh_ranges.pop(0)

        while fresh_ranges and ranges_overlap(a_range, fresh_ranges[0]):
            other_range = fresh_ranges.pop(0)
            a_range = merge_ranges(a_range, other_range)

        disjoint_ranges.add(a_range)

    return disjoint_ranges


def part1(fresh_ranges: list[Range], ingredients: list[Ingredient]) -> int:
    """Return the number of fresh ingredients by counting the number of ingredients
    in any fresh range."""
    is_fresh = lambda ingredient: any(low <= ingredient <= high for low, high in fresh_ranges)

    return sum(1 for ingredient in ingredients if is_fresh(ingredient))


def part2(fresh_ranges: list[Range]) -> int:
    """Return the total possible fresh ingredient IDs by summing the length of
    each range after merging overlapping ranges."""
    range_size = lambda low, high: high - low + 1

    return sum(range_size(*r) for r in merge_overlapping_ranges(fresh_ranges))


assert part1(fresh_ranges, ingredients) == 707
assert part2(fresh_ranges) == 361615643045059
