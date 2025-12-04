"""Port of Todd Ginsberg's Kotlin solution, so I can understand it :)"""

from advent import parse, digits, reduce

banks: list[list[tuple[int, int]]] = [list(enumerate(bank)) for bank in parse(3, digits)]


def solve_part1() -> int:
    return sum(joltage(it, 2) for it in banks)


def solve_part2() -> int:
    return sum(joltage(it, 12) for it in banks)


def joltage(bank: list[tuple[int, int]], batteries: int) -> int:
    def fun(acc: tuple[int, int], offset: int) -> tuple[int, int]:
        total, left_index = acc
        sublist = bank[left_index : len(bank) - batteries + offset]
        it = max(sublist, key=lambda x: x[1])
        return ((total * 10 + it[1]), it[0] + 1)

    return reduce(fun, range(1, batteries + 1), (0, 0))[0]


assert solve_part1() == 17087
assert solve_part2() == 169019504359949

# Todd's original code:
#
# private val banks: List<List<IndexedValue<Int>>> = input.map { parseInput(it) }
#
# fun solvePart1(): Long =
#     banks.sumOf { joltage(it, 2) }
#
# fun solvePart2(): Long =
#     banks.sumOf { joltage(it, 12) }
#
# private fun joltage(bank: List<IndexedValue<Int>>, batteries: Int): Long =
#     (1 .. batteries).fold(0L to 0) { (total, leftIndex), offset ->
#         bank.subList(leftIndex, bank.size - batteries + offset)
#             .maxBy { it.value }
#             .let { (total * 10) + it.value to it.index + 1 }
#     }.first
