from advent import parse, atoms

wires, exprs = parse(24, lambda s: [ atoms(line) for line in str.split(s,'\n') ], sep='\n\n')

def part1():
    d = {}

    for wire, value in wires:
        d[wire] = value

    for (w1, op, w2, _, out) in exprs:
        d[out] = (op, w1, w2)

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

# ---------------------------------------------------------------------------------------------

assert part1() == 56729630917616
