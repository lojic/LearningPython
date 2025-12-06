from advent import parse, atoms, operator, reduce, compose


def apply(op_sym: str, args: list[int]) -> int:
    return reduce({'+': operator.add, '*': operator.mul}[op_sym], args)


def part1() -> int:
    return sum([apply(col[-1], col[:-1]) for col in zip(*parse(6, atoms))])


def part2() -> int:
    rows = filter(
        lambda row: ''.join(row).strip(),
        zip(*parse(6, compose(reversed, list), do_rstrip=False)),
    )

    def answers(rows):
        args = []

        for row in rows:
            args.append(int(''.join(row[:-1]).strip()))

            if row[-1] in ['+', '*']:
                yield apply(row[-1], args)
                args = []

    return sum(answers(rows))


assert part1() == 3525371263915
assert part2() == 6846480843636
