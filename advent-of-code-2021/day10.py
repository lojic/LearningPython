# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day10/day10.rkt
from advent import *

def closing_bracket_for(c):
    if   c == '(': return ')'
    elif c == '[': return ']'
    elif c == '{': return '}'
    elif c == '<': return '>'
    else: return False

is_open_bracket = closing_bracket_for
closes          = lambda open_bracket: lambda c: c == closing_bracket_for(open_bracket)
corrupt         = lambda c: type(c) == str
incomplete      = lambda x: type(x) == list

def parse_line(chars):
    stack = []
    for c in chars:
        if is_open_bracket(c):
            stack.append(c)
        elif closes(stack[-1])(c):
            stack.pop()
        else:
            return c
    return stack

input = [ parse_line(chars) for chars in parse(10, list) ]

def stack_value(stack):
    def value_of(c):
        if   c == ')': return 1
        elif c == ']': return 2
        elif c == '}': return 3
        elif c == '>': return 4

    val = 0
    while stack:
        c   = stack.pop()
        val = (val * 5) + value_of(closing_bracket_for(c))
    return val

def part1(input):
    def value_of(c):
        if   c == ')': return 3
        elif c == ']': return 57
        elif c == '}': return 1197
        elif c == '>': return 25137

    return sum([ value_of(c) for c in input if corrupt(c) ])

def part2(input):
    incompletes = [ l for l in input if incomplete(l) ]
    midpoint    = len(incompletes) // 2
    return sorted([ stack_value(s) for s in incompletes ])[midpoint]

# Tests ---------------------------------------------------------------------------------------

class TestDay10(unittest.TestCase):
    def test_parts(self):
        self.assertEqual(part1(input), 390_993)
        self.assertEqual(part2(input), 2_391_385_187)

unittest.main()
