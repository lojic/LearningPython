# This version uses an idea from TheZigerionScammer on reddit that
# speeds things up tremendously. My version was taking 8 seconds, and
# this version takes about 35 ms!
from advent import parse, words, cache, timeit

towels, designs = parse(19, lambda s: set(words(s)), sep='\n\n')
max_len         = max(len(pat) for pat in towels)

def prefixes_suffixes(design):
    for prefix_len in range(1, min(max_len, len(design)) + 1):
        yield design[0:prefix_len], design[prefix_len:]

@cache
def check_design(design):
    arrangements = 1 if design in towels else 0

    for prefix, suffix in prefixes_suffixes(design):
        if prefix in towels:
            arrangements += check_design(suffix)

    return arrangements

counts = [ cnt for design in designs if (cnt := check_design(design)) > 0 ]

assert len(counts) == 353             # Part 1
assert sum(counts) == 880877787214477 # Part 2
