import re
import pandas as pd

# Identify the phone number of the customer whose last name can be
# spelled with the phone number.

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
    df = pd.read_csv('noahs-customers.csv')
    
    for name, phone in zip(df['name'], df['phone']):
        if phone_matches_last_name(phone, name):
            return phone

    return None

# ---------------------------------------------------------------------------------------------

assert solve() == '826-636-2286'
