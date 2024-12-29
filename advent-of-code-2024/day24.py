# Part 1 on my own. Part 2 via ideas from lscddit on reddit.
from advent import parse, atoms

wires, exprs = parse(24, lambda s: [ atoms(line) for line in str.split(s,'\n') ], sep='\n\n')
d = {}

for wire, value in wires:
    d[wire] = value

for (w1, op, w2, _, out) in exprs:
    d[out] = (op, w1, w2)

def part1():
    def evaluate(expr):
        match expr:
            case int(value): return value
            case str(key):   return evaluate(d[key])
            case (op, w1, w2):
                a = evaluate(d[w1])
                b = evaluate(d[w2])
                match op:
                    case 'AND': return a & b
                    case 'OR':  return a | b
                    case 'XOR': return a ^ b

    return sum((evaluate(key) << i) for i, key in enumerate(sorted([ key for key in d if key[0] == 'z' ])))

def part2():
    operations = [ (key, val) for key, val in d.items() if isinstance(val, tuple) ]
    wrong      = set()

    for out, (op, w1, w2) in operations:
        if out[0] == 'z' and op != 'XOR' and out != 'z45':
            wrong.add(out)

        if op == 'XOR' and \
           out[0] not in ('x', 'y', 'z') and \
           w1[0] not in ('x', 'y', 'z') and \
           w2[0] not in ('x', 'y', 'z'):
            wrong.add(out)

        if op == 'AND' and 'x00' not in (w1, w2):
            for out2, (op2, w1_2, w2_2) in operations:
                if (out == w1_2 or out == w2_2) and op2 != 'OR':
                    wrong.add(out)

        if op == 'XOR':
            for out2, (op2, w1_2, w2_2) in operations:
                if (out == w1_2 or out == w2_2) and op2 == 'OR':
                    wrong.add(out)

    return ",".join(sorted(wrong))

# ---------------------------------------------------------------------------------------------

assert part1() == 56729630917616
assert part2() == 'bjm,hsw,nvr,skf,wkr,z07,z13,z18'
