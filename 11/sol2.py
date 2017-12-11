def cube_distance(x, y):
    return sum(abs(xi - yi) for xi, yi in zip(x, y))/2

unit_vecs = {
    'n' : ( 0,  1, -1),
    'ne': ( 1,  0, -1),
    'se': ( 1, -1,  0),
    's' : ( 0, -1,  1),
    'sw': (-1,  0,  1),
    'nw': (-1,  1,  0),
}

def walk(steps):
    pos = (0,0,0)
    max_dist = 0
    for step in steps:
        pos = [sum(x) for x in zip(pos, unit_vecs[step])]
        this_dist = cube_distance(pos, (0,0,0))
        if this_dist > max_dist: max_dist = this_dist
    return pos, max_dist


with open('input', 'r') as fp:
    steps = fp.readline().strip().split(',')
    print(walk(steps)[1])
