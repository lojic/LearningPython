from advent import re

def increment_password(lst):
    for i in range(len(lst) - 1, -1, -1):
        match lst[i]:
            case 'h': lst[i] = 'j'
            case 'k': lst[i] = 'm'
            case 'n': lst[i] = 'p'
            case 'z': lst[i] = 'a'
            case 'a'|'b'|'c'|'d'|'e'|'f'|'g'|'j'|'m'|'p'|'q'|'r'|'s'|'t'|'u'|'v'|'w'|'x'|'y':
                lst[i] = chr(ord(lst[i]) + 1)

        if lst[i] != 'a':
            return lst

def is_valid(lst):
    s            = "".join(lst)
    has_straight = re.search(r'(?=(abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz))', s)
    has_pairs    = len(set(re.findall(r'(.)\1', s))) >= 2

    return has_straight and has_pairs

def solve(password):
    lst = list(password)

    while True:
        increment_password(lst)

        if is_valid(lst):
            return "".join(lst)

# ---------------------------------------------------------------------------------------------

assert solve('vzbxkghb') == 'vzbxxyzz'
assert solve('vzbxxyzz') == 'vzcaabcc'
