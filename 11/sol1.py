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
    for step in steps:
        pos = [sum(x) for x in zip(pos, unit_vecs[step])]
    return pos

def dist_after_walk(steps):
    return cube_distance(walk(steps), (0,0,0))


assert cube_distance((2, -1, -1), (0,0,0)) == 2
assert dist_after_walk(['ne','ne','ne']) == 3
assert dist_after_walk(['ne','ne','sw','sw']) == 0
assert dist_after_walk(['ne','ne','s','s']) == 2


with open('input', 'r') as fp:
    steps = fp.readline().strip().split(',')
    print(dist_after_walk(steps))
