import re
import pandas as pd

letters = { '2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl',
            '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz' }

def phone_matches_last_name(phone, name):
    phone     = re.sub(r'\D', '', phone)
    last_name = str.split(name)[-1].lower()

    if len(last_name) < len(phone):
        return False

    for d, c in zip(phone, last_name):
        if c not in letters.get(d, ''):
            return False

    return True

def solve():
    customers = pd.read_csv('noahs-customers.csv')
    predicate = lambda row: phone_matches_last_name(row['phone'], row['name'])

    return customers[customers.apply(predicate, axis=1)].iloc[0]['phone']

# ---------------------------------------------------------------------------------------------

assert solve() == '826-636-2286'
