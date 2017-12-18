from collections import defaultdict

def parse(line):
    return line.split(' ')


def do_instructions(instructions, pid, inp, outp):
    reg = defaultdict(lambda: 0)
    reg['p'] = pid

    def resolve(reg_or_num):
        try:
            return int(reg_or_num)
        except ValueError:
            return reg[reg_or_num];

    pc = 0
    snd_cnt = 0
    something_happened = False
    while pc < len(instructions):
        inst = instructions[pc]
        #print("{}: {}".format(pid, inst))
        if inst[0] == 'snd':
            snd_cnt += 1
            outp.append(resolve(inst[1]))
        elif inst[0] == 'set':
            reg[inst[1]] = resolve(inst[2])
        elif inst[0] == 'add':
            reg[inst[1]] += resolve(inst[2])
        elif inst[0] == 'mul':
            reg[inst[1]] *= resolve(inst[2])
        elif inst[0] == 'mod' and resolve(inst[2]) is not 0:
            reg[inst[1]] %= resolve(inst[2])
        elif inst[0] == 'rcv':
            if len(inp):
                reg[inst[1]] = inp.pop(0)
                print("{} rcvd {}".format(pid, reg[inst[1]]))
            else:
                print("{} yielding for rcv".format(pid))
                print("Program {} sent {} values".format(pid, snd_cnt))
                yield something_happened
                something_happened = False
                continue
        elif inst[0] == 'jgz':
            if resolve(inst[1]) > 0:
                pc += resolve(inst[2])
                something_happened = True
                continue # skip the pc increment
        pc += 1
        something_happened = True
    print("Program {} sent {} values".format(pid, snd_cnt))
    yield

with open('input', 'r') as fp:
    atob = []
    btoa = []
    instructions = [parse(row.strip()) for row in fp]
    for a, b in zip(do_instructions(instructions, 0, btoa, atob), do_instructions(instructions, 1, atob, btoa)):
        if a is False and b is False:
            print("Deadlocked!")
            break
