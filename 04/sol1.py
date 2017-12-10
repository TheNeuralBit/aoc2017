def valid_password(password):
    words = password.split(' ')
    return len(set(words)) == len(words)

def count_valid_passwords(passwords):
    return sum(valid_password(item) for item in passwords)

assert count_valid_passwords(['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa']) == 2

with open('input', 'r') as fp:
    rows = (line.strip('\n') for line in fp.readlines())
    print(count_valid_passwords(rows))
