f = open("12.txt", "r").read().splitlines()

paths = dict()

for path in f:
    path = path.split('-')
    if path[0] in paths:
        paths[path[0]].append(path[1])
    else:
        paths[path[0]] = [path[1]]
    if path[1] in paths:
        paths[path[1]].append(path[0])
    else:
        paths[path[1]] = [path[0]]


def determine_paths(current, m, visited=set()):
    if current == 'end':
        return 1
    total_paths = 0
    if current.islower():
        visited.add(current)
    for connection in m[current]:
        if connection not in visited:
            total_paths += determine_paths(connection, m, visited.copy())
    return total_paths


print("Part 1: " + str(determine_paths('start', paths)))


def determine_paths_part2(current, m, visited=[], twice=False):
    if current == 'end':
        return 1
    total_paths = 0
    if current.islower():
        visited.append(current)
    for connection in m[current]:
        if connection != 'start' and visited.count(connection) == 1 and not twice:
            total_paths += determine_paths_part2(connection, m, visited.copy(), True)
        elif connection not in visited:
            total_paths += determine_paths_part2(connection, m, visited.copy(), twice)
    return total_paths


print("Part 2: " + str(determine_paths_part2('start', paths)))
