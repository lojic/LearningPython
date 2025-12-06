from advent import parse, atoms, operator, reduce, compose


apply = lambda op_sym, args: reduce({'+': operator.add, '*': operator.mul}[op_sym], args)
part1 = lambda: [apply(col[-1], col[:-1]) for col in zip(*parse(6, atoms))]


def part2(args=[]):
    for row in filter(
        lambda row: ''.join(row).strip(),
        zip(*parse(6, compose(reversed, list), do_rstrip=False)),
    ):
        args.append(int(''.join(row[:-1]).strip()))
        if row[-1] in ['+', '*']:
            yield apply(row[-1], args)
            args = []


assert sum(part1()) == 3525371263915
assert sum(part2()) == 6846480843636
