from advent import parse, digits, compose

input         = parse(10, digits)
width, height = len(input[0]), len(input)

def get(c):
    return input[y][x] if 0 <= (x := int(c.real)) < width and 0 <= (y := int(c.imag)) < height else None

def dfs(head, prev, result):
    level = get(head)
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
    heads = [ pos for x in range(width) for y in range(height) if get(pos := complex(x, y)) == 0 ]
    return sum(score(dfs(head, -1, [])) for head in heads)

# ---------------------------------------------------------------------------------------------

assert solve(compose(len,set)) == 644
assert solve(len) == 1366
