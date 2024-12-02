# This version used an idea from Triangle Devs discord to compute the
# deltas instead of needing to reverse the list.

from advent import parse, ints, combinations

input = parse(2, ints)

def is_safe(t):
    deltas = [ b - a for a, b in zip(t, t[1:]) ]

    return all(delta in range(1,4) for delta in deltas) or \
        all(delta in range(-3, 0) for delta in deltas)

def is_dampened_safe(t):
    return any(is_safe(t) for t in combinations(t, len(t) - 1))

def part1():
    return sum([ 1 for t in input if is_safe(t) ])

def part2():
    return sum([ 1 for t in input if is_safe(t) or is_dampened_safe(t) ])

# ---------------------------------------------------------------------------------------------

assert part1() == 510
assert part2() == 553
