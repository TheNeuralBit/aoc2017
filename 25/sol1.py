from pprint import pprint
from functools import reduce
from collections import defaultdict

def run(N):
    state = 'A'
    ones = set()
    pos = 0
    for i in range(N):
        if state == 'A':
            if pos not in ones:
                ones.add(pos)
                pos += 1
                state = 'B'
            else:
                ones.remove(pos)
                pos -= 1
                state = 'F'
        elif state == 'B':
            if pos not in ones:
                #ones.remove(pos)
                pos += 1
                state = 'C'
            else:
                ones.remove(pos)
                pos += 1
                state = 'D'
        elif state == 'C':
            if pos not in ones:
                ones.add(pos)
                pos -= 1
                state = 'D'
            else:
                ones.add(pos)
                pos += 1
                state = 'E'
        elif state == 'D':
            if pos not in ones:
                #ones.remove(pos)
                pos -= 1
                state = 'E'
            else:
                ones.remove(pos)
                pos -= 1
                state = 'D'
        elif state == 'E':
            if pos not in ones:
                #ones.remove(pos)
                pos += 1
                state = 'A'
            else:
                ones.add(pos)
                pos += 1
                state = 'C'
        elif state == 'F':
            if pos not in ones:
                ones.add(pos)
                pos -= 1
                state = 'A'
            else:
                ones.add(pos)
                pos += 1
                state = 'A'
    return ones

with open('input', 'r') as fp:
    print(len(run(12794428)))
