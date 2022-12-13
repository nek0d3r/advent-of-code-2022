def isVisible(forest, row, col):
    north = True
    northScore = 0
    for i in reversed(range(0, row)):
        northScore += 1
        if forest[i][col] >= forest[row][col]:
            north = False
            break
    south = True
    southScore = 0
    for i in range(row + 1, len(forest)):
        southScore += 1
        if forest[i][col] >= forest[row][col]:
            south = False
            break
    west = True
    westScore = 0
    for i in reversed(range(0, col)):
        westScore += 1
        if forest[row][i] >= forest[row][col]:
            west = False
            break
    east = True
    eastScore = 0
    for i in range(col + 1, len(forest[0])):
        eastScore += 1
        if forest[row][i] >= forest[row][col]:
            east = False
            break
    return north or south or west or east, northScore * southScore * westScore * eastScore

forest = []
with open("input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        forest.append(list(line.strip()))

visibleTrees = 0
scenicTree = (0, 0, 0)
for row in range(0, len(forest)):
    for col in range(0, len(forest[0])):
        visible, scenicScore = isVisible(forest, row, col)
        visibleTrees += 1 if visible else 0
        if scenicScore > scenicTree[2]:
            scenicTree = (row, col, scenicScore)

print(f"Visible trees: {visibleTrees}")
print(f"Most scenic tree is [x:{scenicTree[1] + 1},y:{scenicTree[0] + 1}] tree at score {scenicTree[2]}")