import numpy as np

with open("input") as file:
    lines = [str(line.rstrip()).split(" ") for line in file.readlines()]

lines = [(line[0].split(','), line[2].split(',')) for line in lines]
coords = []

for line in lines:
    coord = []
    for seg in line:
        coord.append((int(seg[0]), int(seg[1])))
    coord.sort() # smallest value of each axis is now always in the left, we now only have to draw top to bottom
    # or left to right

    coords.append(coord)

grid_x = max([max(a[0], b[0]) for a, b in coords])
grid_y = max([max(a[1], b[1]) for a, b in coords])

# print(*coords, sep='\n')
# print(grid_x, grid_y)

grid = np.full((grid_y+1, grid_x+1), 0, dtype=int)
# print(grid)


def is_hoz_or_vert_line(line):
    a, b = line[0], line[1]
    return a[0] == b[0] or a[1] == b[1]

#
# good_lines = [coord for coord in coords if is_hoz_or_vert_line(coord)]
# print(*good_lines, sep='\n')


def gen_points_on_line(line):
    a, b = line[0], line[1]
    if a[0] == b[0]:
        return [(a[0], p) for p in range(a[1], b[1] + 1)]
    elif a[1] == b[1]:
        return [(p, a[1]) for p in range(a[0], b[0] + 1)]
    elif a[1] < b[1]:
        dif = b[0] - a[0]
        return [(a[0] + p, a[1] + p) for p in range(dif + 1)]
    else:
        dif = b[0] - a[0]
        return [(a[0] + p, a[1] - p) for p in range(dif + 1)]

# print(coords)
# print(gen_points_on_line(coords[5]))
# print(gen_points_on_line(coords[0]))

for line in coords:
    points = gen_points_on_line(line)
    for point in points:
        try:
            grid[point[1], point[0]] = grid[point[1], point[0]] + 1
        except:
            print("catch", line, point)

counts = np.bincount(grid.flatten())
print(grid)
print(counts)
print(sum(counts[2:]))
