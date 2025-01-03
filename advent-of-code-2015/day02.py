from advent import parse, ints, combinations

input = parse(2, ints)

def paper(l, w, h):
    sides = (l * w, l * h, w * h)
    extra = min(sides)
    return sum(2 * side for side in sides) + extra

def ribbon(l, w, h):
    sides = (2 * (l + w), 2 * (l + h), 2 * (w + h))
    bow   = l * w * h
    return min(sides) + bow

solve = lambda part: sum(part(*dimensions) for dimensions in input)

# ---------------------------------------------------------------------------------------------

assert solve(paper)  == 1588178
assert solve(ribbon) == 3783758
