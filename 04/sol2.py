from collections import defaultdict

def word_to_dict(word):
    rtrn = defaultdict(lambda: 0)
    for ch in word: rtrn[ch] += 1
    return rtrn

def valid_password(password):
    words = password.split(' ')
    dicts = [word_to_dict(word) for word in words]
    for i, item in enumerate(dicts[:-1]):
        for other in dicts[i+1:]:
            if item == other: return False
    return True

def count_valid_passwords(passwords):
    return sum(valid_password(item) for item in passwords)

import pdb
pdb.set_trace()
assert valid_password('abcde fghij') == True
assert valid_password('abcde xyz ecdab') == False
assert valid_password('a ab abc abd abf abj') == True
assert count_valid_passwords(['abcde fghij', 'abcde xyz ecdab', 'a ab abc abd abf abj']) == 2

with open('input', 'r') as fp:
    rows = (line.strip('\n') for line in fp.readlines())
    print(count_valid_passwords(rows))
