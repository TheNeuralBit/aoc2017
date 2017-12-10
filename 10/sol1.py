def tie_knots(l, lengths):
    idx = 0
    skip = 0
    for length in lengths:
        knot(l, length, idx)
        idx = (idx + length + skip) % len(l)
        skip += 1
    return l

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


with open('input', 'r') as fp:
    lengths = map(int, fp.readline().strip().split(','))
    l = list(range(256))
    tie_knots(l, lengths)
    print(l[0]*l[1])
