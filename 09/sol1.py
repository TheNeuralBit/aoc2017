import re
regex = re.compile("^(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]{1,2}) (-?\d+)$")

from collections import defaultdict

def parse_garbage(stream):
    group = 0
    in_garbage = False
    canceled = False
    score = 0
    count = 0
    for ch in stream:
        if canceled:
            canceled = False
        elif in_garbage:
            if ch == ">":
                in_garbage = False
            elif ch == "!":
                canceled = True
            else:
                count += 1
        elif ch == "<":
            in_garbage = True
        elif ch == "{":
            group += 1
        elif ch == "}":
            score += group
            group -= 1


    if group != 0:
        print("group = {} != 0".format(group))

    return score, count

with open('input', 'r') as fp:
    stream = fp.readline().strip()
    print(parse_garbage(stream))
