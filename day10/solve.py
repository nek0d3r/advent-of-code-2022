x = 1
cyclesToCheck = [20, 60, 100, 140, 180, 220]
signalStrengths = []
cycleWait = 0
instruction = ["noop"]
cycleCounter = 1

print(f"Sprite position\t: ###.....................................\n")

with open("input2.txt") as f:
    while True:
        if not cycleWait:
            line = f.readline()
            if not line:
                break
            print(f"Start cycle\t{cycleCounter}: begin executing {line.strip()}")
            instruction = line.strip().split(" ")
            if instruction[0] == "noop":
                cycleWait = 1
            elif instruction[0] == "addx":
                cycleWait = 2
        print(f"During cycle\t{cycleCounter}: CRT draws pixel in position {cycleCounter - 1}")
        print(f"Current CRT row: \n")
        # if cycleCounter % 40 == 0:
        #     print()
        # else:
        #     print("#", end = "")
        cycleWait -= 1
        if cycleCounter in cyclesToCheck:
            signalStrengths.append(x * cycleCounter)
        if not cycleWait:
            if instruction[0] == "addx":
                x += int(instruction[1])
            print(f"End of cycle\t{cycleCounter}: finish executing {' '.join(instruction)} (Register X is now {x})")
            print(f"Sprite position\t: ", end = "")
            print([i for i in range(int(cycleCounter / 40), 40)])
            for i in range(int(cycleCounter / 40) - 1, 40):
                print("#" if x in [i - 1, i, i + 1] else ".", end = "")
            print()

        cycleCounter += 1
print(f"Signal strength sum: {sum(signalStrengths)}")