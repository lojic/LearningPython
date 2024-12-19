from advent import parse, words, cache, timeit

pats, designs = parse(19, words, sep='\n\n')

@cache
def check_design(design, depth=1):
    if design == '':
        return 1
    else:
        return sum(check_design(design.removeprefix(pat), depth + 1) for pat in pats if design.startswith(pat))

def get_counts():    
    counts = [ cnt for design in designs if (cnt := check_design(design)) > 0 ]

# assert len(counts) == 353             # Part 1
# assert sum(counts) == 880877787214477 # Part 2

print(timeit.timeit('get_counts()', globals=globals(), number=1))
