"""Advent of Code 2025: Day 10 - Factory Part 2 (using help from reddit)"""

from advent import parse
from scipy.optimize import linprog

Machine = tuple[list[list[int]], list[int]]


def parse_machine(line) -> Machine:
    def parse_buttons(buttons):
        return [[int(s) for s in button[1:-1].split(',')] for button in buttons]

    def parse_joltage(joltage):
        return [int(s) for s in joltage[1:-1].split(',')]

    items = line.split()

    return (parse_buttons(items[1:-1]), parse_joltage(items[-1]))


machines: list[Machine] = parse(10, parse_machine)  # type: ignore


def minimize(buttons, joltage) -> float:
    c = [1 for _ in buttons]
    A = [[1 if i in b else 0 for b in buttons] for i in range(len(joltage))]
    return linprog(c, A_eq=A, b_eq=joltage, integrality=1).fun


def part2():
    return int(sum(minimize(buttons, joltage) for buttons, joltage in machines))


assert part2() == 18273
