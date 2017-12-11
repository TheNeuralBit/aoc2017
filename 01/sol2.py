import sys

def count_doubles(string):
    integers = [int(c) for c in string]
    length = len(integers)
    lookahead = len(integers)/2
    s = 0
    for i, val in enumerate(integers):
        print("%s == %s?" % (integers[i], integers[(i+lookahead)%length]))
        if integers[i] == integers[(i+lookahead)%length]:
            s += integers[i]
    return s

assert count_doubles('1212') == 6
assert count_doubles('1221') == 0
assert count_doubles('123425') == 4
assert count_doubles('123123') == 12
assert count_doubles('12131415') == 4

with open("input", "r") as fp:
    print(count_doubles(fp.readline().strip()))
