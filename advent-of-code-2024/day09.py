from advent import parse, digits

input = parse(9, digits)[0] + (0,)

def get_disk():
    disk = []
    i    = 0

    for f, s in zip(input[::2], input[1::2]):
        disk.append([ s, [ i for n in range(f) ] ])
        i += 1

    return disk

def checksum(disk):
    total = 0
    pos   = 0

    for s, *lsts in disk:
        for lst in lsts:
            for i in lst:
                total += pos * i
                pos += 1

        pos += s

    return total

def solve(compact):
    return checksum(compact(get_disk()))

def part1(disk):
    beg = 0
    end = len(disk) - 1

    while beg < end:
        dst_len = disk[beg][0]
        src_len = len(disk[end][1])

        if dst_len == 0 or src_len == 0:
            if dst_len == 0:
                beg += 1
            if src_len == 0:
                end -= 1
        else:
            for i in range(min(dst_len, src_len)):
                disk[beg][0] -= 1
                disk[end][0] += 1
                disk[beg][1].append(disk[end][1].pop())

    return disk

def part2(disk):
    def first_available(disk, start, end, size):
        for i in range(start, end):
            s, *_ = disk[i]
            if s >= size:
                return i

    def attempt_move(disk, beg, end, src_len):
        idx = first_available(disk, beg, end, src_len)

        if idx is not None:
            lst = disk[end][1:]

            if len(lst) > 1:
                disk[end-1][0] += src_len
            else:
                disk[end][0] += src_len

            disk[idx][0] -= src_len
            disk[idx].append(disk[end][1])
            disk[end][1] = []

    beg = 0
    end = len(disk) - 1

    while beg < end:
        dst_len = disk[beg][0]
        src_len = len(disk[end][1])

        if dst_len == 0:
            beg += 1
        else:
            attempt_move(disk, beg, end, src_len)
            end -= 1

    return disk

# ---------------------------------------------------------------------------------------------

assert solve(part1) == 6390180901651
assert solve(part2) == 6412390114238
