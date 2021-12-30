# Port of my Racket solution:
# https://github.com/lojic/LearningRacket/blob/master/advent-of-code-2021/solutions/day16/day16.rkt
from advent import *

Chunk    = namedtuple('Chunk', 'last bits')
Header   = namedtuple('Header', 'version type')
Literal  = namedtuple('Literal', 'header val')
Operator = namedtuple('Operator', 'header len_type_id packets')

# ---------------------------------------------------------------------------------------------

def solve(input, part):
    pkt, _ = parse_packet(input)
    return part(pkt)

def sum_versions(pkt):
    if type(pkt) == Literal:
        return pkt.header.version
    else:
        return pkt.header.version + sum(sum_versions(pkt) for pkt in pkt.packets)

def eval_pkt(pkt):
    op = { 0 : sum,
           1 : prod,
           2 : min,
           3 : max,
           4 : None,
           5 : lambda l: 1 if l[0]  > l[1] else 0,
           6 : lambda l: 1 if l[0]  < l[1] else 0,
           7 : lambda l: 1 if l[0] == l[1] else 0 }[pkt.header.type]

    if type(pkt) == Literal:
        return pkt.val
    else:
        return op([ eval_pkt(pkt) for pkt in pkt.packets])

# Parsers -------------------------------------------------------------------------------------

def parse_packet(bits):
    header, bits = parse_header(bits)
    parser       = parse_literal if header.type == 4 else parse_operator
    return  parser(header, bits)

def parse_header(bits):
    version, bits = parse_version(bits)
    type, bits    = parse_type_id(bits)
    return (Header(version, type), bits)

def parse_version(bits):
    return (to_number(bits[:3]), bits[3:])

def parse_type_id(bits):
    return (to_number(bits[:3]), bits[3:])

def parse_literal(header, bits):
    lst, bits = parse_chunks(bits)
    return (Literal(header, to_number(lst)), bits)

def parse_chunks(bits, result = []):
    while True:
        chunk, bits = parse_chunk(bits)
        result      = result + chunk.bits
        if chunk.last: return (result, bits)

def parse_chunk(bits):
    lst  = bits[:5]
    last = (lst[0] == 0)
    return (Chunk(last, lst[1:]), bits[5:])

def parse_operator(header, bits):
    len_type_id = bits[0]
    bits        = bits[1:]
    fun         = parse_by_len if len_type_id == 0 else parse_by_num
    pkts, bits  = fun(bits)
    return (Operator(header, len_type_id, pkts), bits)

def parse_by_len(bits):
    len, bits      = to_number(bits[:15]), bits[15:]
    sub_bits, bits = bits[:len], bits[len:]
    packets        = []

    while sub_bits:
        pkt, sub_bits = parse_packet(sub_bits)
        packets.append(pkt)

    return (packets, bits)

def parse_by_num(bits):
    num, bits = to_number(bits[:11]), bits[11:]
    packets   = []

    while num > 0:
        pkt, bits = parse_packet(bits)
        packets.append(pkt)
        num -= 1

    return (packets, bits)

# Support -------------------------------------------------------------------------------------

def to_number(bits): return bool_list_to_decimal(bits)
def to_binary(s):    return [ int(c) for c in ''.join(f'{int(x,16):04b}' for x in s) ] # from Peter Norvig

# Tests ---------------------------------------------------------------------------------------

class TestDay16(unittest.TestCase):
    def test_solve(self):
        input = to_binary(parse(16)[0])
        self.assertEqual(solve(input, sum_versions), 843)
        self.assertEqual(solve(input, eval_pkt), 5_390_807_940_351)

unittest.main()
