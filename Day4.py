fd = open('Day4.txt', 'r')

def check_contain(borders, pars):
    return borders[0] <= pars[0] and pars[1] <= borders[1]

def check_overlap(borders, pars):
    return pars[0] <= borders[0] and pars[1] >= borders[0]

total = 0
for line in fd:
    elf1, elf2 = list(map(lambda x: tuple(map(int, x.split('-'))), line.strip().split(',')))
    total += check_overlap(elf1, elf2) or check_overlap(elf2, elf1)

print(total)