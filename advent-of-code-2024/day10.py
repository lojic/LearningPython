from advent import parse, digits, compose, defaultdict, grid_to_hash

input = parse(10, digits)
grid  = defaultdict(lambda: None, grid_to_hash(input))
solve = lambda score: sum([ score(dfs(head, -1, [])) for head, level in grid.copy().items() ])

def dfs(head, prev, result):
    level = grid[head]
    if level != prev + 1:
        return result
    elif level == 9:
        result.append(head)
        return result
    else:
        for dir in (1, 1j, -1, -1j):
            dfs(head + dir, level, result)
        return result

# ---------------------------------------------------------------------------------------------

assert solve(compose(len,set)) == 644
assert solve(len) == 1366
