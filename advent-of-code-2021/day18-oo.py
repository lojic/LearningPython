# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day18/day18.rkt
from advent import *

input = parse(18)

class Node:
    def __init__(self, parent=None, value=None, left=None, right=None):
        self.parent = parent
        self.value  = value
        self.left   = left
        self.right  = right

    def __add__(self, other):
        node         = Node()
        left         = self.dup()
        right        = other.dup()
        left.parent  = node
        right.parent = node
        node.left    = left
        node.right   = right
        return node

    def dup(self):
        return parse_snail(self.to_list())

    def explode(self, level=0):
        if self.regular_node():
            return False
        elif level == 4 and self.pair_of_regulars():
            self.explode_pair()
            return True
        else:
            return self.left.explode(level+1) or self.right.explode(level+1)

    def explode_pair(self):
        left_regular  = self.previous_regular()
        right_regular = self.next_regular()
        if left_regular:
            left_regular.value += self.left.value

        if right_regular:
            right_regular.value += self.right.value

        self.value = 0
        self.left  = None
        self.right = None

    def left_most(self, pred):
        if pred(self):            return self
        elif self.regular_node(): return None
        else:
            return self.left.left_most(pred) or self.right.left_most(pred)

    def magnitude(self):
        if self.regular_node():
            return self.value
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def next_regular(self):
        def helper(parent, child):
            if not parent: return None
            else:
                right = parent.right
                if right and (right != child):
                    node = right.left_most(Node.regular_node)
                    if node:
                        return node
                    else:
                        return helper(parent.parent, parent)
                else:
                    return helper(parent.parent, parent)

        return helper(self.parent, self)

    def pair_node(self):
        return self.left != None and self.right != None

    def pair_of_regulars(self):
        return self.pair_node() and self.left.regular_node() and self.right.regular_node()

    def previous_regular(self):
        def helper(parent, child):
            if not parent: return None
            else:
                left = parent.left
                if left and (left != child):
                    node = left.right_most(Node.regular_node)
                    if node:
                        return node
                    else:
                        return helper(parent.parent, parent)
                else:
                    return helper(parent.parent, parent)

        return helper(self.parent, self)

    def reduce(self):
        if self.explode(): return self.reduce()
        elif self.split(): return self.reduce()
        else:              return self

    def regular_node(self):
        return self.value is not None

    def right_most(self, pred):
        if pred(self):            return self
        elif self.regular_node(): return None
        else:
            return self.right.right_most(pred) or self.left.right_most(pred)

    def split(self):
        def at_least_10(node):
            return node.regular_node() and node.value >= 10

        big = self.left_most(at_least_10)
        if big:
            big.split_regular()
            return True
        else:
            return False

    def split_regular(self):
        quo, rem   = divmod(self.value, 2)
        self.value = None
        self.left  = Node(self, quo)
        self.right = Node(self, quo + rem)

    def to_list(self):
        if self.pair_node():
            return f'[{self.left.to_list()},{self.right.to_list()}]'
        else:
            return f'{self.value}'

def part1(nums):
    sum = nums[0]
    for num in nums[1:]:
        sum = add_reduce(sum, num)
    return sum.magnitude()

def part2(nums):
    combs   = list(combinations(nums, 2))
    tuples  = combs + [ (y,x) for (x,y) in combs ]
    largest = 0
    for t in tuples:
        sum = add_reduce(t[0], t[1]).magnitude()
        if sum > largest: largest = sum
    return largest

# ---------------------------------------------------------------------------------------------

def add_reduce(left, right):
    return (left + right).reduce()

def create_node(snail_number, parent=None):
    if type(snail_number) == list:
        node       = Node(parent)
        node.left  = create_node(snail_number[0], node)
        node.right = create_node(snail_number[1], node)
        return node
    else:
        return Node(parent, snail_number)

def parse():
    return [ parse_snail(line) for line in input ]

def parse_snail(s):
    snail_number = eval(s)
    return create_node(snail_number)

# Tests ---------------------------------------------------------------------------------------

class TestDay18(unittest.TestCase):
    def test_solve(self):
        nums = parse()
        self.assertEqual(part1(nums), 3665)
        self.assertEqual(part2(nums), 4775)

unittest.main()
