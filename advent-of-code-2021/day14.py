# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day14/day14.rkt
from advent import *

class State:
    def __init__(self, rules, letters, pairs):
        self.rules   = rules
        self.letters = letters
        self.pairs   = pairs

def solve(state, iterations):
    result  = iterate(step, state, iterations)
    letters = result.letters.values()
    return max(letters) - min(letters)

def step(state):
    rules       = state.rules
    src_pairs   = state.pairs
    dst_letters = dict(state.letters)
    dst_pairs   = defaultdict(lambda: 0, src_pairs)

    for pair in src_pairs.keys():
        letter         = rules[pair]
        pair_count     = src_pairs[pair]
        left           = pair[0] + letter
        right          = letter + pair[1]

        dst_letters[letter] += pair_count # Add letter
        dst_pairs[pair]     -= pair_count # Consume pair
        dst_pairs[left]     += pair_count # Produce left child
        dst_pairs[right]    += pair_count # Produce right child

    return State(rules, dst_letters, dst_pairs)

def parse_state():
    input    = parse(14, words)
    template = input[0][0]
    rules    = dict(input[2:])
    letters  = { l:len(list(g)) for (l,g) in groupby(sorted(list(template))) }
    pairs    = { template[i:i+2]:1 for i in range(len(template)-1) }

    return State(rules, letters, pairs)

# Tests ---------------------------------------------------------------------------------------

class TestDay14(unittest.TestCase):
    def test_solve(self):
        state = parse_state()
        self.assertEqual(solve(state, 10), 2_549)
        self.assertEqual(solve(state, 40), 2_516_901_104_210)

unittest.main()
