def parse(rows):
    return [list(map(int, row.split(': '))) for row in rows]

def find_delay(scanners):
    delay = 0
    constants = [(scanner[0], 2*(scanner[1]-1)) for scanner in scanners]

    while True:
        caught = False
        for constant in constants:
            if (delay + constant[0]) % constant[1] == 0:
                caught = True
                break

        if not caught: return delay
        else: delay += 1

assert find_delay([(0, 3), (1, 2), (4, 4), (6, 4)]) == 10

with open('input', 'r') as fp:
    scanners = parse(line.strip() for line in fp)
    print(find_delay(scanners))
