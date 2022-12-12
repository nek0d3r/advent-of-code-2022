packetChars = []
messageChars = []
i = 1
j = 1
foundPacket = False
foundMessage = False

with open("input.txt") as f:
    while True:
        char = f.read(1)
        if not char:
            break
        if not foundPacket:
            packetChars.append(char)
            if len(packetChars) > 4:
                packetChars.pop(0)
        if not foundMessage:
            messageChars.append(char)
            if len(messageChars) > 14:
                messageChars.pop(0)
        foundPacket = len(packetChars) == 4 and not any(packetChars.count(c) > 1 for c in packetChars)
        foundMessage = len(messageChars) == 14 and not any(messageChars.count(c) > 1 for c in messageChars)
        if not foundPacket:
            i += 1
        if not foundMessage:
            j += 1
        if foundPacket and foundMessage:
            break
print(f"Unique packet signal start ", end = "")
for char in packetChars:
    print(f"{char}", end = "")
print(f" ends at {i}")
print(f"Unique message signal start ", end = "")
for char in messageChars:
    print(f"{char}", end = "")
print(f" ends at {j}")