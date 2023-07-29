x = 1
cyclesToCheck = [20, 60, 100, 140, 180, 220]
signalStrengths = []
cycleWait = 0
instruction = ["noop"]
cycleCounter = 1
crt = ["." for i in range(40*6)]

with open("input.txt") as f:
    while True:
        if not cycleWait:
            line = f.readline()
            if not line:
                break
            instruction = line.strip().split(" ")
            if instruction[0] == "noop":
                cycleWait = 1
            elif instruction[0] == "addx":
                cycleWait = 2
        cycleWait -= 1
        if cycleCounter in cyclesToCheck:
            signalStrengths.append(x * cycleCounter)
        if not cycleWait:
            if instruction[0] == "addx":
                x += int(instruction[1])
        
        # CRT display
        print("column: " + str(cycleCounter % 40) + ", x: " + str(x))
        if (cycleCounter % 40 >= x - 1 and cycleCounter % 40 <= x + 1):
            crt[cycleCounter] = "#"

        cycleCounter += 1
display = ""
for i in range(len(crt)):
    display += crt[i]
    if (i + 1) % 40 == 0:
        display += "\n"
print(display)
print(f"Signal strength sum: {sum(signalStrengths)}")