fd = open('Day1.txt', 'r')

max_cal = 0
sum_cal = 0
for line in fd:
    if line.strip():
        sum_cal += int(line.strip())
    else:
        max_cal = max(max_cal, sum_cal)
        sum_cal = 0
print(max_cal)