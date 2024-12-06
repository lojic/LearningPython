from advent import parse, remainder, grid_to_hash, defaultdict

lines         = (parse(6, list))
grid          = defaultdict(lambda: None, grid_to_hash(lines, elem_filter=lambda c: c == '#'))
width, height = len(lines[0]), len(lines)
rotate        = { '^' : '>', '>' : 'v', 'v' : '<', '<' : '^' }
delta         = { '^' : -1j, '>' : 1,   'v' : 1j,  '<' : -1  }

def get_guard():
    idx = "".join([ "".join(row) for row in lines ]).find('^')
    return ('^', complex(idx % height, idx // height))

def move(guard):
    g, pos = guard
    pos2   = pos + delta[g]
    x, y   = int(pos2.real), int(pos2.imag)

    if 0 <= x < width and 0 <= y < height:
        if grid[pos2] == '#':
            return (rotate[g], pos)
        else:
            return (g, pos2)
    else:
        return None

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
    def is_cycle_with_obstacle(guard, pos):
        grid[pos] = '#'
        _, cycle = path_positions(guard)
        del grid[pos]
        return cycle

    guard = get_guard()

    return sum(is_cycle_with_obstacle(guard, pos) for pos in path_positions(guard)[0])

# ---------------------------------------------------------------------------------------------

assert part1() == 4696
assert part2() == 1443
