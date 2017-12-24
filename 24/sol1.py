def parse(line):
    return tuple(map(int, line.split('/')))

def strongest(needed, pipes):
    available = [i for i, p in enumerate(pipes) if needed in p]
    if len(available) == 0:
        return 0

    m = -1
    for idx in available:
        pipe = pipes[idx]
        next_needed = pipe[0] if pipe.index(needed) == 1 else pipe[1]
        result = sum(pipe) + strongest(next_needed, pipes[:idx] + pipes[idx+1:])
        if result > m: m = result

    return m

with open('input', 'r') as fp:
    pipes = [parse(line.strip()) for line in fp]
    print(strongest(0, pipes))
