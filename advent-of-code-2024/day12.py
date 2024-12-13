from advent import parse, grid_to_hash

grid = grid_to_hash(parse(12, list))
dirs = (n, e, s, w) = (-1j, 1, 1j, -1)

def dfs(pos, plant, seen, fences, area=0):
    seen.add(pos)

    for dir in dirs:
        next_pos = pos + dir
        if grid.get(next_pos, None) == plant:
            if next_pos not in seen:
                area, fences = dfs(next_pos, plant, seen, fences, area)
        else:
            fences.append((pos, dir))

    return (area + 1, fences)

def sides(fences):
    sides      = 0
    horizontal = sorted([ (pos, dir) for pos, dir in fences if dir in (n, s) ],
                        key=lambda f: (str(f[1]), f[0].imag, f[0].real))
    vertical   = sorted([ (pos, dir) for pos, dir in fences if dir in (e, w) ],
                        key=lambda f: (str(f[1]), f[0].real, f[0].imag))

    prev_d, prev_x, prev_y = None, None, None

    for pos, dir in horizontal:
        x, y = pos.real, pos.imag
        if dir != prev_d or y != prev_y or x != prev_x + 1:
            sides += 1
        prev_d, prev_x, prev_y = dir, x, y

    prev_d, prev_x, prev_y = None, None, None

    for pos, dir in vertical:
        x, y = pos.real, pos.imag
        if dir != prev_d or x != prev_x or y != prev_y + 1:
            sides += 1
        prev_d, prev_x, prev_y = dir, x, y

    return sides

def solve(part):
    seen = set()
    return sum(area * part(fences) for area, fences in
               [ dfs(pos, grid[pos], seen, []) for pos in grid.keys() if pos not in seen ])

# ---------------------------------------------------------------------------------------------

assert solve(len)   == 1437300
assert solve(sides) == 849332
