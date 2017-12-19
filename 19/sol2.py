def neighbors4(p):
    return [                  (p[0]  , p[1]-1),                   \
            (p[0]-1, p[1]  ),                   (p[0]+1, p[1]  ), \
                              (p[0]  , p[1]+1)                  ]

def parse(line):
    return list(line)

def follow(maze):
    step = (0, 1)
    p = (maze[0].index('|'), 0)
    rtrn = 0
    while True:
        p = [a + b for a, b in zip(p, step)]
        # note that this counts one step past the end, but we also don't count
        # the first step, so it works out
        rtrn += 1
        val = maze[p[1]][p[0]]
        if val == '+':
            ns = [n for n in neighbors4(p) if maze[n[1]][n[0]] in '-|' and [a + b for a, b in zip(n, step)] != p]
            if not len(ns): return rtrn
            else: step = [a - b for a, b in zip(ns[0], p)]
        elif val == ' ':
            return rtrn

with open('input', 'r') as fp:
    print(follow([parse(line.strip('\n')) for line in fp]))
