from advent import parse, Counter

input = parse(1)[0]

def part1():
    c = Counter(input)
    return c['('] - c[')']

def part2():
    floor = 0
    for pos, c in enumerate(input, start=1):
        match c:
            case '(': floor += 1
            case ')': floor -= 1

        if floor < 0:
            return pos

# ---------------------------------------------------------------------------------------------

assert part1() == 232
assert part2() == 1783
