from advent import parse, ints, combinations

input = parse(2, ints)

def is_safe(t):
    def helper(t):
        for x, y in zip(t, t[1:]):
            if not x < y <= (x + 3):
                return False
        return True

    return helper(t) or helper(list(reversed(t)))

def is_dampened_safe(t):
    for t in combinations(t, len(t) - 1):
        if is_safe(t):
            return True
    return False

def part1():
    return sum([ 1 for t in input if is_safe(t) ])

def part2():
    return sum([ 1 for t in input if is_safe(t) or is_dampened_safe(t) ])

# ---------------------------------------------------------------------------------------------

assert part1() == 510
assert part2() == 553
