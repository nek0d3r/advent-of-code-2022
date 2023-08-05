import itertools

def solve(file, floor):
    map_coords = []
    with open(file) as f:
        while True:
            path = f.readline().strip()
            if not path:
                break

            lines = []
            for point in path.split(" -> "):
                coords = point.split(",")
                lines.append((int(coords[0]), int(coords[1])))
            map_coords.append(lines)

    x_coords = list(itertools.chain(*[[j[0] for j in i] for i in map_coords]))
    x_coords.append(500)
    y_coords = list(itertools.chain(*[[j[1] for j in i] for i in map_coords]))

    lower_bound = max(y_coords)
    left_bound = min(x_coords)
    right_bound = max(x_coords)

    map = [['.']*(right_bound - left_bound + 1) for _ in range(lower_bound + 1)]
    for path in map_coords:
        for cur in range(1, len(path)):
            if path[cur - 1][0] == path[cur][0]:
                bounds = sorted([path[cur - 1][1], path[cur][1]])
                for i in range(bounds[0], bounds[1] + 1):
                    map[i][path[cur][0] - left_bound] = '#'
            else:
                bounds = sorted([path[cur - 1][0] - left_bound, path[cur][0] - left_bound])
                for i in range(bounds[0], bounds[1] + 1):
                    map[path[cur][1]][i] = '#'

    if floor:
        map.append(['.']*(right_bound - left_bound + 1))
        map.append(['#']*(right_bound - left_bound + 1))

    sand_origin = (500 - left_bound, 0)

    sand = None
    while True:
        if not sand:
            if map[sand_origin[1]][sand_origin[0]] != '.':
                break
            sand = sand_origin
        else:
            if sand[0] == 0:
                sand = (sand[0] + 1, sand[1])
                sand_origin = (sand_origin[0] + 1, sand_origin[1])
                for row in range(len(map)):
                    map[row].insert(0, '.')
                if floor:
                    map[len(map) - 1][0] = '#'
            
            if sand[0] == len(map[0]) - 1:
                for row in range(len(map)):
                    map[row].append('.')
                if floor:
                    map[len(map) - 1][len(map[0]) - 1] = '#'
            
            if sand[1] + 1 >= len(map):
                sand = None
                break
            elif map[sand[1] + 1][sand[0]] == '.':
                sand = (sand[0], sand[1] + 1)
            elif map[sand[1] + 1][sand[0] - 1] == '.':
                sand = (sand[0] - 1, sand[1] + 1)
            elif map[sand[1] + 1][sand[0] + 1] == '.':
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                map[sand[1]][sand[0]] = 'o'
                sand = None
                # for row in map:
                #     for char in row:
                #         print(char, end='')
                #     print()
                # print()

    for row in map:
        for char in row:
            print(char, end='')
        print()

    print(f"Resting sand: {list(itertools.chain(*map)).count('o')}")

def solve1(file):
    solve(file, False)

def solve2(file):
    solve(file, True)

solve2("input.txt")