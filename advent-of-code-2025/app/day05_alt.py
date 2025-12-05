"""Advent of Code 2025: Day 5 - Cafeteria (alt version w/ post-hoc knowledge)"""

from advent import parse, positive_ints

Ingredient = int
Range = tuple[int, int]

section1, section2 = parse(5, str.split, sep='\n\n')
fresh: list[Range] = [positive_ints(r) for r in section1]  # type: ignore
ingredients: list[Ingredient] = [int(i) for i in section2]


def part1(fresh: list[Range], ingredients: list[Ingredient]) -> int:
    is_fresh = lambda ingredient: any(low <= ingredient <= high for low, high in fresh)

    return sum(1 for ingredient in ingredients if is_fresh(ingredient))


def part2(fresh: list[Range]) -> int:
    fresh = sorted(fresh)
    total = 0

    while fresh:
        a_range = fresh.pop(0)

        while fresh and a_range[1] >= fresh[0][0]:
            a_range = (a_range[0], max(a_range[1], fresh.pop(0)[1]))

        total += a_range[1] - a_range[0] + 1

    return total


assert part1(fresh, ingredients) == 707
assert part2(fresh) == 361615643045059
