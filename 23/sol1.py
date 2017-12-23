from collections import defaultdict

def parse(line):
    return line.split(' ')

def do_instructions(instructions):
    reg = defaultdict(lambda: 0)
    count = 0

    def resolve(reg_or_num):
        try:
            return int(reg_or_num)
        except ValueError:
            return reg[reg_or_num];

    pc = 0
    count = 0
    while pc < len(instructions):
        inst = instructions[pc]
        if inst[0] == 'set':
            reg[inst[1]] = resolve(inst[2])
        elif inst[0] == 'sub':
            reg[inst[1]] -= resolve(inst[2])
        elif inst[0] == 'mul':
            count += 1
            reg[inst[1]] *= resolve(inst[2])
        elif inst[0] == 'mod':
            reg[inst[1]] %= resolve(inst[2])
        elif inst[0] == 'jnz':
            if resolve(inst[1]) != 0:
                pc += int(inst[2])
                continue # skip the pc increment
        pc += 1
    return count

with open('input', 'r') as fp:
    print(do_instructions([parse(line.strip()) for line in fp]))
