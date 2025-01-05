from advent import parse, ints, json

input = parse(12)[0]

def evaluate(obj):
    match obj:
        case int(obj):  return obj
        case list(obj): return sum(evaluate(x) for x in obj)
        case dict(obj): return 0 if 'red' in obj.values() else sum(evaluate(x) for x in obj.values())
        case _:         return 0

assert sum(ints(input))            == 111754 # Part 1
assert evaluate(json.loads(input)) == 65402  # Part 2
