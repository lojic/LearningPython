def run(a):
    idx, pc, b, c = 0, 0, 0, 0
    output = []

    while a != 0:
        b = a % 8
        b ^= 1
        c = int(a / 2 ** b)
        b ^= 4
        a = int(a / 8)
        b ^= c
        v = b % 8
        output.append(v)

    return output

assert run(65804993) == [5,1,4,0,5,1,0,2,6] # Part 1
