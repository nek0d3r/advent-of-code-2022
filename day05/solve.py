with open("input.txt") as f:
    readingCrates = True
    crateDims = []
    stacks = {}
    part2Stacks = {}
    for line in f:
        if readingCrates:
            if line == "\n":
                for i in range(0, len(crateDims[0])):
                    stacks[crateDims[0][i]] = []
                    part2Stacks[crateDims[0][i]] = []
                    for j in range(1, len(crateDims)):
                        if crateDims[j][i] == " ": break
                        stacks[crateDims[0][i]].append(crateDims[j][i])
                        part2Stacks[crateDims[0][i]].append(crateDims[j][i])
                readingCrates = False
                continue
            crateDims.insert(0, [line[i+1:i+2] for i in range(0, len(line), 4)])
        else:
            move = line.strip().split(" ")
            del move[0]
            del move[1]
            del move[2]
            crane = []
            for i in range(0, int(move[0])):
                crate = stacks[move[1]].pop()
                crane.append(part2Stacks[move[1]].pop())
                stacks[move[2]].append(crate)
            for i in range(0, len(crane)):
                crate = crane.pop()
                part2Stacks[move[2]].append(crate)
    print("Message response: ", end = "")
    for key, stack in stacks.items():
        print(f"{stack[len(stack)-1:][0]}", end = "")
    print()
    print("Part 2 message response: ", end = "")
    for key, stack in part2Stacks.items():
        print(f"{stack[len(stack)-1:][0]}", end = "")
    print()
