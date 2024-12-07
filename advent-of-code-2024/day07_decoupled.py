from advent import parse, ints

input = parse(7, ints)

def expressions(operators, operands, exps):
    if len(operands) == 0:
        return exps
    else:
        return expressions(operators, operands[1:], [ e + (o, operands[0]) for e in exps for o in operators ])

def evaluate(exp, result):
    if len(exp) == 0:
        return result
    else:
        match exp[0]:
            case '||': result = int(str(result) + str(exp[1]))
            case '+':  result += exp[1]
            case '*':  result *= exp[1]

        return evaluate(exp[2:], result)

def is_valid(ops, operands):
    return any(operands[0] == evaluate(exp[1:], exp[0]) for exp in expressions(ops, operands[2:], ((operands[1],),)))

def solve(operators):
    return sum(lst[0] for lst in input if is_valid(operators, lst))

# ---------------------------------------------------------------------------------------------

assert solve(('*','+'))      == 2664460013123   # Part 1
assert solve(('*','+','||')) == 426214131924213 # Part 2
