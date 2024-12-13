from advent import parse, ints
from sympy import symbols, Eq, solve

input   = parse(13, ints, sep='\n\n', print_lines=3)
epsilon = 0.0001
err     = 10000000000000

def cost(a0, a1, a2, a3, b0, b1, offset, limit):
    x, y = symbols('x y')
    eq1 = Eq(a0*x + a2*y, b0 + offset)
    eq2 = Eq(a1*x + a3*y, b1 + offset)
    solution = solve((eq1, eq2), (x, y))
    a, b = solution[x], solution[y]
    a_int, b_int = round(a), round(b)

    if 0 <= a_int <= limit and 0 <= b_int <= limit and abs(a - a_int) < epsilon and abs(b - b_int) < epsilon:
        return 3 * a_int + b_int

def run(offset=0, limit=100):
    return sum(c for t in input if (c := cost(*t, offset, limit)))

# ---------------------------------------------------------------------------------------------

assert run()         == 29436
assert run(err, err) == 103729094227877
