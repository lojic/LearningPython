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

def part1(nums):
    sum = nums[0]
    for num in nums[1:]:
        sum = add_reduce(sum, num)
    return magnitude(sum)

def part2(nums):
    combs   = list(combinations(nums, 2))
    tuples  = combs + [ (y,x) for (x,y) in combs ]
    largest = 0
    for t in tuples:
        sum = magnitude(add_reduce(t[0], t[1]))
        if sum > largest: largest = sum
    return largest

# ---------------------------------------------------------------------------------------------

def add(left, right):
    node         = Node()
    left         = copy_node(left)
    right        = copy_node(right)
    left.parent  = node
    right.parent = node
    node.left    = left
    node.right   = right
    return node

def add_reduce(left, right):
    return reduce(add(left, right))

def copy_node(node):
    return parse_snail(to_list(node))

def create_node(snail_number, parent=None):
    if type(snail_number) == list:
        node       = Node(parent)
        node.left  = create_node(snail_number[0], node)
        node.right = create_node(snail_number[1], node)
        return node
    else:
        return Node(parent, snail_number)

def explode(node, level=0):
    if regular_node(node):
        return False
    elif level == 4 and pair_of_regulars(node):
        explode_pair(node)
        return True
    else:
        return explode(node.left, level+1) or explode(node.right, level+1)

def explode_pair(node):
    left_regular  = previous_regular(node)
    right_regular = next_regular(node)
    if left_regular:
        left_regular.value += node.left.value

    if right_regular:
        right_regular.value += node.right.value

    node.value = 0
    node.left  = None
    node.right = None

def left_most(pred, node):
    if not node:             return None
    elif pred(node):         return node
    elif regular_node(node): return None
    else:
        return left_most(pred, node.left) or left_most(pred, node.right)

def magnitude(node):
    if regular_node(node):
        return node.value
    else:
        return 3 * magnitude(node.left) + 2 * magnitude(node.right)

def next_regular(node):
    def helper(parent, child):
        if not parent: return None
        else:
            right = parent.right
            if right and (right != child):
                node = left_most(regular_node, right)
                if node:
                    return node
                else:
                    return helper(parent.parent, parent)
            else:
                return helper(parent.parent, parent)

    return helper(node.parent, node)

def pair_node(node):
    return node.left != None and node.right != None

def pair_of_regulars(node):
    return pair_node(node) and regular_node(node.left) and regular_node(node.right)

def parse():
    return [ parse_snail(line) for line in input ]

def parse_snail(s):
    snail_number = eval(s)
    return create_node(snail_number)

def previous_regular(node):
    def helper(parent, child):
        if not parent: return None
        else:
            left = parent.left
            if left and (left != child):
                node = right_most(regular_node, left)
                if node:
                    return node
                else:
                    return helper(parent.parent, parent)
            else:
                return helper(parent.parent, parent)

    return helper(node.parent, node)

def reduce(node):
    if explode(node): return reduce(node)
    elif split(node): return reduce(node)
    else:             return node

def regular_node(node):
    return node.value != None

def right_most(pred, node):
    if not node:             return None
    elif pred(node):         return node
    elif regular_node(node): return None
    else:
        return right_most(pred, node.right) or right_most(pred, node.left)

def split(node):
    def at_least_10(node):
        return regular_node(node) and node.value >= 10

    big = left_most(at_least_10, node)
    if big:
        split_regular(big)
        return True
    else:
        return False

def split_regular(node):
    quo, rem   = divmod(node.value, 2)
    node.value = None
    node.left  = Node(node, quo)
    node.right = Node(node, quo + rem)

def to_list(node):
    if pair_node(node):
        return f'[{to_list(node.left)},{to_list(node.right)}]'
    else:
        return f'{node.value}'

def find_corrupt_link(node):
    if node.left and node.left.parent != node:
        return node.left
    if node.right and node.right.parent != node:
        return node.right
    if node.left:
        left = find_corrupt_link(node.left)
        if left:
            return left
    if node.right:
        right = find_corrupt_link(node.right)
        if right:
            return right
    return None

# Tests ---------------------------------------------------------------------------------------

class TestDay18(unittest.TestCase):
    def test_solve(self):
        nums = parse()
        self.assertEqual(part1(nums), 3665)
        self.assertEqual(part2(nums), 4775)

unittest.main()
