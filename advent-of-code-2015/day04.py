from advent import parse, hashlib, count_from

input = "ckczppom"

def solve(num_zeros):
    for i in count_from(1):
        data   = (input + str(i)).encode('ascii')
        result = hashlib.md5(data).hexdigest()

        if result[:num_zeros] == '0' * num_zeros:
            return i

# -------------------------------------------------------------------------------------

assert solve(5) == 117946
assert solve(6) == 3938038
