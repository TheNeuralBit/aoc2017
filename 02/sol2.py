def compute_row(row):
    for i, a in enumerate(row):
        for j, b in enumerate(row):
            if i == j: continue
            if a % b == 0: return int(a/b)
            if b % a == 0: return int(b/a)

def compute_checksum(matrix):
    return sum(compute_row(row) for row in matrix)

assert compute_row([5, 9, 2, 8]) == 4
assert compute_row([9, 4, 7, 3]) == 3
assert compute_row([3, 8, 6, 5]) == 2
assert compute_checksum([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 9

with open('input', 'r') as fp:
    rows = ([int(item) for item in line.strip().split('\t')] for line in fp)
    print(compute_checksum(rows))

