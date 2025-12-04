from advent import parse, digits

input: tuple[tuple[int, ...]] = parse(3, digits)


def bank_joltage(bank: tuple[int, ...], num_batteries: int) -> int:
    joltage = 0

    for n in range(num_batteries, 0, -1):
        digit = max(bank[: len(bank) - (n - 1)])
        joltage = (joltage * 10) + digit
        bank = bank[bank.index(digit) + 1 :]

    return joltage


def solve(num_batteries: int) -> int:
    return sum(bank_joltage(bank, num_batteries) for bank in input)


assert solve(2) == 17087
assert solve(12) == 169019504359949
