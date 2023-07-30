from dataclasses import dataclass
import itertools

@dataclass
class Node:
    value: int
    north: int = None
    east: int = None
    south: int = None
    west: int = None
    dist: float = float("inf")
    prev: int = None

content: str
with open("input2.txt") as f:
    content = f.read()

rows = content.splitlines()
start: int
end: int
map = []
for row in range(len(rows)):
    nodes = []
    for col in range(len(rows[row])):
        node = Node(rows[row][col])

        block: chr
        if rows[row][col] == 'S':
            block = 'a'
            start = row * len(rows[row]) + col
        elif rows[row][col] == 'E':
            block = 'z'
            end = row * len(rows[row]) + col
        else:
            block = rows[row][col]

        north_block = '|' if row - 1 < 0 else rows[row - 1][col]
        south_block = '|' if row + 1 >= len(rows) else rows[row + 1][col]
        west_block = '|' if col - 1 < 0 else rows[row][col - 1]
        east_block = '|' if col + 1 >= len(rows[row]) else rows[row][col + 1]

        if north_block in ['S', 'E'] or ord(north_block) <= ord(block) + 1:
            node.north = (row - 1) * len(rows[row]) + col
        if south_block in ['S', 'E'] or ord(south_block) <= ord(block) + 1:
            node.south = (row + 1) * len(rows[row]) + col
        if west_block in ['S', 'E'] or ord(west_block) <= ord(block) + 1:
            node.west = row * len(rows[row]) + col - 1
        if east_block in ['S', 'E'] or ord(east_block) <= ord(block) + 1:
            node.east = row * len(rows[row]) + col + 1
        nodes.append(node)
    map.append(nodes)

graph = list(itertools.chain(*map))
print(graph)

graph[start].dist = 0
visited = []
unvisited = [i for i in range(len(graph))]
vertex = start
while len(unvisited) > 0:
    shortest = float("inf")
    for node in unvisited:
        if graph[node].dist < shortest:
            vertex = node
            shortest = graph[node].dist
    
    if graph[vertex].north in unvisited and graph[vertex].dist + 1 < graph[graph[vertex].north].dist:
        graph[graph[vertex].north].dist = graph[vertex].dist + 1
    if graph[vertex].east in unvisited and graph[vertex].dist + 1 < graph[graph[vertex].east].dist:
        graph[graph[vertex].east].dist = graph[vertex].dist + 1
    if graph[vertex].south in unvisited and graph[vertex].dist + 1 < graph[graph[vertex].south].dist:
        graph[graph[vertex].south].dist = graph[vertex].dist + 1
    if graph[vertex].west in unvisited and graph[vertex].dist + 1 < graph[graph[vertex].west].dist:
        graph[graph[vertex].west].dist = graph[vertex].dist + 1

    visited.append(vertex)
    unvisited.remove(vertex)

print(graph[end].dist)