from advent import parse, atoms
import numpy as np

N     = 1000
input = [ tuple(reversed(t[:2] + t[3:6])) for t in [ tuple(reversed(t)) for t in parse(6, atoms) ] ]

def part1():
    lights = np.zeros((N,N), bool)

    for cmd, x1, y1, x2, y2 in input:
        view = lights[x1:x2+1, y1:y2+1]
        match cmd:
            case 'off':    view[...] = False
            case 'on':     view[...] = True
            case 'toggle': np.logical_not(view, view)

    return lights.sum()

def part2():
    lights = np.zeros((N,N), np.int32)

    for cmd, x1, y1, x2, y2 in input:
        view = lights[x1:x2+1, y1:y2+1]
        match cmd:
            case 'off':    view[...] = np.where(view > 0, view - 1, 0)
            case 'on':     view += 1
            case 'toggle': view += 2

    return lights.sum()

# ---------------------------------------------------------------------------------------------

assert part1() == 543903
assert part2() == 14687245
