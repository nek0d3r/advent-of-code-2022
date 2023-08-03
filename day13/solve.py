import ast, os

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
            return True
        elif left == right:
            print("Continue compare")
            return None
        else:
            print("Inputs are in wrong order")
            return False
    elif len(left) == 0:
        print("Inputs are in right order")
        return True
    elif len(right) == 0:
        print("Inputs are in wrong order")
        return False
    else:
        i = 0
        while i < len(left) and i < len(right):
            result = compare(left[i], right[i], depth + 1)
            if result != None:
                return result
            i += 1
        if i == len(right) and i < len(left):
            print("Inputs are in wrong order")
            return False
        elif depth > 0:
            print("Continue compare")
            return None
        else:
            print("Ran out of items, inputs are in right order")
            return True

with open("input.txt") as f:
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
        input()
        os.system("cls")

        if result:
            sum += index
        index += 1
    
    print(f"Pair indices sum: {sum}")