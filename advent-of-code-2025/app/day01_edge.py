from advent import parse, atom, Callable

input = [(line[0], int(line[1:])) for line in parse(1, atom)]


part1 = lambda current, _: 1 if current == 0 else 0
part2 = lambda _, clicks: clicks


def solve(part: Callable[[int, int], int], count: int = 0, dial: int = 50) -> int:
    for dir, n in input:
        dial, clicks = rotate(dial, dir, n)
        count += part(dial, clicks)

    return count


def rotate(prev: int, dir: str, n: int) -> tuple[int, int]:
    clicks, dial = divmod(prev + (n if dir == 'R' else -n), 100)

    if dir == 'L':
        if prev == 0 and dial != 0:
            clicks += 1
        elif dial == 0 and prev != 0:
            clicks -= 1

    return dial, abs(clicks)


assert solve(part1) == 1154
assert solve(part2) == 6819
