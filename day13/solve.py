import ast

def compare(left, right):
    print(f"{left}<=>{right}")
    if type(left) is list and type(right) is int:
        print("Convert right to list")
        compare(left, [right])
    elif type(left) is int and type(right) is list:
        print("Convert left to list")
        compare([left], right)
    elif type(left) is int and type(right) is int:
        if left < right:
            print("Inputs are in right order")
            return True
        elif left == right:
            print("Continue compare")
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
            compare(left[i], right[i])
            i += 1
        if i == len(right) and i < len(left):
            print("Inputs are in wrong order")
            return False
        else:
            print("Inputs are in right order")
            return True

with open("input2.txt") as f:
    while True:
        left = ast.literal_eval(f.readline().strip())
        right = ast.literal_eval(f.readline().strip())
        f.readline()
        if not left or not right:
            break
        
        result = compare(left, right)
        print(result)
        print()