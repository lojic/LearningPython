from advent import parse, re

input: str = "".join(parse(3))

def solve(ignore_commands=False) -> int:
    enabled: bool = True
    sum: int      = 0

    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)", input):
        if match.group() == "do()":
            enabled = True
        elif match.group() == "don't()":
            enabled = False
        elif enabled or ignore_commands:
            sum += (int(match.group(1)) * int(match.group(2)))

    return sum

# ---------------------------------------------------------------------------------------------

assert solve(True) == 174960292
assert solve()     == 56275602
