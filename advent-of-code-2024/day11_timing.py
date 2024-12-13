from advent import parse, ints, cache, timeit, defaultdict, lru_cache

input = parse(11, ints)[0]

# ---------------------------------------------------------------------------------------------
# Original solution

@cache
def blink(stone, blinks):
    if blinks == 0:
        return 1
    elif stone == 0:
        return blink(1, blinks - 1)
    else:
        s    = str(stone)
        l, r = divmod(len(s), 2)
        if r == 0:
            return blink(int(s[:l]), blinks - 1) + blink(int(s[l:]), blinks - 1)
        else:
            return blink(stone * 2024, blinks - 1)

def solve(blinks):
    return sum(blink(stone, blinks) for stone in input)

# ---------------------------------------------------------------------------------------------
# Port of Danny's solution

def solve2(blinks):
    stones = { stone : 1 for stone in input }

    for _ in range(blinks):
        new_stones = defaultdict(lambda: 0)

        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            else:
                s    = str(stone)
                l, r = divmod(len(s), 2)
                if r == 0:
                    new_stones[int(s[:l])] += count
                    new_stones[int(s[l:])] += count
                else:
                    new_stones[stone * 2024] += count

        stones = new_stones

    return sum(stones.values())

# ---------------------------------------------------------------------------------------------

print(timeit.timeit('solve(75)', globals=globals(), number=1))
print(timeit.timeit('solve2(75)', globals=globals(), number=1))
