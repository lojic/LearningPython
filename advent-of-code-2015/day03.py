from advent import parse

input = parse(3)[0]
dir   = { '>' : 1, 'v' : 1j, '<' : -1, '^' : -1j }

def deliver(input=input):
    pos    = complex(0,0)
    houses = { pos }

    for c in input:
        pos += dir[c]
        houses.add(pos)

    return houses

part1 = lambda: len(deliver())
part2 = lambda: len(deliver(input[::2]) | deliver(input[1::2]))

# ---------------------------------------------------------------------------------------------

assert part1() == 2565
assert part2() == 2639
