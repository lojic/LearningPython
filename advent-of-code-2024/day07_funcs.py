# Coded this version after spotting higher order functions in another solution.
from advent import parse, ints

input = parse(7, ints)

plus = lambda x, y: x + y
mult = lambda x, y: x * y
conc = lambda x, y: int(str(x) + str(y))

def is_valid(ops, answer, result, operands):
    if  result > answer:
        return False
    elif len(operands) == 0:
        return result == answer
    else:
        return any(is_valid(ops, answer, op(result, operands[0]), operands[1:]) for op in ops)

def solve(*operators):
    return sum(lst[0] for lst in input if is_valid(operators, lst[0], lst[1], lst[2:]))

# ---------------------------------------------------------------------------------------------

assert solve(mult, plus)       == 2664460013123   # Part 1
assert solve(mult, plus, conc) == 426214131924213 # Part 2
