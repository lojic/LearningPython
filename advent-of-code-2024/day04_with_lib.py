from advent import parse, grid_word_search

input = parse(4)
(se, sw, nw, ne) = (1+1j, -1+1j, -1-1j, 1-1j)

def part1():
    return len(grid_word_search(input, "XMAS"))

def part2():
    diag1 = { (x, y) for (x, y, d) in grid_word_search(input, "MAS", (-1, 0, 1), (ne, sw)) }
    diag2 = { (x, y) for (x, y, d) in grid_word_search(input, "MAS", (-1, 0, 1), (se, nw)) }
    return len(diag1 & diag2)

# ---------------------------------------------------------------------------------------------

assert part1() == 2297
assert part2() == 1745
