import re
regex = re.compile("^(\w+) (inc|dec) (-?\d+) if (\w+) ([<>=!]{1,2}) (-?\d+)$")

from collections import defaultdict

def parse(row):
    match = regex.match(row)
    if match:
        return match.groups()
    else:
        return None

def do_instructions(l):
    registers = defaultdict(lambda: 0)
    rtrn = 0
    for inst in l:
        reg, op, val, cond_reg, cond_op, cond_val = inst
        val = int(val)
        if eval("%s %s %s" % (registers[cond_reg], cond_op, cond_val)):
            registers[reg] = registers[reg] + (val if op == "inc" else -val)
        m = max(registers.values())
        if m > rtrn: rtrn = m
    return rtrn


with open('input', 'r') as fp:
    rows = (line.strip() for line in fp.readlines())
    registers = do_instructions(parse(row) for row in rows)
    print(registers)
