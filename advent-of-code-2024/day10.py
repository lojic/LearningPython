from advent import parse, digits, compose, defaultdict, grid_to_hash

input         = parse(10, digits)
grid          = defaultdict(lambda: None, grid_to_hash(input))
width, height = len(input[0]), len(input)

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

def solve(score):
    heads = [ pos for x in range(width) for y in range(height) if grid[(pos := complex(x, y))] == 0 ]
    return sum(score(dfs(head, -1, [])) for head in heads)

# ---------------------------------------------------------------------------------------------

assert solve(compose(len,set)) == 644
assert solve(len) == 1366
