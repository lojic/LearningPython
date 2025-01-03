from advent import parse, groupby, iterate

input = '1113122113'

def look_and_say(s):
    for key, group in groupby(s):
        yield len(list(group))
        yield int(key)

def solve(n):
    return len(iterate(lambda s: list(look_and_say(s)), input, n))

# ---------------------------------------------------------------------------------------------

assert solve(40) == 360154
assert solve(50) == 5103798
