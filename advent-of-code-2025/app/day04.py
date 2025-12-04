"""Advent of Code 2025: Day 4 - Printing Department"""

from advent import parse, grid_to_hash, Generator

grid: dict[complex, str] = grid_to_hash(parse(4, list), elem_filter=lambda c: c == '@')
dirs: tuple[complex, ...] = (-1j, 1 - 1j, 1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j)


def adjacent(pos: complex) -> list[complex]:
    """Return a list of coordinates (as complex numbers) for adjacent rolls
    to the specified position"""
    return [neighbor for dir in dirs if (neighbor := pos + dir) in grid]


def accessible(grid: dict[complex, str]) -> list[complex]:
    """Return a list of coordinates (as complex numbers) for all accessible
    rolls in the grid"""
    return [pos for pos in grid if len(adjacent(pos)) < 4]


def remove_rolls(grid: dict[complex, str]) -> Generator[int, None, None]:
    """Iterate removal of accessible rolls while yielding the number of
    rolls removed for each iteration. Continue until there are no
    accessible rolls remaining"""
    while rolls := accessible(grid):
        for pos in rolls:
            del grid[pos]
        yield len(rolls)


removed = list(remove_rolls(grid))

assert removed[0] == 1564
assert sum(removed) == 9401
