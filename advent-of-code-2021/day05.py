# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day05/day05.rkt
from advent import *

make_step = lambda p: p / max(abs(p.real), abs(p.imag))

def parse_points(x1,y1,x2,y2):
    p1 = complex(x1, y1)
    p2 = complex(x2, y2)
    return (p1, p2, make_step(p2 - p1))

input = [ parse_points(*t) for t in parse(5, ints) ]

def points(line):
    p1, p2, step = line
    n = int(abs((p2 - p1) / step)) + 1
    return [ p1 + i * step for i in range(n) ]

def solve(lines):
    d = collections.defaultdict(lambda: 0)
    for line in lines:
        for point in points(line):
            d[point] += 1
    return len([ v for (k,v) in d.items() if v >= 2 ])

part1 = lambda lines: solve([ (p1, p2, step) for (p1, p2, step) in input
                              if step.real == 0 or step.imag == 0 ])
part2 = solve

# Tests ---------------------------------------------------------------------------------------

class TestDay05(unittest.TestCase):
    def test_points(self):
        self.assertEqual(points([complex(0,0), complex(3,3), complex(1,1)]),
                         [complex(0,0), complex(1,1), complex(2,2), complex(3,3)])
    def test_part1(self):
        self.assertEqual(part1(input), 7318)
    def test_part2(self):
        self.assertEqual(part2(input), 19939)

unittest.main()
