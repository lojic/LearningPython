# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day02/day02.rkt
from advent import*

input = parse(2, atoms)

def solve(part, input):
    d = { 'aim' : 0, 'pos' : 0, 'depth' : 0 }
    for pair in input: part(d, *pair)
    return d['pos'] * d['depth']

def part1(d, cmd, n):
    if cmd ==   'forward': d['pos']   += n
    elif cmd == 'down':    d['depth'] += n
    elif cmd == 'up':      d['depth'] -= n

def part2(d, cmd, n):
    if cmd ==   'forward': d['pos'] += n; d['depth'] += (d['aim'] * n)
    elif cmd == 'down':    d['aim'] += n
    elif cmd == 'up':      d['aim'] -= n

class TestDay01(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(solve(part1, input), 1936494)
    def test_part2(self):
        self.assertEqual(solve(part2, input), 1997106066)

unittest.main()
