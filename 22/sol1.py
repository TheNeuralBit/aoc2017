def parse(line, y):
    return ((x,y) for x, v in enumerate(line) if v == '#')

# -1 = right
# +1 = left
DIRS = [(0,1),(1,0),(0,-1),(-1,0)]

def traverse(infected, N):
    pos = (0,0)
    count = 0
    d = 2
    for i in range(N):
        if pos in infected:
            d = (d - 1) % 4
            infected.remove(pos)
        else:
            d = (d + 1) % 4
            infected.add(pos)
            count += 1

        D = DIRS[d]
        pos = (pos[0] + D[0], pos[1]+ D[1])
    return count

with open('input', 'r') as fp:
    infected = set()
    for y, line in enumerate(fp):
        for x, y in parse(line.strip('\n'), y):
            infected.add((x - 12, y - 12))
    print(traverse(infected, 10000))
