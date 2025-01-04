from advent import parse, atoms

input = parse(16, atoms)

facts = { 'akitas' : 0, 'cars' : 2, 'cats' : 7, 'children' : 3, 'goldfish' : 5, 'perfumes' : 1,
          'pomeranians' : 3, 'samoyeds' : 2, 'trees' : 3, 'vizslas' : 0 }

def solve(part):
    for _, sue, *lst in input:
        if all(part(k, v) for k, v in zip(lst[::2], lst[1::2])):
            return sue

def part1(k, v):
    return facts[k] == v

def part2(k, v):
    match k:
        case 'cats' | 'trees':           return facts[k] < v
        case 'goldfish' | 'pomeranians': return facts[k] > v
        case _:                          return facts[k] == v

# -------------------------------------------------------------------------------------

assert solve(part1) == 373
assert solve(part2) == 260
