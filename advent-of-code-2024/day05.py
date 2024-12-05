from advent import parse, ints, mapt, defaultdict, cmp_to_key

rules, updates = parse(5, lambda s: mapt(ints, str.split(s)), sep='\n\n')
order_dict     = defaultdict(set)
for p1, p2 in rules: order_dict[p1].add(p2)

is_ordered     = lambda t: list(t) == sort_pages(t)
middle         = lambda t: t[len(t) // 2]
sort_pages     = lambda t: sorted(t, key=cmp_to_key(lambda a, b: -1 if b in order_dict[a] else 1))
fix_updates    = lambda u: [ sort_pages(t) for t in u if not is_ordered(t) ]

assert sum(middle(t) for t in updates if is_ordered(t)) == 6949 # Part 1

assert sum(middle(t) for t in fix_updates(updates)) == 4145 # Part 2
