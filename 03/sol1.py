def find_loc(num):


def distance(loc):


assert compute_checksum([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18

with open('input', 'r') as fp:
    rows = ([int(item) for item in line.strip().split('\t')] for line in fp.readlines())
    print(compute_checksum(rows))
