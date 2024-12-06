from advent import parse, remainder

grid          = (parse(6, list))
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
    history = set()

    while guard is not None and guard not in history:
        _, pos = guard
        history.add(guard)
        guard = move(guard)

    return (set(pos for g, pos in history), guard is not None)

def part1():
    return len(path_positions()[0])

def part2():
    def set_ch(pos, ch):
        x, y = int(pos.real), int(pos.imag)
        grid[y][x] = ch

    def is_cycle_with_obstacle(guard, pos):
        set_ch(pos, '#')
        _, cycle = path_positions(guard)
        set_ch(pos, '.')
        return cycle

    guard = get_guard()

    return sum(is_cycle_with_obstacle(guard, pos) for pos in path_positions(guard)[0])

# ---------------------------------------------------------------------------------------------

assert part1() == 4696
assert part2() == 1443
