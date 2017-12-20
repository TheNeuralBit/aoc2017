from collections import defaultdict
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

def step(particle):
    p, v, a = particle
    v = add(v, a)
    p = add(p, v)
    return p, v, a

def distance(x, y):
    return sum(abs(i) for i in subtract(x, y))

def remove_collisions(particles):
    position_counts = defaultdict(lambda: 0)
    for p in particles:
        position_counts[p[0]] += 1

    dupes = set()
    for p, c in position_counts.items():
        if c > 1: dupes.add(p)

    if not len(dupes): return particles
    else:
        return [p for p in particles if p[0] not in dupes]

def simulate(particles):
    same_count = 0
    this_len = len(particles)
    while True:
        last_len = this_len
        particles = remove_collisions(particles)
        this_len = len(particles)
        if this_len == last_len: same_count += 1
        else: same_count = 0
        if same_count > 1000:
            return len(particles)
        particles = [step(particle) for particle in particles]

with open('input', 'r') as fp:
    print(simulate([parse(line.strip('\n')) for line in fp]))
