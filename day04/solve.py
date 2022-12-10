contained = 0
overlap = 0
with open("input.txt") as f:
    for line in f:
        pair = line.strip().split(",")
        elf1 = pair[0].split("-")
        elf2 = pair[1].split("-")
        elf1Contains2 = True
        for i in range(int(elf2[0]), int(elf2[1]) + 1):
            if i not in range(int(elf1[0]), int(elf1[1]) + 1):
                elf1Contains2 = False
                break
        elf2Contains1 = True
        for i in range(int(elf1[0]), int(elf1[1]) + 1):
            if i not in range(int(elf2[0]), int(elf2[1]) + 1):
                elf2Contains1 = False
                break
        if elf1Contains2 or elf2Contains1:
            contained += 1
        for i in range(int(elf2[0]), int(elf2[1]) + 1):
            if i in range(int(elf1[0]), int(elf1[1]) + 1):
                overlap += 1
                break
print(f"Amount of contained ranges of roles: {contained}")
print(f"Amount of overlapped roles: {overlap}")
