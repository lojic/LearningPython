val = lambda a: ((((a % 8) ^ 1) ^ 4) ^ int(a / 2 ** ((a % 8) ^ 1))) % 8

def part1(a):
    def gen_digits(a):
        while a != 0:
            b = val(a)
            yield b
            a = int(a / 8)

    return ",".join([ str(d) for d in gen_digits(a) ])

def part2():
    expected = list(reversed([2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0]))

    def check(m, n, idx):
        for a in range(m, n):
            if val(a) == expected[idx]:
                if idx == 15:
                    yield a
                else:
                    yield from check(a*8, (a+1)*8, idx+1)

    return next(check(0,8,0))

# ---------------------------------------------------------------------------------------------

assert part1(65804993) == "5,1,4,0,5,1,0,2,6"
assert part2()         == 202322936867370
