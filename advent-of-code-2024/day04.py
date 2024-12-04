from advent import parse

input = parse(4, print_lines=None)
width, height = len(input[0]), len(input)
dirs = (1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j)
(e, se, s, sw, w, nw, n, ne) = dirs

def get(c):
    x, y = int(c.real), int(c.imag)
    return input[y][x] if 0 <= x < width and 0 <= y < height else None

def part1():
    def check(c, dir):
        return ['X','M','A','S'] == [ get(c+n*dir) for n in range(4) ]

    return sum(check(complex(x, y), dir) for dir in dirs for x in range(width) for y in range(height))

def part2():
    def check(c, dir):
        return ['M','A','S'] == [ get(c+n*dir) for n in (-1, 0, 1) ]

    def is_x(c):
        return (check(c, ne) or check(c, sw)) and (check(c, nw) or check(c, se))

    return sum(is_x(complex(x, y)) for x in range(width) for y in range(height))

# ---------------------------------------------------------------------------------------------

assert part1() == 2297
assert part2() == 1745
