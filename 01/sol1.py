import sys

with open("input", "r") as fp:
    integers = [int(c) for c in fp.readline().strip()]
    i = len(integers) - 1
    s = 0
    while i >= 0:
        if integers[i] == integers[i-1]:
            s += integers[i]
        i -= 1

    print(s)
