from functools import reduce
from collections import defaultdict
from pprint import pprint
import sys
import copy


# [(position 1, range 1, forward 1), None, ..., (position n, range n, forward n)]

def parse(rows):
    return [list(map(int, row.split(': '))) for row in rows]

def initial_state(scanners):
    firewall_depth = scanners[-1][0] + 1
    state = [None]*firewall_depth
    for scanner in scanners:
        state[scanner[0]] = [0, scanner[1], True]
    return state

def simulate(scanners, delay):
    severity = 0
    state = initial_state(scanners)

    for i in range(delay):
        move_scanners(state)

    for i in range(len(state)):
        if state[i] is not None and state[i][0] == 0:
           return True
        move_scanners(state)
    return False

#def find_delay(scanners):
#    severity = 0
#    firewall_depth = scanners[-1][0] + 1
#    state = [None]*firewall_depth
#    for scanner in scanners:
#        state[scanner[0]] = [0, scanner[1], True]
#
#    caught_list = []
#    i = 0
#
#    while True:
#
#        caught_list.append(False)
#        if len(caught_list) > firewall_depth:
#            delay_to_check = i-firewall_depth
#            if not caught_list[delay_to_check]:
#                return delay_to_check
#        for delay in range(max(0, i - firewall_depth + 1), min(i + 1, firewall_depth)):
#            if state[i - delay] is not None and state[i - delay][0] == 0:
#                caught_list[delay] = True
#        move_scanners(state)
#        i += 1
#    #return severities
def find_delay(scanners):
    scanner_states = []
    state = initial_state(scanners)

    delay = 0
    while True:
        scanner_states.append([scanner[0] if scanner is not None else None for scanner in state])
        while len(scanner_states) > len(state):
            scanner_states.pop(0)
            delay += 1
        if len(scanner_states) == len(state) and all(scanner_states[pos][pos] != 0 for pos in range(len(state))):
            return delay
        move_scanners(state)

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


assert find_delay([(0, 3), (1, 2), (4, 4), (6, 4)]) == 10


with open('input', 'r') as fp:
    scanners = parse(line.strip() for line in fp)
    print('running on input')
    print(find_delay(scanners))
