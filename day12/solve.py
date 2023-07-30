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
with open("input.txt") as f:
    content = f.read()

rows = content.splitlines()
start: int
lowest = []
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
        if block == 'a':
            lowest.append(row * len(rows[row]) + col)

        north_block = '|' if row - 1 < 0 else rows[row - 1][col]
        if north_block == 'S':
            north_block = 'a'
        if north_block == 'E':
            north_block = 'z'
        south_block = '|' if row + 1 >= len(rows) else rows[row + 1][col]
        if south_block == 'S':
            south_block = 'a'
        if south_block == 'E':
            south_block = 'z'
        west_block = '|' if col - 1 < 0 else rows[row][col - 1]
        if west_block == 'S':
            west_block = 'a'
        if west_block == 'E':
            west_block = 'z'
        east_block = '|' if col + 1 >= len(rows[row]) else rows[row][col + 1]
        if east_block == 'S':
            east_block = 'a'
        if east_block == 'E':
            east_block = 'z'

        if ord(north_block) <= ord(block) + 1:
            node.north = (row - 1) * len(rows[row]) + col
        if ord(south_block) <= ord(block) + 1:
            node.south = (row + 1) * len(rows[row]) + col
        if ord(west_block) <= ord(block) + 1:
            node.west = row * len(rows[row]) + col - 1
        if ord(east_block) <= ord(block) + 1:
            node.east = row * len(rows[row]) + col + 1
        nodes.append(node)
    map.append(nodes)

graph = list(itertools.chain(*map))

paths = []
for low in lowest:
    for node in graph:
        node.dist = float("inf")
        node.prev = None

    graph[low].dist = 0
    visited = []
    unvisited = [i for i in range(len(graph))]
    vertex = low
    while len(unvisited) > 0:
        shortest = float("inf")
        vertex = unvisited[0]
        for node in unvisited:
            if graph[node].dist < shortest:
                vertex = node
                shortest = graph[node].dist
        
        if graph[vertex].north in unvisited and graph[vertex].dist + 1 < graph[graph[vertex].north].dist:
            graph[graph[vertex].north].dist = graph[vertex].dist + 1
            graph[graph[vertex].north].prev = vertex
        if graph[vertex].east in unvisited and graph[vertex].dist + 1 < graph[graph[vertex].east].dist:
            graph[graph[vertex].east].dist = graph[vertex].dist + 1
            graph[graph[vertex].east].prev = vertex
        if graph[vertex].south in unvisited and graph[vertex].dist + 1 < graph[graph[vertex].south].dist:
            graph[graph[vertex].south].dist = graph[vertex].dist + 1
            graph[graph[vertex].south].prev = vertex
        if graph[vertex].west in unvisited and graph[vertex].dist + 1 < graph[graph[vertex].west].dist:
            graph[graph[vertex].west].dist = graph[vertex].dist + 1
            graph[graph[vertex].west].prev = vertex

        visited.append(vertex)
        # print(f"Removing {vertex} from {unvisited}")
        unvisited.remove(vertex)

    for node in graph:
        # print(f"{graph.index(node)} ({node.value})\t{node.dist}\t{node.prev}")
        if node.value == 'E':
            paths.append(node.dist)

print(f"Shortest steps to goal: {min(paths)}")