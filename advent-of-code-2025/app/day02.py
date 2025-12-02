from advent import parse, positive_ints, Callable

input = parse(2, positive_ints, sep=',')

part1 = lambda s: s[: len(s) // 2] * 2 == s


def part2(s: str) -> bool:
    length = len(s)

    for i in range(1, (length // 2) + 1):
        quotient, remainder = divmod(length, i)

        if remainder == 0 and s[:i] * quotient == s:
            return True

    return False


def solve(invalid: Callable[[str], bool]):
    return sum(sum(n for n in range(left, right + 1) if invalid(str(n))) for left, right in input)


assert solve(part1) == 23560874270
assert solve(part2) == 44143124633
