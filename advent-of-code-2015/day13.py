from advent import parse, atoms, permutations

input = [ (name1, n if verb == 'gain' else -n, name2[:-1])
          for name1, _, verb, n, _, _, _, _, _, _, name2 in parse(13, atoms) ]

def happiness(seating, neighbors):
    total = 0
    last  = len(seating) - 1

    for i in range(len(seating)):
        src    = seating[i]
        dst1   = seating[i-1] if i > 0    else seating[last]
        dst2   = seating[i+1] if i < last else seating[0]
        total += (neighbors.get((src, dst1), 0) + neighbors.get((src, dst2), 0))

    return total

def solve(extra=False):
    neighbors = {}
    names     = set()

    for src, n, dst in input:
        neighbors[(src,dst)] = n
        names.add(src)

    if extra:
        names.add('me')

    return max(happiness(seating, neighbors) for seating in permutations(names, len(names)))

# ---------------------------------------------------------------------------------------------

assert solve()     == 733
assert solve(True) == 725
