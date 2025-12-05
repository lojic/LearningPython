from advent import parse, positive_ints
import portion as P


def part2():
    return sum(
        interval.upper - interval.lower + 1
        for interval in P.from_data(
            [(True, *positive_ints(r), True) for r in parse(5, str.split, sep='\n\n')[0]]
        )
    )


assert part2() == 361615643045059
