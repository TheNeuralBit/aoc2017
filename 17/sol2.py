import sys
from numba import jit

@jit
def do_insertions(steps, N):
    rtrn = 0
    pos = 0
    length = 1
    print()
    for length in range(1, N+1):
        pos = ((pos + steps) % length) + 1
        if pos == 1: rtrn = length

    return rtrn

steps = 343
print(do_insertions(steps, 50000000))
