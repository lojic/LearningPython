from advent import parse, ints, cache

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
    return sum(blink(stone, blinks) for stone in parse(11, ints)[0])

# ---------------------------------------------------------------------------------------------

assert solve(25) == 183484
assert solve(75) == 218817038947400
