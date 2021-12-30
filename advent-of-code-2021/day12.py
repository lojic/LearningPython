# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day12/day12.rkt
from advent import *

neighbors = defaultdict(set)
for (c1,c2) in parse(12,words):
    neighbors[c1].add(c2)
    neighbors[c2].add(c1)

def solve(g, is_neighbor):
    return quantify(get_paths(g, is_neighbor))

def get_paths(neighbors, is_neighbor, path=["start"]):
    if path[-1] == 'end':
        yield [path]
    else:
        for cave in neighbors[path[-1]]:
            if is_neighbor(path, cave):
                # # I learned about "yield from" from Peter Norvig's solution:
                # # https://github.com/norvig/pytudes/blob/main/ipynb/Advent-2021.ipynb
                yield from get_paths(neighbors, is_neighbor, path + [cave])

def first_revisit(path):
    return not [ True for (k,g) in groupby(sorted([ cave for cave in path if is_small(cave) ])) if len(list(g)) > 1 ]

def valid_neighbor_1(path, cave):
    return is_large(cave) or cave not in path

def valid_neighbor_2(path, cave):
    return valid_neighbor_1(path, cave) or (non_terminal(cave) and first_revisit(path))

is_small     = lambda cave: (not is_large(cave)) and non_terminal(cave)
is_large     = lambda cave: cave.isupper()
non_terminal = lambda cave: cave not in ['start', 'end']

# Tests ---------------------------------------------------------------------------------------

class TestDay12(unittest.TestCase):
    def test_parts(self):
        self.assertEqual(solve(neighbors, valid_neighbor_1), 3_887)
        self.assertEqual(solve(neighbors, valid_neighbor_2), 104_834)

unittest.main()
