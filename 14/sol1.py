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

def grid_from_str(in_str):
    for row in range(128):
        bit_strs = ('{0:08b}'.format(l) for l in dense_hash('{}-{}'.format(in_str, row)))
        yield [bit == '1' for bit in ''.join(bit_strs)]

in_str = 'xlqgujun'
print(sum(sum(row) for row in grid_from_str(in_str)))
