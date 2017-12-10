from functools import reduce

def sparse_hash(s):
    lengths = list(map(ord, s)) + [17, 31, 73, 47, 23]
    l = list(range(256))
    idx = 0
    skip = 0
    for i in range(64):
        for length in lengths:
            knot(l, length, idx)
            idx = (idx + length + skip) % len(l)
            skip += 1
    return l

def dense_hash(s):
    l = sparse_hash(s)
    return [reduce(lambda a, b: a^b, l[i*16:(i+1)*16]) for i in range(int(len(l)/16))]

def tohex(l):
    return ''.join("%02x" % i for i in l)

def knot(l, length, idx):
    halflen = int(length/2)
    lindices  = (i % len(l) for i in range(idx, idx+halflen))
    rindices = (i % len(l) for i in range(idx+length - 1, idx+length-1-halflen, -1))

    for left, right in zip(lindices, rindices):
        tmp = l[right]
        l[right] = l[left]
        l[left]  = tmp
    return l

assert knot([0, 1, 2, 3, 4], 3, 1) == [0, 3, 2, 1, 4]
assert knot([0, 1, 2, 3, 4], 4, 3) == [4, 3, 2, 1, 0]
assert tohex(dense_hash('')) == 'a2582a3a0e66e6e86e3812dcb672a272'
assert tohex(dense_hash('AoC 2017')) == '33efeb34ea91902bb2f59c9920caa6cd'


with open('input', 'r') as fp:
    print(tohex(dense_hash(fp.readline().strip())))
