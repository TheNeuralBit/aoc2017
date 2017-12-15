from itertools import islice
from numba import jit

a_factor = 16807
b_factor = 48271

@jit
def generate(start, factor, mod):
    # 2147483647 = (2^31) - 1 = 0x7FFFFFFF
    n = start
    while True:
        n = ( n * factor ) % 0x7FFFFFFF
        if n % mod == 0: yield n

def generate_pairs(a_start, b_start, num):
    return islice(zip(generate(a_start, a_factor, 4), generate(b_start, b_factor, 8)), num)

assert list(islice(generate(65, a_factor, 1), 5)) == [1092455, 1181022009, 245556042, 1744312007, 1352636452]
assert list(islice(generate(8921, b_factor, 1), 5)) == [430625591, 1233683848, 1431495498, 137874439, 285222916]

a_start = 699
b_start = 124

print(sum((a & 0xFFFF) == (b & 0xFFFF) for a,b in generate_pairs(a_start, b_start, 5000000)))
