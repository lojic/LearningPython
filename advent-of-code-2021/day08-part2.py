# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day08/day08-part2.rkt
from advent import *

input = parse(8, lambda line: mapt(atoms, line.split(' | ')))

def solve(input):
    return sum([ entry(lst[0], lst[1]) for lst in input])

def entry(lst, digits):
    sets = make_sets(lst)
    d1   = find(sets, by_count(2))
    d7   = find(sets, by_count(3))
    d4   = find(sets, by_count(4))
    d8   = find(sets, by_count(7))
    d6   = find(sets, by_subtraction(d1, 6, 5))
    d2   = find(sets, by_subtraction(d4, 5, 3))
    d9   = find(sets, by_subtraction(d4 | d7, 6, 1))
    d0   = find(sets, by_exclusion([d6, d9], 6))
    d3   = find([ s for s in sets if s != d2 ], by_subtraction(d7, 5, 2))
    d5   = find([ s for s in sets if s != d2 ], by_subtraction(d7, 5, 3))
    d    = { d0 : 0, d1 : 1, d2 : 2, d3 : 3, d4 : 4, d5 : 5, d6 : 6, d7 : 7, d8 : 8, d9 : 9 }
    digit_sets = make_sets(digits)

    return display_value(d, digit_sets)

def make_sets(lst):
    return [ frozenset(s) for s in lst ] # frozenset is hashable, set is not

def find(lst, pred):
    return findf(pred, lst)

def by_count(n):
    return lambda s: n == len(s)

def by_exclusion(exclude, l):
    return lambda s: l == len(s) and (not s in exclude)

def by_subtraction(sub, l, cnt):
    return lambda s: l == len(s) and cnt == len(s - sub)

def display_value(d, digits):
    return 1000 * d[digits[0]] + 100 * d[digits[1]] + 10 * d[digits[2]] + d[digits[3]]

# Tests ---------------------------------------------------------------------------------------

class TestDay08(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), 1027483)

unittest.main()
