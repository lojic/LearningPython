# Port of my Racket solution:
#
from advent import *

input  = parse(13, atoms, sep='\n')
points = { entry for entry in input if len(entry) == 2 }
folds  = [ (val if axis == 'x' else False, val if axis == 'y' else False)
           for (fold, along, axis, val) in [ entry for entry in input if len(entry) > 2 ]]

def solve():
    lst = points
    return [ lst := fold_points(fold, lst) for fold in folds ][-1]

def fold_points(fold, points):
    sentinel = 2 ** 32
    axis = (fold[0] or sentinel, fold[1] or sentinel)

    def non_axis(p):
        return not (axis[0] == p[0] or axis[1] == p[1])

    def fold_point(p):
        def min_point(p1, p2): return (min(p1[0], p2[0]), min(p1[1], p2[1]))

        return min_point(p, (2 * axis[0] - p[0], 2 * axis[1] - p[1]))

    return set([ fold_point(p) for p in points if non_axis(p) ])

def display_code(coords):
    for y in range(1 + max(p[1] for p in coords)):
        for x in range(1 + max(p[0] for p in coords)):
            print('#' if (x,y) in coords else ' ', end='')
        print(' ')

display_code(solve())
