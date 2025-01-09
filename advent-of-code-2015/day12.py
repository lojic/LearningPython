from advent import parse, ints, json

input = parse(12)[0]

def evaluate(obj):
    match obj:
        case int(obj):  return obj
        case list(obj): return sum(evaluate(x) for x in obj)
        case dict(obj):
            vals = obj.values()
            return 0 if 'red' in vals else sum(evaluate(x) for x in vals)
        case _:         return 0

assert sum(ints(input))            == 111754 # Part 1
assert evaluate(json.loads(input)) == 65402  # Part 2
