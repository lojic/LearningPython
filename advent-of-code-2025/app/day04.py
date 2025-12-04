from advent import parse, grid_to_hash, Generator

grid: dict[complex, str] = grid_to_hash(parse(4, list), elem_filter=lambda c: c == '@')
dirs: tuple[complex, ...] = (-1j, 1 - 1j, 1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j)
adjacent = lambda pos: [neighbor for dir in dirs if grid.get(neighbor := pos + dir)]
accessible_rolls = lambda grid: [pos for pos in grid.keys() if len(adjacent(pos)) < 4]


def remove_rolls(grid: dict[complex, str]) -> Generator[int, None, None]:
    while rolls := accessible_rolls(grid):
        for pos in rolls:
            del grid[pos]
        yield len(rolls)


removed = list(remove_rolls(grid))

assert removed[0] == 1564
assert sum(removed) == 9401
