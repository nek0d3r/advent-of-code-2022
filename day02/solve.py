# A and X: rock
# B and Y: paper
# C and Z: scissors

# X: lose
# Y: draw
# Z: win

strategy = []

with open("./input.txt") as f:
    lines = f.readlines()
    for line in lines:
        play = line.strip().split(" ")
        player1 = ""
        player2 = ""
        result = ""

        if play[0] == "A":
            player2 = "R"
        elif play[0] == "B":
            player2 = "P"
        else:
            player2 = "S"

        if play[1] == "X":
            player1 = "R"
            result = "L"
        elif play[1] == "Y":
            player1 = "P"
            result = "D"
        else:
            player1 = "S"
            result = "W"
        
        strategy.append(((player1, player2, result)))

part1Score = 0
part2Score = 0
for play in strategy:
    # We know there's a tie
    if play[0] == play[1]:
        part1Score += 3
    # Player 1 wins
    elif (play[0] == "R" and play[1] != "P") or \
        (play[0] == "P" and play[1] != "S") or \
        (play[0] == "S" and play[1] != "R"):
        part1Score += 6
    
    # Add score based on what we play
    if play[0] == "R":
        part1Score += 1
    elif play[0] == "P":
        part1Score += 2
    else:
        part1Score += 3
    
    # According to new strategy
    # We need to win
    if play[2] == "W":
        part2Score += 6
        # Played rock, we play paper
        if play[1] == "R":
            part2Score += 2
        # Played paper, we play scissors
        elif play[1] == "P":
            part2Score += 3
        # Played scissors, we play rock
        else:
            part2Score += 1
    # We need to draw
    elif play[2] == "D":
        part2Score += 3
        # Played rock, we play rock
        if play[1] == "R":
            part2Score += 1
        # Played paper, we play paper
        elif play[1] == "P":
            part2Score += 2
        # Played scissors, we play scissors
        else:
            part2Score += 3
    # We need to lose
    else:
        # Played rock, we play scissors
        if play[1] == "R":
            part2Score += 3
        # Played paper, we play rock
        elif play[1] == "P":
            part2Score += 1
        # Played scissors, we play paper
        else:
            part2Score += 2

print(f"Total score based on strategy 1: {part1Score}")
print(f"Total score based on strategy 2: {part2Score}")