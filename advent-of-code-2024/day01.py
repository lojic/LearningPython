from advent import ints, parse, Counter

left, right = zip(*parse(1, ints))

# Part 1
assert sum([ abs(x[0] - x[1]) for x in zip(sorted(left), sorted(right)) ]) == 1189304

# Part 2
c = Counter(right)
assert sum([ n * c[n] for n in left ]) == 24349736
