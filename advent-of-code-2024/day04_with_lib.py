from advent import parse, grid_word_search

input = parse(4)
(se, sw, nw, ne) = (1+1j, -1+1j, -1-1j, 1-1j)

def part1():
    return len(list(grid_word_search(input, "XMAS")))

def part2():
    diag1 = { (x, y) for (x, y, d) in grid_word_search(input, "MAS", (ne, sw), -1) }
    diag2 = { (x, y) for (x, y, d) in grid_word_search(input, "MAS", (se, nw), -1) }
    return len(diag1 & diag2)

# ---------------------------------------------------------------------------------------------

assert part1() == 2297
assert part2() == 1745
