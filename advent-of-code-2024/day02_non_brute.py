# The key idea is from reddit i.e. linear scan to invalid pair, then
# try with either of the pair's elements removed.
from advent import parse, ints

input = parse(2, ints)

def is_safe(t, allow_delete=False):
    is_valid = lambda a, b: a < b < (a + 4)

    for i in range(len(t)-1):
        if not is_valid(t[i], t[i+1]):
            return allow_delete and \
                (is_safe(t[i-1:i] + t[i+1:]) or \
                 is_safe(t[i:i+1] + t[i+2:]))
    return True

def part1():
    return sum(is_safe(t) or is_safe(list(reversed(t))) for t in input)

def part2():
    return sum(is_safe(t, True) or is_safe(list(reversed(t)), True) for t in input)

# ---------------------------------------------------------------------------------------------

assert part1() == 510
assert part2() == 553
