lines = []
with open("./input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip())

totalCal = []
count = 0
for line in lines:
    if line == "":
        totalCal.append(count)
        count = 0
    else:
        count += int(line)

firstElf = max(totalCal)
totalCal.remove(firstElf)
secondElf = max(totalCal)
totalCal.remove(secondElf)
thirdElf = max(totalCal)

print(firstElf + secondElf + thirdElf)