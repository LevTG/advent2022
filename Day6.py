fd = open('Day6.txt', 'r')

marker = 14

line = fd.readline().strip()
for i in range(len(line)):
    if len(set(list(line[i:i+marker]))) == marker:
        print(i+marker)
        break
