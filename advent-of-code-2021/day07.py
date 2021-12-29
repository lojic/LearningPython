# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day07/day07.rkt
from advent import *

input = parse(7, int, sep=',')

def solve(cost, positions):
    cost_sum = lambda pos: sum([ cost(abs(n-pos)) for n in positions ])

    return min([ cost_sum(pos) for pos in range(max(positions)) ])

part1_cost = lambda n: n
part2_cost = lambda n: (n * (n + 1)) / 2

# Tests ---------------------------------------------------------------------------------------

class TestDay07(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(part1_cost, input), 351_901)
        self.assertEqual(solve(part2_cost, input), 101_079_875)

unittest.main()
