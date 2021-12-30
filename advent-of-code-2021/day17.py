# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day17/day17.rkt
from advent import *

x_min, x_max, y_min, y_max = 206, 250, -105, -57

part1 = lambda lst: max([ l[2] for l in chain.from_iterable(lst) ])
part2 = lambda lst: len(lst)

def solve(part):
    velocities = []
    for dx in range(1, x_max + 2):
        for dy in range(y_min - 1, 2 * -y_min + 1):
            lst = shoot(dx, dy)
            if lst: velocities.append(lst)
    return part(velocities)

def shoot(dx, dy):
    x, y, top, results = 0, 0, 0, []
    while x <= x_max and y >= y_min:
        if x >= x_min and y <= y_max:
            results.append((dx, dy, top))

        if dx > 0:   dx -= 1
        elif dx < 0: dx += 1

        dy -= 1
        x  += dx
        y  += dy
        top = max(y, top)

    return results

# Tests ---------------------------------------------------------------------------------------

class TestDay17(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(part1), 5460)
        self.assertEqual(solve(part2), 3618)

unittest.main()
