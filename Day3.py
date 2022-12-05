fd = open('Day3.txt', 'r')

def priority(prod):
    offset = 27 - ord('A') if prod.isupper() else 1 - ord('a')
    return ord(prod) + offset 

# Day3_1
# total = 0
# for line in fd:
#     line = line.strip()
#     mid = len(line)//2
#     sym_left, sym_right = set(line[:mid]), set(line[mid:])
#     total += priority((sym_left & sym_right).pop())
# print(total)

# Day3_2
total = 0
lines = fd.readlines()
i = 0
while i < len(lines):
    r1, r2, r3 = set(lines[i].strip()), set(lines[i+1].strip()), set(lines[i+2].strip())
    total += priority((r1 & r2 & r3).pop())
    i += 3
print(total)