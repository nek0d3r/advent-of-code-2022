from dataclasses import dataclass

@dataclass
class Node:
    value: int
    north: bool = False
    east: bool = False
    south: bool = False
    west: bool = False

content: str
with open("input2.txt") as f:
    content = f.read()

rows = content.splitlines()
map = []
for row in range(len(rows)):
    nodes = []
    for col in range(len(rows[row])):
        node = Node(rows[row][col])

        block: chr
        if rows[row][col] == 'S':
            block = 'a'
        elif rows[row][col] == 'E':
            block = 'z'
        else:
            block = rows[row][col]

        north_block = 'Z' if row - 1 < 0 else rows[row - 1][col]
        south_block = 'Z' if row + 1 >= len(rows) else rows[row + 1][col]
        west_block = 'Z' if col - 1 < 0 else rows[row][col - 1]
        east_block = 'Z' if col + 1 >= len(rows[row]) else rows[row][col + 1]

        if north_block in ['S', 'E'] or ord(north_block) <= ord(block) + 1:
            node.north = True
        if south_block in ['S', 'E'] or ord(south_block) <= ord(block) + 1:
            node.south = True
        if west_block in ['S', 'E'] or ord(west_block) <= ord(block) + 1:
            node.west = True
        if east_block in ['S', 'E'] or ord(east_block) <= ord(block) + 1:
            node.east = True
        nodes.append(node)
    map.append(nodes)

print(map)