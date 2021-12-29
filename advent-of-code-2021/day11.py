# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day11/day11.rkt
from advent import *

# An octopus is represented by a 3-tuple:  (coord, energy, flashed)
octopus_coord   = lambda o: o[0]
octopus_energy  = lambda o: o[1]
octopus_flashed = lambda o: o[2]

input = parse(11,list)

def part1(octopi, n):
    sum = 0
    while n > 0:
        octopi = step(octopi)
        n -= 1
        sum += quantify(octopi, octopus_flashed)
    return sum

def part2(octopi):
    n = 0
    while not all(octopus_flashed(o) for o in octopi):
        octopi = step(octopi)
        n += 1
    return n

def reset(octopi):
    return [ reset_octo(o) if octopus_flashed(o) else o for o in octopi ]

def increment_energy(octopi):
    return [ increment_octo(o) for o in octopi ]

def flash(octopi):
    # Helpers ---------------------------------------------------------------------------------
    def flash_needed(octo):
        return (octopus_energy(octo) > 9) and (not octopus_flashed(octo))

    def flash_one_octopus(octo, octopi):
        def neighbors_of(coord):
            return [ coord + i for i in [ -1j, 1, +1j, -1, 1-1j, -1-1j, 1+1j, -1+1j ]]

        def mark_flashed(o): return (o[0], o[1], True)

        adjacent = neighbors_of(octopus_coord(octo))

        def update_octo(o):
            if octopus_coord(o) == octopus_coord(octo): return mark_flashed(o)
            elif octopus_coord(o) in adjacent:          return increment_octo(o)
            else:                                       return o

        return [ update_octo(o) for o in octopi ]
    # -----------------------------------------------------------------------------------------

    octo = findf(flash_needed, octopi)

    while octo:
        octopi = flash_one_octopus(octo, octopi)
        octo   = findf(flash_needed, octopi)

    return octopi

def parse():
    N = 10
    to_coord = lambda x, y: x + y * +1j
    octopi = []

    for y in range(N):
        for x in range(N):
            octopi.append((to_coord(x,y), int(input[y][x]), False))
    return octopi

step           = lambda octopi: flash(increment_energy(reset(octopi)))
increment_octo = lambda o: (o[0], o[1] + 1, o[2])
reset_octo     = lambda o: (o[0], 0, False)

# Tests ---------------------------------------------------------------------------------------

class TestDay11(unittest.TestCase):
    def test_parts(self):
        octopi = parse()
        self.assertEqual(part1(octopi, 100), 1647)
        self.assertEqual(part2(octopi), 348)

unittest.main()
