from collections import defaultdict

def parse(line):
    return line.split(' ')


def do_instructions(instructions):
    reg = defaultdict(lambda: 0)

    def resolve(reg_or_num):
        try:
            return int(reg_or_num)
        except ValueError:
            return reg[reg_or_num];
    pc = 0
    last_sound = None
    while pc < len(instructions):
        inst = instructions[pc]
        if inst[0] == 'snd':
            last_sound = resolve(inst[1])
        elif inst[0] == 'set':
            reg[inst[1]] = resolve(inst[2])
        elif inst[0] == 'add':
            reg[inst[1]] += resolve(inst[2])
        elif inst[0] == 'mul':
            reg[inst[1]] *= resolve(inst[2])
        elif inst[0] == 'mod':
            reg[inst[1]] %= resolve(inst[2])
        elif inst[0] == 'rcv' and last_sound is not 0 and last_sound is not None:
            reg[inst[1]] = last_sound
            print("Recovered {}".format(last_sound))
        elif inst[0] == 'jgz':
            if resolve(inst[1]) > 0:
                pc += int(inst[2])
                continue # skip the pc increment
        pc += 1

with open('input', 'r') as fp:
    do_instructions([parse(line.strip()) for line in fp])
