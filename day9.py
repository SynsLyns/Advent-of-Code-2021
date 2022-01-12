f = [[int(char) for char in x] for x in open("9.txt", "r").read().splitlines()]

low_points = []
basin_sizes = []
adjacent_tiles = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def add1(x):
    return x + 1


def get_basin_size(x, y, m, visited=[]):
    if x < 0 or x >= len(m) or y < 0 or y >= len(m[x]) or m[x][y] == 9 or [x, y] in visited:
        return 0
    else:
        visited.append([x, y])
        return 1 + get_basin_size(x + 1, y, m, visited) \
               + get_basin_size(x - 1, y, m, visited) \
               + get_basin_size(x, y + 1, m, visited) \
               + get_basin_size(x, y - 1, m, visited)


for row, arr in enumerate(f):
    for col, value in enumerate(arr):
        is_low = True
        for adjacent in adjacent_tiles:
            if row + adjacent[0] < 0 or row + adjacent[0] >= len(f) or col + adjacent[1] < 0 \
                    or col + adjacent[1] >= len(arr):
                continue
            else:
                if f[row + adjacent[0]][col + adjacent[1]] <= value:
                    is_low = False
        if is_low:
            low_points.append(value)
            basin_sizes.append(get_basin_size(row, col, f))

print("Part 1: " + str(sum(map(add1, low_points))))

product = 1

for i in range(3):
    product *= max(basin_sizes)
    basin_sizes.remove(max(basin_sizes))

print("Part 2: " + str(product))
