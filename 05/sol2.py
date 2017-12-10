def follow_jumps(arr):
    count = 0
    position = 0
    while 0 <= position < len(arr):
        jump = arr[position]
        arr[position] +=  -1 if jump >= 3 else 1
        position += jump
        count += 1
    return count

assert follow_jumps([0, 3, 0, 1, -3]) == 10

with open('input', 'r') as fp:
    rows = (line.strip('\n') for line in fp.readlines())
    print(follow_jumps(list(map(int, rows))))
