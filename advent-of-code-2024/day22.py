from advent import parse, iterate, Counter
from operator import add

input = parse(22, int)

def evolve(n):
    n =    (n * 64 ^ n)   % 16777216
    n =    (n // 32 ^ n)  % 16777216
    return (n * 2048 ^ n) % 16777216

def get_changes(n):
    prev_digit = n % 10
    changes    = []

    for _ in range(2000):
        n = evolve(n)
        digit = n % 10
        changes.append((digit, digit - prev_digit))
        prev_digit = digit

    return changes

def count_sequences(n):
    changes = get_changes(n)
    d       = {}

    for i in range(3, len(changes)):
        t = (changes[i-3][1], changes[i-2][1], changes[i-1][1], changes[i][1])
        if not t in d:
            d[t] = changes[i][0]

    return d

def part1():
    return sum(iterate(evolve, n, 2000) for n in input)

def part2():
    bananas = Counter()

    for n in input:
        for t, v in count_sequences(n).items():
            bananas[t] += v

    return bananas.most_common(1)[0][1]

# ---------------------------------------------------------------------------------------------

assert part1() == 19927218456 # 1.6 s
assert part2() == 2189        # 5.4 s
