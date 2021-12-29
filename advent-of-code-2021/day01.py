# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day01/day01.rkt
from advent import *

input = [ int(x) for x in file_to_lines('day01.txt') ]

def count_increases(lst):
    """Return a count of the number of times a number in the list is
    greater than the preceding number."""
    return len([ y for (x,y) in zip(lst, lst[1:]) if y > x])

def windows(lst):
    """Return a list of 3-element sliding windows from a list"""
    return list(zip(lst, lst[1:], lst[2:]))

def part1():
    return count_increases(input)

def part2():
    return count_increases(list(map(sum, windows(input))))

# Tests ---------------------------------------------------------------------------------------

class TestDay01(unittest.TestCase):
    def test_count_increase(self):
        self.assertEqual(count_increases([3,2,1]), 0)
        self.assertEqual(count_increases([3,2,3,1,2]), 2)

    def test_windows(self):
        self.assertEqual(windows([1,2,3,4,5]), [(1,2,3),(2,3,4),(3,4,5)])

    def test_part1(self):
        self.assertEqual(part1(), 1616)
        
    def test_part2(self):
        self.assertEqual(part2(), 1645)

unittest.main()
