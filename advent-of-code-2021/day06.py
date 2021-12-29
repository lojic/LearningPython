# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day06/day06.rkt
from advent import *

input = parse(6, int, sep=',')

def solve(n):
    f = [0] * 9

    for i in input:
        f[i] += 1

    for i in range(n):
        f = [ f[1], f[2], f[3], f[4], f[5], f[6], f[0] + f[7], f[8], f[0] ]

    return sum(f)

# Tests ---------------------------------------------------------------------------------------

class TestDay06(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(80), 371_379)
        self.assertEqual(solve(256), 1_674_303_997_472)

unittest.main()
