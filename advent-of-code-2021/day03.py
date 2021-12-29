# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day03/day03.rkt
from advent import *

input = parse(3, lambda s: [ int(c) for c in s ])

# Compute the column sums. For example:
# [[0, 0, 1]
#  [1, 0, 1]
#  [0, 1, 0]] results in:
#  [1, 1, 2]
compute_sums = lambda lst: [ sum(t) for t in zip(*lst) ]

# Flip 1 to 0 or 0 to 1 in a list of boolean numbers
flip = lambda lst: [ 0 if b == 1 else 1 for b in lst ]

# Return a list of boolean numbers representing the most common
# boolean number in each position of a list of boolean numbers. In
# the case of a tie, use a default value which defaults to 1.
#
# For example:
# [[0, 0, 1, 0]
#  [1, 0, 1, 1]
#  [0, 1, 0, 0]
#  [0, 1, 0, 0]] results in:
#  [0, 1, 1, 0]
def compute_common(lst, default=1):
    half = len(lst) / 2
    def fun(n):
        if n == half:  return default
        elif n > half: return 1
        else:          return 0
    return [ fun(n) for n in compute_sums(lst) ]

# Part 1 solution
def part1(input):
    common   = compute_common(input)
    uncommon = flip(common)
    gamma    = bool_list_to_decimal(common)
    epsilon  = bool_list_to_decimal(uncommon)

    return gamma * epsilon

# Part 2 solution
def part2(input):
    def life(input, oxy):
        num_bits = len(input[0])

        def scrub(lst, oxy, bit):
            common = compute_common(lst)
            xss    = common if oxy else flip(common)
            return [ l for l in lst if l[bit] == xss[bit] ]

        lst = input
        bit = 0
        while True:
            if (bit >= num_bits) or (len(lst) < 2): break
            lst = scrub(lst, oxy, bit)
            bit += 1
        return lst[0]

    return bool_list_to_decimal(life(input, True)) * bool_list_to_decimal(life(input, False))

# Tests ---------------------------------------------------------------------------------------

class TestDay03(unittest.TestCase):
    def test_compute_sums(self):
        self.assertEqual(compute_sums([[0,0,1],[1,0,1],[0,1,0]]), [1,1,2])
    def test_flip(self):
        self.assertEqual(flip([1,0,1,1,0]), [0,1,0,0,1])
    def test_input(self):
        self.assertEqual(input[0], [0,1,1,1,1,0,1,1,1,1,1,0])
    def test_bool_list_to_decimal(self):
        self.assertEqual(bool_list_to_decimal([1,0,1,1]), 11)
    def test_part1(self):
        self.assertEqual(part1(input), 852500)
    def test_part2(self):
        self.assertEqual(part2(input), 1007985)

unittest.main()
