from advent import parse, atom, Callable

input = [(line[0], int(line[1:])) for line in parse(1, atom)]


part1 = lambda dial, _: 1 if dial == 0 else 0
part2 = lambda _, clicks: clicks


def solve(part: Callable[[int, int], int], count: int = 0, dial: int = 50) -> int:
    for dir, n in input:
        clicks, dial = divmod(dial + (n if dir == 'R' else -n), 100)
        count += part(dial, abs(clicks))

    return count


assert solve(part1) == 1154
assert solve(part2) == 6819
