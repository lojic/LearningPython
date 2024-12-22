from advent import parse, nx, cross_product, cache, re

# Parse and preprocess graphs -----------------------------------------------------------------
codes = parse(21, list)

ng = nx.DiGraph()
ng.add_edges_from([ (s, d, { 'btn' : c }) for (s, d, c) in [ ('7', '8', '>'), ('7', '4', 'v'),
    ('8', '9', '>'), ('8', '5', 'v'), ('8', '7', '<'), ('9', '6', 'v'), ('9', '8', '<'), ('4', '5', '>'), ('4', '1', 'v'),
    ('4', '7', '^'), ('5', '6', '>'), ('5', '2', 'v'), ('5', '4', '<'), ('5', '8', '^'), ('6', '3', 'v'), ('6', '5', '<'),
    ('6', '9', '^'), ('1', '2', '>'), ('1', '4', '^'), ('2', '3', '>'), ('2', '0', 'v'), ('2', '1', '<'), ('2', '5', '^'),
    ('3', 'A', 'v'), ('3', '2', '<'), ('3', '6', '^'), ('0', 'A', '>'), ('0', '2', '^'), ('A', '0', '<'), ('A', '3', '^') ] ])
numeric_shortest_paths = dict(nx.all_pairs_all_shortest_paths(ng))

dg = nx.DiGraph()
dg.add_edges_from([ (s, d, { 'btn' : c }) for (s, d, c) in [ ('^', 'A', '>'), ('^', 'v', 'v'), ('A', '>', 'v'), ('A', '^', '<'),
    ('<', 'v', '>'), ('v', '>', '>'), ('v', '<', '<'), ('v', '^', '^'), ('>', 'v', '<'), ('>', 'A', '^') ]])
directional_shortest_paths = dict(nx.all_pairs_all_shortest_paths(dg))
# ---------------------------------------------------------------------------------------------

def compile_code(g, shortest, code):
    translate   = lambda g, p: [ g.edges[src, dst]['btn'] for src, dst in zip(p, p[1:]) ] + [ 'A' ]
    multi_paths = [ shortest[src][dst] for src, dst in zip(['A']+code, code) ]
    buttons     = [ [translate(g, path) for path in multi_path] for multi_path in multi_paths ]

    return [ [ x for xs in cp for x in xs ] for cp in cross_product(*buttons) ]

@cache
def get_shortest(n, s):
    if n == 0:
        return len(s)
    else:
        return min(sum(get_shortest(n-1, phrase)
                   for phrase in re.findall(r"[>v<^]*?A", "".join(code)))
                   for code in compile_code(dg, directional_shortest_paths, list(s)))

def solve(n):
    numeric_value     = lambda code: int("".join(code[0:3]))
    shortest_sequence = lambda code: min(get_shortest(n, "".join(compiled))
                                         for compiled in compile_code(ng, numeric_shortest_paths, code))
    complexity        = lambda code: numeric_value(code) * shortest_sequence(code)

    return sum(complexity(code) for code in codes)

# ---------------------------------------------------------------------------------------------

assert solve(2)  == 152942
assert solve(25) == 189235298434780
