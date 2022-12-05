fd = open('Day2.txt', 'r')

total = 0
for line in fd:
    g_s, m_s = line.strip().split()
    g, m = ord(g_s) - ord('@'), ord(m_s) - ord('W')
    val = g - m
    total += m
    if val in (-1, 2):
        total += 6
    elif val == 0:
        total += 3

print(total)
