from advent import parse, ints, iterate, count_from

robots        = parse(14, ints, print_lines=3)
width, height = 101, 103
tick          = lambda r: [ ((x + vx) % width, (y + vy) % height, vx, vy) for x, y, vx, vy in r ]

def part1(n=100):
    bots           = iterate(tick, robots, 100)
    ul, ur, ll, lr = 0, 0, 0, 0
    xmid, ymid     = width // 2, height // 2

    for x, y, _, _ in bots:
        if x < xmid:
            if y < ymid:
                ul += 1
            elif y > ymid:
                ll += 1
        elif x > xmid:
            if y < ymid:
                ur += 1
            elif y > ymid:
                lr += 1

    return ul * ur * ll * lr

def mostly_symmetric(s, xmid):
    good, bad = 0, 0

    for x, y in s:
        if x < xmid:
            if (xmid + xmid - x, y) in s:
                good += 1
            else:
                bad += 1

    return good > bad

def print_robots(s):
    for row in range(height):
        for col in range(width):
            if (col, row) in s:
                print('x', end='')
            else:
                print('.', end='')
        print('')

def part2():
    r = robots

    for seconds in count_from(1):
        r = tick(r)
        s = { (x,y) for x, y, _, _ in r }

        for xmid in range(30, width-30):
            if mostly_symmetric(s, xmid):
                print(f'xmid={xmid}')
                print(f'{seconds} ------------------------------------------------------------------------------------------------')
                print_robots(s)
                return seconds

# ---------------------------------------------------------------------------------------------

assert part1() == 224969976
assert part2() == 7892
