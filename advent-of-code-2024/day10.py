from advent import parse, digits, compose, defaultdict, grid_to_hash

grid  = defaultdict(lambda: None, grid_to_hash(parse(10, digits)))
solve = lambda score: sum([ score(dfs(head, -1, [])) for head, level in grid.copy().items() if level == 0 ])

def dfs(pos, prev, result):
    level = grid[pos]
    if level != prev + 1:
        return result
    elif level == 9:
        return result + [ pos ]
    else:
        for dir in (1, 1j, -1, -1j):
            result = dfs(pos + dir, level, result)
        return result

# ---------------------------------------------------------------------------------------------

assert solve(compose(len,set)) == 644
assert solve(len) == 1366
