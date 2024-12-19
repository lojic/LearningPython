# This version uses an idea from TheZigerionScammer on reddit that
# speeds things up tremendously. My version was taking 8 seconds, and
# this version takes about 35 ms!
from advent import parse, words, cache, timeit

towels, designs = parse(19, lambda s: set(words(s)), sep='\n\n')
max_len         = max(len(pat) for pat in towels)

@cache
def check_design(design):
    arrangements = 1 if design in towels else 0

    for prefix_len in range(1, min(max_len, len(design)) + 1):
        if design[0:prefix_len] in towels:
            arrangements += check_design(design[prefix_len:])

    return arrangements

counts = [ cnt for design in designs if (cnt := check_design(design)) > 0 ]

assert len(counts) == 353             # Part 1
assert sum(counts) == 880877787214477 # Part 2
