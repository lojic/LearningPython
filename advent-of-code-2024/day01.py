from advent import ints, parse, Counter

left, right = zip(*parse(1, ints))

def part1():
    return sum([ abs(l - r) for l, r in zip(sorted(left), sorted(right)) ])

def part2():
    c = Counter(right)
    return sum([ n * c[n] for n in left ])

# ---------------------------------------------------------------------------------------------

assert part1() == 1189304
assert part2() == 24349736
