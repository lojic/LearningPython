from advent import parse, atoms, operator

input = parse(16, atoms)

facts = { 'akitas' : 0, 'cars' : 2, 'cats' : 7, 'children' : 3, 'goldfish' : 5, 'perfumes' : 1,
          'pomeranians' : 3, 'samoyeds' : 2, 'trees' : 3, 'vizslas' : 0 }
part1 = lambda _: operator.eq

def part2(k):
    match k:
        case 'cats' | 'trees':           return operator.lt
        case 'goldfish' | 'pomeranians': return operator.gt
        case _:                          return operator.eq

def solve(part):
    for _, sue, *lst in input:
        if all(part(k)(facts[k], v) for k, v in zip(lst[::2], lst[1::2])):
            return sue

# -------------------------------------------------------------------------------------

assert solve(part1) == 373
assert solve(part2) == 260
