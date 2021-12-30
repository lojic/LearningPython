# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day15/day15-conspicio.rkt
from advent import *

# Represent a path with a 3-tuple (risk x y) to more easily work with the heap

def solve(input, width):
    dim0    = 100
    dim     = width * dim0
    vec     = list(chain.from_iterable(input))
    visited = [ False ] * (dim * dim)
    paths   = [(0, 0, 0)]

    is_visited  = lambda x, y: visited[y * dim + x]
    wrap        = lambda n: (n - 9) if n > 9 else n

    def set_visited(x,y): visited[y * dim + x] = True

    def get(x, y):
        tile_x, x = divmod(x, dim0)
        tile_y, y = divmod(y, dim0)
        risk      = vec[y * dim0 + x]
        return wrap(risk + tile_x + tile_y)

    while True:
        risk, x, y = heappop(paths)
        if is_visited(x, y):
            continue
        elif (x == dim-1) and (y == dim-1):
            return risk
        else:
            set_visited(x, y)
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (0 <= nx < dim) and (0 <= ny < dim) and (not is_visited(nx, ny)):
                    heappush(paths, (risk + get(nx,ny), nx, ny))

# Tests ---------------------------------------------------------------------------------------

class TestDay15(unittest.TestCase):
    def test_solve(self):
        input = parse(15, digits)
        self.assertEqual(solve(input, 1), 687)
        self.assertEqual(solve(input, 5), 2957)

unittest.main()
