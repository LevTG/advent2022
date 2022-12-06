import re


re_cargo = re.compile('(\[(?P<cargo>\w)\])|(?P<empty>\s{3})\s?')
re_moving = re.compile('move (?P<move>\d+) from (?P<from>\d) to (?P<to>\d)')


def get(column, count):
    stack = []
    for _ in range(count):
        stack.append(column.pop(0))
    return stack


fd = open('Day5.txt', 'r')

storage = []
for line in fd:
    if re_cargo.search(line):
        finds = re_cargo.findall(line)
        if len(storage) < 1:
            storage = [[] for f in finds]
        for i, f in enumerate(finds):
            if f[1]:
                storage[i].append(f[1])
    elif re_moving.search(line):
        res = re_moving.match(line)
        count, start, end = int(res['move']), int(res['from'])-1, int(res['to'])-1
        # FIRST PART
        # for i in range(count):
        #     cargo = storage[start].pop(0)
        #     storage[end].insert(0, cargo)
        
        # SECOND PART
        cargo = get(storage[start], count)
        storage[end] = cargo + storage[end]
        
        # print(line)
        # for stack in storage:
        #     print(stack)

for stack in storage:
    print(stack.pop(0), end='')
