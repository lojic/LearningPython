from advent import parse, nx, cross_product

codes = parse(21, list)

npad = nx.DiGraph()
npad.add_edges_from([ (s, d, { 'btn' : c }) for (s, d, c) in [('7', '8', '>'), ('7', '4', 'v'),
    ('8', '9', '>'), ('8', '5', 'v'), ('8', '7', '<'), ('9', '6', 'v'), ('9', '8', '<'), ('4', '5', '>'), ('4', '1', 'v'),
    ('4', '7', '^'), ('5', '6', '>'), ('5', '2', 'v'), ('5', '4', '<'), ('5', '8', '^'), ('6', '3', 'v'), ('6', '5', '<'),
    ('6', '9', '^'), ('1', '2', '>'), ('1', '4', '^'), ('2', '3', '>'), ('2', '0', 'v'), ('2', '1', '<'), ('2', '5', '^'),
    ('3', 'A', 'v'), ('3', '2', '<'), ('3', '6', '^'), ('0', 'A', '>'), ('0', '2', '^'), ('A', '0', '<'), ('A', '3', '^')] ])
npad_shortest_paths = dict(nx.all_pairs_all_shortest_paths(npad))

dpad = nx.DiGraph()
dpad.add_edges_from([(s, d, { 'btn' : c }) for (s, d, c) in [('^', 'A', '>'), ('^', 'v', 'v'), ('A', '>', 'v'), ('A', '^', '<'),
    ('<', 'v', '>'), ('v', '>', '>'), ('v', '<', '<'), ('v', '^', '^'), ('>', 'v', '<'), ('>', 'A', '^') ]])
dpad_shortest_paths = dict(nx.all_pairs_all_shortest_paths(dpad))

def translate_path(g, path):
    return [ g.edges[src, dst]['btn'] for src, dst in zip(path, path[1:]) ] + [ 'A' ]

def compile_code(g, shortest, code):
    multi_paths = [ shortest[src][dst] for src, dst in zip(['A']+code, code) ]
    buttons     = [ [translate_path(g, path) for path in multi_path] for multi_path in multi_paths ]
    button_seqs = [ [ x for lst in cp for x in lst ] for cp in cross_product(*buttons) ]
    return button_seqs

def get_numeric(code):
    return int("".join(code[0:3]))

def part1():
    total = 0

    for code in codes:
        shortest = 1000000

        for dpad_code1 in compile_code(npad, npad_shortest_paths, code):
            dpad_codes2 = compile_code(dpad, dpad_shortest_paths, dpad_code1)
            for dpad_code2 in dpad_codes2:
                dpad_codes3 = compile_code(dpad, dpad_shortest_paths, dpad_code2)
                for dpad_code3 in dpad_codes3:
                    l = len(dpad_code3)
                    if l < shortest:
                        shortest = l

        n = get_numeric(code)
        print(f'shortest={shortest}, numeric={n}, result={n*shortest}')
        total += n * shortest

    return total

# ---------------------------------------------------------------------------------------------

assert part1() == 152942
