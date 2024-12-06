from advent import parse, remainder

grid          = list(parse(6, list, print_lines=None))
width, height = len(grid[0]), len(grid)
rotate        = { '^' : '>', '>' : 'v', 'v' : '<', '<' : '^' }
delta         = { '^' : -1j, '>' : 1,   'v' : 1j,  '<' : -1  }

def get(c):
    x, y = int(c.real), int(c.imag)
    return grid[y][x] if 0 <= x < width and 0 <= y < height else None

def get_guard():
    idx = "".join([ "".join(row) for row in grid ]).find('^')
    return ('^', complex(idx % height, idx // height))

def move(guard):
    g, pos = guard
    pos2   = pos + delta[g]
    ch     = get(pos2)

    match ch:
        case None : return None
        case '#'  : return (rotate[g], pos)
        case _    : return (g, pos2)

def path_positions(guard=get_guard()):
    positions = set()

    while guard is not None:
        _, pos = guard
        positions.add(pos)
        guard = move(guard)

    return positions

def part2():
    def set_ch(x, y, ch):
        grid[y][x] = ch

    def is_cycle_with_obstacle(guard, pos):
        history = set()
        x, y = int(pos.real), int(pos.imag)
        set_ch(x, y, '#') # Place obstacle

        while guard not in history and guard is not None:
            history.add(guard)
            guard = move(guard)

        set_ch(x, y, '.') # Remove obstacle to restore grid
        return guard is not None

    guard = get_guard()

    return sum(is_cycle_with_obstacle(guard, pos) for pos in path_positions(guard))

# ---------------------------------------------------------------------------------------------

assert len(path_positions()) == 4696
assert part2() == 1443
