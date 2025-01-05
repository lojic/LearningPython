from advent import parse, ints, json

input = parse(12)[0]

def evaluate(obj):
    if isinstance(obj, dict):
        vals = obj.values()

        if 'red' in vals:
            return 0
        else:
            return sum(evaluate(x) for x in vals)
    elif isinstance(obj, list):
        return sum(evaluate(x) for x in obj)
    elif isinstance(obj, int):
        return obj
    else:
        return 0

part1 = lambda: sum(ints(input))

def part2():
    return evaluate(json.loads(input))

# ---------------------------------------------------------------------------------------------

assert part1() == 111754
assert part2() == 65402
