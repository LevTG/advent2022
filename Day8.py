import numpy as np
from functools import reduce

fd = open('Day8.txt', 'r')

forest = []

for line in fd:
    forest.append(list(map(int, list(line.strip()))))
forest = np.array(forest)

vis = np.zeros(forest.shape, dtype=bool)
vis[0, :] = True
vis[:, 0] = True
vis[-1, :] = True
vis[:, -1] = True

def check_vis(part, tree):
    return tree > np.max(part)


for row in range(1, forest.shape[0]-1):
    for col in range(1, forest.shape[1]-1):
        slices = [forest[:row, col], forest[row, :col], forest[row+1:, col], forest[row, col+1:]]
        visibleness = [check_vis(part, forest[row][col]) for part in slices]
        # print(visibleness)
        vis[row][col] = reduce(lambda x, y: x or y, visibleness)

# print(np.invert(vis))
print(np.sum(vis))


# PART TWO
def count_vis(part, azi, tree):
    if azi < 0:
        part = part[::-1]
    dist = 0
    for h in part:
        if tree > h:
            dist += 1
        else:
            return dist + 1
    return dist
vis = np.zeros(forest.shape)

for row in range(1, forest.shape[0]-1):
    for col in range(1, forest.shape[1]-1):
        azis = [-1, -1, 1, 1]
        slices = [forest[:row, col], forest[row, :col], forest[row+1:, col], forest[row, col+1:]]
        visibleness = [count_vis(part, azi, forest[row][col]) for part, azi in zip(slices, azis)]
        # print(visibleness)
        vis[row][col] = reduce(lambda x, y: x * y, visibleness)

print(np.max(vis))

