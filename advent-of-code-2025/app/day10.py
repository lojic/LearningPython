"""Advent of Code 2025: Day 10 - Factory"""

from advent import parse, heappop, heappush, decimal_to_bool_list

Machine = tuple[int, list[int], list[int]]


def parse_machine(line) -> Machine:
    def parse_diagram(s):
        return int(''.join(['0' if s == '.' else '1' for s in list(reversed(s[1:-1]))]), 2)

    def parse_buttons(buttons):
        return [sum([2 ** int(s) for s in button[1:-1].split(',')]) for button in buttons]

    def parse_joltage(joltage):
        return [int(s) for s in joltage[1:-1].split(',')]

    items = line.split()

    return (
        parse_diagram(items[0]),
        parse_buttons([s for s in items if s[0] == '(']),
        parse_joltage([s for s in items if s[0] == '{'][0]),
    )


machines: list[Machine] = parse(10, parse_machine)


def part1(m: Machine) -> int:
    (diagram, buttons, _) = m
    h = []

    for button in buttons:
        heappush(h, (1, button, button))

    while True:
        (presses, button, lights) = heappop(h)

        if lights == diagram:
            return presses

        for btn in buttons:
            heappush(h, (presses + 1, btn, lights ^ btn))


def part2(m: Machine) -> int:
    """This implementation produces the correct answer quickly for the sample input, but
    is too slow for the real input. I need to switch to a linear programming solution."""

    def step_joltages(counters, btn) -> list[int]:
        counters = counters[:]  # clone
        for i, d in enumerate(reversed(decimal_to_bool_list(btn))):
            counters[i] += d
        return counters

    (_, buttons, joltages) = m
    n = len(joltages)
    h = []

    for btn in buttons:
        heappush(h, (1, step_joltages([0] * n, btn)))

    seen = set()

    while True:
        (presses, counters) = heappop(h)
        key = tuple(counters)

        if key in seen:
            continue
        else:
            seen.add(key)

        if any(counters[i] > joltages[i] for i in range(n)):
            continue
        elif joltages == counters:
            return presses

        for btn in buttons:
            heappush(h, (presses + 1, step_joltages(counters, btn)))


def solve(part):
    return sum(part(m) for m in machines)


assert solve(part1) == 475
# print(solve(part2))
