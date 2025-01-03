from advent import parse, re

input = parse(5)

def part1(s):
    num_vowels  = len(re.findall(r'[aeiou]', s))
    num_repeats = len(re.findall(r'(.)\1', s))
    no_excluded = not re.search(r'(ab|cd|pq|xy)', s)

    return num_vowels >= 3 and num_repeats > 0 and no_excluded

def part2(s):
    non_overlapping_pair_of_2 = re.search(r'(..).*?\1', s)
    duplicate_wrapping_one    = re.search(r'(.).\1', s)

    return non_overlapping_pair_of_2 and duplicate_wrapping_one

def solve(part):
    return sum(1 for s in input if part(s))

# ---------------------------------------------------------------------------------------------

assert solve(part1) == 258
assert solve(part2) == 53
