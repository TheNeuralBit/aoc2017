from itertools import islice

def generate(start, factor):
    # 2147483647 = (2^31) - 1 = 0x7FFFFFFF
    n = start
    while True:
        n = ( n * factor ) % 0x7FFFFFFF
        yield n

a_factor = 16807
b_factor = 48271

assert list(islice(generate(65, a_factor), 5)) == [1092455, 1181022009, 245556042, 1744312007, 1352636452]
assert list(islice(generate(8921, b_factor), 5)) == [430625591, 1233683848, 1431495498, 137874439, 285222916]

a_start = 699
b_start = 124

all_pairs = islice(zip(generate(a_start, a_factor), generate(b_start, b_factor)), 40000000)
print(sum((a & 0xFFFF) == (b & 0xFFFF) for a,b in all_pairs))
