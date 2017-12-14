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

#def neighbors8(p):
#    return [(p[0]-1, p[1]-1), (p[0]  , p[1]-1), (p[0]+1, p[1]-1), \
#            (p[0]-1, p[1]  ),                   (p[0]+1, p[1]  ), \
#            (p[0]-1, p[1]+1), (p[0]  , p[1]+1), (p[0]+1, p[1]+1)]

def neighbors4(p):
    return [                  (p[0]  , p[1]-1),                   \
            (p[0]-1, p[1]  ),                   (p[0]+1, p[1]  ), \
                              (p[0]  , p[1]+1)                  ]

def find_regions(grid):
    for row in grid:
        for i, x in enumerate(row):
            row[i] = -1 if x else 0
    # 0 indicates unused space
    # -1 indicates used space not yet allocated to a group
    region = 1
    for y, row in enumerate(grid):
        while -1 in row:
            x = row.index(-1)
            grid[y][x] = region
            grow_from(grid, (x, y), region)
            region += 1
    return region - 1

def grow_from(grid, p, region):
    Y = len(grid)
    X = len(grid[0])
    def get_bounded_neighbors(p):
        return [n for n in neighbors4(p) if 0 <= n[0] < X and 0 <= n[1] < Y and grid[n[1]][n[0]] is -1]
    bounded_neighbors = set(get_bounded_neighbors(p))
    while len(bounded_neighbors):
        n = bounded_neighbors.pop()
        if grid[n[1]][n[0]] is -1:
            grid[n[1]][n[0]] = region
            for on in get_bounded_neighbors(n):
                bounded_neighbors.add(on)


in_str = 'xlqgujun'
grid = list(grid_from_str(in_str))

print(find_regions(grid))
