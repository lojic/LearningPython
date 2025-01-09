from advent import parse, grid_to_hash

input1, input2 = parse(15, sep='\n\n')
lines          = str.split(input1,'\n')
instructions   = [ { '>' : 1, 'v' : 1j, '<' : -1, '^' : -1j }[c] for c in input2 if c != '\n' ]
gps            = lambda box: 100 * int(box.imag) + int(box.real)
is_box         = lambda c: c == 'O' or c == '[' or c == ']'

def push_boxes(grid, pos, dir, skip_recur=False, quiet=False):
    if not (quiet or push_boxes(grid, pos, dir, quiet=True)):
        return False

    box       = grid[pos]
    other_pos = None
    other_box = None

    if box == 'O' or dir == -1 or dir == 1:
        skip_recur = True
    elif box == '[':
        other_pos = pos + 1
        other_box = ']'
    else:
        other_pos = pos - 1
        other_box = '['

    if skip_recur or push_boxes(grid, other_pos, dir, True, quiet):
        next_pos = pos + dir
        next_box = grid.get(next_pos)

        if next_box is None or is_box(next_box) and push_boxes(grid, next_pos, dir, quiet=quiet):
            if not quiet:
                grid[next_pos] = box
                del grid[pos]
            return True

    return False

def move(grid, bot, dir):
    pos = bot + dir
    box = grid.get(pos)
    return pos if box is None or is_box(box) and push_boxes(grid, pos, dir) else bot

def solve(part):
    grid = part()
    bot  = [ pos for pos, val in grid.items() if val == '@' ][0]
    del grid[bot]

    for dir in instructions:
        bot = move(grid, bot, dir)

    return sum(gps(pos) for pos, val in grid.items() if val in ['[','O'])

# Parts ---------------------------------------------------------------------------------------

def part1():
    return grid_to_hash(lines, elem_filter=lambda c: c != '.')

def part2():
    expand_row = lambda line: [ c for sublist in [ { 'O' : [ '[', ']' ],
                                                     '@' : [ '@', '.' ],
                                                     '#' : [ '#', '#' ],
                                                     '.' : [ '.', '.' ] }[c] for c in line ] for c in sublist ]

    return grid_to_hash(lines, elem_filter=lambda c: c != '.', row_transform=expand_row)

# ---------------------------------------------------------------------------------------------

assert solve(part1) == 1497888
assert solve(part2) == 1522420
