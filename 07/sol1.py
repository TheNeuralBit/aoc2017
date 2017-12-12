import re
from functools import reduce

reg = re.compile("^(\w+) \((\d+)\)(?: \-\> (.*))?$")
def parse(row):
    match = reg.match(row)
    if match:
        name, weight, children = match.groups()
        return name, int(weight), children.split(", ") if children else []
    else:
        return None

import pdb

#assert reallocate(array('I', [0, 2, 7, 0])) == 5
def add_program(accum, program):
    name, weight, children = program

    parents = accum["reverse"].pop(name, [])

    parent = accum["root"]
    # walk through the tree to find this node's parent
    for parent_name in parents:
        parent = parent["children"][parent_name]


    parents.append(name)
    found_children = {}
    for child in children:
        found = accum["root"]["children"].pop(child, None)
        if found:
            found_children[child] = found
            for key, lookup in accum["reverse"].items():
                try:
                    idx = lookup.index(child)
                    #pdb.set_trace()
                    for other_parent in reversed(parents):
                        lookup.insert(idx, other_parent)
                except ValueError: continue


            #for other_child in found["children"]:
            #    pdb.set_trace()
            #    accum["reverse"][other_child] = parents + [child]
        else:
            # add this node's children to the reverse lookup
            accum["reverse"][child] = parents[:]

    try:
        parent["children"][name] = {"weight": weight, "children": found_children}
    except TypeError:
        pdb.set_trace()

    return accum

def check_weight(name, program):
    weights = [check_weight(name, child) for name, child in program["children"].items()]
    if not all(weight == weights[0] for weight in weights[1:]):
        print("{} is imbalanced!".format(name))
        for child, weight in zip(program["children"], weights):
            print("{}: {}".format(child, weight))

    return program["weight"] + sum(weights)




with open('input', 'r') as fp:
    rows = (line.strip() for line in fp)
    result = reduce(add_program, (parse(row) for row in rows), {"root": {"children": {}}, "reverse": {}})
    print(result["root"]["children"].keys())

    check_weight("root", result["root"])
