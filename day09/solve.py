state = [[True]]
knotState = [[True]]
head = [0, 0]
tail = [0, 0]
knots = []
for i in range(0, 10):
    knots.append([0, 0])

def showState(state, knotState, head, tail, knots, showTail = True, wait = True):
    for row in range(0, len(state)):
        for col in range(0, len(state[0])):
            if head == [row, col]:
                print("H", end = "")
            elif tail == [row, col] and showTail:
                print("T", end = "")
            elif not showTail and [row, col] in knots[1:]:
                for i in range(1, len(knots)):
                    if knots[i] == [row, col]:
                        print(f"{i}", end = "")
                        break
            elif showTail:
                print(f"{'#' if state[row][col] else '.'}", end = "")
            else:
                print(f"{'#' if knotState[row][col] else '.'}", end = "")
        print()
    if wait:
        input("Press enter to continue...")

def moveVertical(state, knotState, head, tail, knots, amount):
    step = int(amount / abs(amount))
    for _ in range(0, amount, step):
        if head[0] + step < 0:
            state.insert(0, [False] * len(state[0]))
            knotState.insert(0, [False] * len(knotState[0]))
            tail[0] -= step
            for knot in knots[1:]:
                knot[0] -= step
        elif head[0] + step >= len(state):
            state.append([False] * len(state[0]))
            knotState.append([False] * len(knotState[0]))
            head[0] += step
            knots[0][0] += step
        else:
            head[0] += step
            knots[0][0] += step
        updateTail(state, head, tail)
        updateKnots(knotState, knots)

def moveHorizontal(state, knotState, head, tail, knots, amount):
    step = int(amount / abs(amount))
    for _ in range(0, amount, step):
        if head[1] + step < 0:
            for stateRow in state:
                stateRow.insert(0, False)
            for stateRow in knotState:
                stateRow.insert(0, False)
            tail[1] -= step
            for knot in knots[1:]:
                knot[1] -= step
        elif head[1] + step >= len(state[0]):
            for stateRow in state:
                stateRow.append(False)
            for stateRow in knotState:
                stateRow.append(False)
            head[1] += step
            knots[0][1] += step
        else:
            head[1] += step
            knots[0][1] += step
        updateTail(state, head, tail)
        updateKnots(knotState, knots)

def updateTail(state, head, tail):
    if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
        return
    if tail[0] != head[0]:
        tail[0] += 1 if tail[0] < head[0] else -1
    if tail[1] != head[1]:
        tail[1] += 1 if tail[1] < head[1] else -1
    state[tail[0]][tail[1]] = True

def updateKnots(knotState, knots):
    oldTail = knots[len(knots) - 1].copy()
    for knot in range(1, len(knots)):
        if abs(knots[knot][0] - knots[knot - 1][0]) <= 1 and abs(knots[knot][1] - knots[knot - 1][1]) <= 1:
            continue
        if knots[knot][0] != knots[knot - 1][0]:
            knots[knot][0] += 1 if knots[knot][0] < knots[knot - 1][0] else -1
        if knots[knot][1] != knots[knot - 1][1]:
            knots[knot][1] += 1 if knots[knot][1] < knots[knot - 1][1] else -1
    if knots[len(knots) - 1] != oldTail:
        knotState[knots[len(knots) - 1][0]][knots[len(knots) - 1][1]] = True

with open("input.txt") as f:
    while True:
        #showState(state, knotState, head, tail, knots, False)
        line = f.readline()
        if not line:
            break
        move = line.strip().split(" ")
        if move[0] == "U":
            moveVertical(state, knotState, head, tail, knots, -int(move[1]))
        elif move[0] == "D":
            moveVertical(state, knotState, head, tail, knots, int(move[1]))
        elif move[0] == "L":
            moveHorizontal(state, knotState, head, tail, knots, -int(move[1]))
        elif move[0] == "R":
            moveHorizontal(state, knotState, head, tail, knots, int(move[1]))

spacesVisited = 0
for row in state:
    for col in row:
        spacesVisited += 1 if col else 0

print(f"Spaces visited: {spacesVisited}")

knotSpacesVisited = 0
for row in knotState:
    for col in row:
        knotSpacesVisited += 1 if col else 0

print(f"Knot spaces visited: {knotSpacesVisited}")