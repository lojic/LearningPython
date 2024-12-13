from advent import parse, ints
import numpy as np

input   = parse(13, ints, sep='\n\n')
epsilon = 0.0001
err     = 10000000000000

def cost(a00, a10, a01, a11, b0, b1, offset, limit):
    coefficients = np.array([[a00, a01],[a10, a11]])
    unknowns     = np.array([b0 + offset, b1 + offset])
    a, b         = np.linalg.solve(coefficients, unknowns)
    a_int, b_int = round(a), round(b)

    if 0 <= a_int <= limit and 0 <= b_int <= limit and abs(a - a_int) < epsilon and abs(b - b_int) < epsilon:
        return 3 * a_int + b_int

def solve(offset=0, limit=100):
    return sum(c for t in input if (c := cost(*t, offset, limit)))

# ---------------------------------------------------------------------------------------------

assert solve()         == 29436
assert solve(err, err) == 103729094227877
