# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day09/day09.rkt
from advent import *

cave   = parse(9, digits)
width  = len(cave[0])
height = len(cave)

def get(x, y):
    return cave[y][x] if (0 <= x < width) and (0 <= y < height) else 9

def low_points():
    points = []
    for x in range(width):
        for y in range(height):
            n = get(x, y)
            if (n < get(x,  y-1) and # North
                n < get(x+1,  y) and # East
                n < get(x,  y+1) and # South
                n < get(x-1, y)):    # West

                points.append((x, y, n))
    return points

def get_basin(t):
    def flood(x, y, prev_height):
        """Use a queue to implement flood vs. recursion"""
        result = []
        queue  = deque()
        queue.append((x,y,prev_height-1))
        while queue:
            x, y, prev_height = queue.popleft()
            h = get(x,y)
            if prev_height < h < 9:
                result.append((x,y,h))
                for (x,y) in [ (x, y-1), (x+1, y), (x, y+1), (x-1, y) ]:
                    queue.append((x, y, h))
        return result

    return set(flood(*t))

part1 = lambda: sum([ n+1 for (x,y,n) in low_points() ])

part2 = lambda: prod(sorted([ len(get_basin(t)) for t in low_points() ])[-3:])

# Tests ---------------------------------------------------------------------------------------

class TestDay09(unittest.TestCase):
    def test_parts(self):
        self.assertEqual(part1(), 566)
        self.assertEqual(part2(), 891684)

unittest.main()
