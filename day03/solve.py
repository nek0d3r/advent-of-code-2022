totalPriority1 = 0
totalPriority2 = 0
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

lines = []
with open("./input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip())

for i in range(0, len(lines)):
    bag = lines[i]
    compartment1 = bag[:int(len(bag)/2)]
    compartment2 = bag[int(len(bag)/2):]
    
    if i % 3 == 0:
        for char in bag:
            if lines[i + 1].find(char) != -1 and lines[i + 2].find(char) != -1:
                totalPriority2 += priority.find(char) + 1
                break

    for char in compartment1:
        if compartment2.find(char) != -1:
            totalPriority1 += priority.find(char) + 1
            break

print(f"Total priority: {totalPriority1}")
print(f"Total priority for groups: {totalPriority2}")