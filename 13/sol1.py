from functools import reduce
from collections import defaultdict


# [(position 1, range 1, forward 1), None, ..., (position n, range n, forward n)]

def parse(rows):
    return [list(map(int, row.split(': '))) for row in rows]

def simulate(scanners):
    severity = 0
    firewall_depth = scanners[-1][0] + 1
    state = [None]*firewall_depth
    for scanner in scanners:
        state[scanner[0]] = [0, scanner[1], True]
    for i in range(firewall_depth):
        if state[i] is not None and state[i][0] == 0:
            severity += i*state[i][1]
        move_scanners(state)
    return severity

def move_scanners(state):
    for item in state:
        if item is None: continue
        if item[2]:
            item[0] += 1
            if item[0] == item[1] - 1:
                item[2] = False
        else:
            item[0] -= 1
            if item[0] == 0:
                item[2] = True




with open('input', 'r') as fp:
    scanners = parse(line.strip() for line in fp)
    print(simulate(scanners))
