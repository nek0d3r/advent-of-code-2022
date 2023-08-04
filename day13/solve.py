import ast
from functools import cmp_to_key

def compare(left, right, depth = 0):
    print(f"{left}<=>{right}")
    if type(left) is list and type(right) is int:
        print("Convert right to list")
        return compare(left, [right], depth + 1)
    elif type(left) is int and type(right) is list:
        print("Convert left to list")
        return compare([left], right, depth + 1)
    elif type(left) is int and type(right) is int:
        if left < right:
            print("Inputs are in right order")
            return -1
        elif left == right:
            print("Continue compare")
            return 0
        else:
            print("Inputs are in wrong order")
            return 1
    else:
        i = 0
        while i < len(left) and i < len(right):
            result = compare(left[i], right[i], depth + 1)
            if result != 0:
                return result
            i += 1
        if i == len(right) and i < len(left):
            print("Inputs are in wrong order")
            return 1
        elif i == len(left) and i < len(right):
            print("Inputs are in right order")
            return -1
        elif depth > 0:
            print("Continue compare")
            return 0
        else:
            print("Ran out of items, inputs are in right order")
            return 0

def solve1(file):
    with open(file) as f:
        index = 1
        sum = 0
        while True:
            left_packet = f.readline()
            right_packet = f.readline()
            f.readline()
            if not left_packet or not right_packet:
                break
            left = ast.literal_eval(left_packet.strip())
            right = ast.literal_eval(right_packet.strip())
            
            result = compare(left, right)
            print(result)
            print()

            if result != 1:
                sum += index
            index += 1
        
        print(f"Pair indices sum: {sum}")

def solve2(file):
    content: str
    with open(file) as f:
        content = f.read()
    content = content.replace("\n\n", "\n")

    packets = []
    for line in content.splitlines():
        packets.append(ast.literal_eval(line.strip()))
    packets.append([[2]])
    packets.append([[6]])
    packets_ordered = sorted(packets, key=cmp_to_key(compare))
    print(f"\nDecoder key: {(packets_ordered.index([[2]]) + 1) * (packets_ordered.index([[6]]) + 1)}")

solve2("input.txt")