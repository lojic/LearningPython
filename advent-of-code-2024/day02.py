from advent import parse, ints, combinations

input: tuple[tuple[int, ...], ...]
input = parse(2, ints)

def is_safe(t) -> bool:
    helper = lambda t: all(x < y <= (x + 3) for x, y in zip(t, t[1:]))
    return helper(t) or helper(list(reversed(t)))

def is_dampened_safe(t) -> bool:
    return any(is_safe(t) for t in combinations(t, len(t) - 1))

def part1() -> int:
    return sum(1 for t in input if is_safe(t))

def part2() -> int:
    return sum(1 for t in input if is_safe(t) or is_dampened_safe(t))

# ---------------------------------------------------------------------------------------------

assert part1() == 510
assert part2() == 553
