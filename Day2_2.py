fd = open('Day2.txt', 'r')

ldw = {'X':0, 'Y':3, 'Z':6}

total = 0
for line in fd:
    g_s, m_s = line.strip().split()
    g = ord(g_s) - ord('@')
    total += ldw[m_s]
    if m_s == 'Y':
        total += g
    elif m_s == 'X':
        total += g+2 if 0 < g+2 <= 3 else g-1
    else:
        total += g+1 if 0 < g+1 <= 3 else g-2

print(total)
