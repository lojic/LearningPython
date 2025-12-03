from advent import parse, digits, Generator

input = parse(3, digits)


def bank_digits(batteries: list[int], num_batteries: int) -> Generator[int, None, None]:
    for n in range(num_batteries, 0, -1):
        yield (digit := max(batteries[: len(batteries) - (n - 1)]))
        batteries = batteries[batteries.index(digit) + 1 :]


def solve(num_batteries: int) -> int:
    return sum(
        int(''.join([str(digit) for digit in bank_digits(batteries, num_batteries)]))
        for batteries in input
    )


assert solve(2) == 17087
assert solve(12) == 169019504359949
