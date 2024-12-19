# This version uses an idea from TheZigerionScammer on reddit that
# speeds things up tremendously. My version was taking 8 seconds, and
# this version takes about 35 ms!
from advent import parse, words, cache, timeit

pat_set, designs = parse(19, lambda s: set(words(s)), sep='\n\n')
max_pat_len      = max([len(pat) for pat in pat_set])

@cache
def check_design(design):
    total = 1 if design in pat_set else 0

    for y in range(1, min(max_pat_len, len(design)) + 1):
        if design[0:y] in pat_set:
            total += check_design(design[y:])

    return total

counts = [ cnt for design in designs if (cnt := check_design(design)) > 0 ]

assert len(counts) == 353             # Part 1
assert sum(counts) == 880877787214477 # Part 2
