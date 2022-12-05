fd = open('Day1.txt', 'r')

cals = []
sum_cal = 0
for line in fd:
    if line.strip():
        sum_cal += int(line.strip())
    else:
        cals.append(sum_cal)
        sum_cal = 0
print(sum(sorted(cals, reverse=True)[:3]))