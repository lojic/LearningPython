"""Advent of Code 2025: Day 10 - Factory Part 2 (using help from reddit)"""

from scipy.optimize import linprog

b = 0
for _, *buttons, joltage in map(str.split, open('app/day10.txt')):
    buttons = [eval(b[:-1] + ',)') for b in buttons]
    joltage = eval(joltage[1:-1])
    numbers = range(len(joltage))

    c = [1 for _ in buttons]
    A = [[1 if i in b else 0 for b in buttons] for i in numbers]
    b += linprog(c, A_eq=A, b_eq=joltage, integrality=1).fun

assert b == 18273
