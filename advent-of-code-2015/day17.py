from advent import parse, combinations

containers = parse(17, int)

solve = lambda fun: fun(ways
                        for n in range(1, len(containers) + 1)
                        if (ways := sum(1 for combo in combinations(containers, n)
                                        if sum(combo) == 150)))

# ---------------------------------------------------------------------------------------------

assert solve(sum)  == 654 # Part 1
assert solve(next) == 57  # Part 2
