import re
REG = re.compile("p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>")

def parse(line):
    m = re.match(REG, line)
    groups = m.groups()
    p = tuple(map(int, groups[0:3]))
    v = tuple(map(int, groups[3:6]))
    a = tuple(map(int, groups[6:9]))
    return p, v, a

def add(a, b):
    return tuple(ai + bi for ai, bi in zip(a, b))

def subtract(a, b):
    return tuple(ai - bi for ai, bi in zip(a, b))

def multiply(a, b):
    return tuple(ai*b for ai in a)

def step(particle, t):
    p, v, a = particle
    # v(t) = v(0) + a(0)*t
    v = add(v, multiply(a, t))
    # x(t) = x(0) + v(0)*t + 1/2a(0)^2
    p = add(p, add(multiply(v, t), multiply((ai*ai for ai in a), 1/2)))
    return p, v, a

def distance(x, y):
    return sum(abs(i) for i in subtract(x, y))

def simulate(particles):
    idx = -1
    same_count = 0
    while True:
        last_idx = idx
        idx, p = min(enumerate(particles), key=lambda a: distance(a[1][0], (0,0,0)))
        if idx == last_idx: same_count += 1
        else: same_count = 0
        if same_count > 10:
            return idx
        particles = [step(particle, 10000) for particle in particles]

with open('input', 'r') as fp:
    print(simulate([parse(line.strip('\n')) for line in fp]))
