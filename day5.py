f = open("5.txt", "r").read().splitlines()

occurrences = {}

for line in f:
    line = [list(map(int, l.strip().split(','))) for l in line.split('->')]
    if line[0][0] == line[1][0]:
        distance = line[1][1] - line[0][1]
        current = line[0]
        for i in range(abs(distance)+1):
            if tuple(current) in occurrences.keys():
                occurrences[tuple(current)] += 1
            else:
                occurrences[tuple(current)] = 1
            current[1] += int(distance/abs(distance))
    elif line[0][1] == line[1][1]:
        distance = line[1][0] - line[0][0]
        current = line[0]
        for i in range(abs(distance)+1):
            if tuple(current) in occurrences.keys():
                occurrences[tuple(current)] += 1
            else:
                occurrences[tuple(current)] = 1
            current[0] += int(distance/abs(distance))

print("Part 1: ", sum(1 for value in occurrences.values() if value >= 2))

occurrences = {}

for line in f:
    line = [list(map(int, l.strip().split(','))) for l in line.split('->')]
    if line[0][0] == line[1][0]:
        distance = line[1][1] - line[0][1]
        current = line[0]
        for i in range(abs(distance)+1):
            if tuple(current) in occurrences.keys():
                occurrences[tuple(current)] += 1
            else:
                occurrences[tuple(current)] = 1
            current[1] += int(distance/abs(distance))
    elif line[0][1] == line[1][1]:
        distance = line[1][0] - line[0][0]
        current = line[0]
        for i in range(abs(distance)+1):
            if tuple(current) in occurrences.keys():
                occurrences[tuple(current)] += 1
            else:
                occurrences[tuple(current)] = 1
            current[0] += int(distance/abs(distance))
    else:
        distanceX = line[1][0] - line[0][0]
        distanceY = line[1][1] - line[0][1]
        current = line[0]
        for i in range(abs(distanceX)+1):
            if tuple(current) in occurrences.keys():
                occurrences[tuple(current)] += 1
            else:
                occurrences[tuple(current)] = 1
            current[0] += int(distanceX/abs(distanceX))
            current[1] += int(distanceY / abs(distanceY))

print("Part 2: ", sum(1 for value in occurrences.values() if value >= 2))