f = [[int(char) for char in x] for x in open("11.txt", "r").read().splitlines()]

flashes = 0
steps = 100
directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

for i in range(steps):

    # first step: increase all energy by 1
    for row in range(10):
        for col in range(10):
            f[row][col] += 1

    flashed = []

    # second step: flash octopus with energy > 9
    while True:
        update = False
        for row in range(10):
            for col in range(10):
                if [row, col] not in flashed and f[row][col] > 9:
                    update = True
                    flashed.append([row, col])
                    flashes += 1
                    for d in directions:
                        if 0 <= row + d[0] <= 9 and 0 <= col + d[1] <= 9:
                            f[row + d[0]][col + d[1]] += 1
        if not update:
            break

    # final step: set flashed octopus to 0 energy
    for octopus in flashed:
        f[octopus[0]][octopus[1]] = 0

print("Part 1: " + str(flashes))
step = 100

while True:

    # first step: increase all energy by 1
    for row in range(10):
        for col in range(10):
            f[row][col] += 1

    flashed = []

    # second step: flash octopus with energy > 9
    while True:
        update = False
        for row in range(10):
            for col in range(10):
                if [row, col] not in flashed and f[row][col] > 9:
                    update = True
                    flashed.append([row, col])
                    flashes += 1
                    for d in directions:
                        if 0 <= row + d[0] <= 9 and 0 <= col + d[1] <= 9:
                            f[row + d[0]][col + d[1]] += 1
        if not update:
            break

    # final step: set flashed octopus to 0 energy
    for octopus in flashed:
        f[octopus[0]][octopus[1]] = 0

    step += 1

    if sum([sum(line) for line in f]) == 0:
        break


print("Part 2: " + str(step))
