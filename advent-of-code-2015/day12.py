from advent import parse, ints, json

input = parse(12)[0]

def evaluate(obj):
    if isinstance(obj, dict):
        return 0 if 'red' in obj.values() else sum(evaluate(x) for x in obj.values())
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
