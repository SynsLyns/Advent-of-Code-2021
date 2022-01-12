f = [[int(char) for char in x] for x in open("15.txt", "r").read().splitlines()]
directions = [[1,0],[-1,0],[0,1],[0,-1]]

start = [0,0]

def estimate_lowest_path(s, m):
    path = []
    pos = s
    risk = 0
    while True:
        min_path = [0,0]
        min_value = -1
        for dir in directions:
            if [pos[0] + dir[0], pos[1] + dir[1]] not in path:
                if m[pos[0] + dir[0], pos[1] + dir[1]] < min_value or min_value == -1:
                    min_value = m[pos[0] + dir[0], pos[1] + dir[1]]
                    min_path = [pos[0] + dir[0], pos[1] + dir[1]]
        path.append(pos)
        pos = min_path
        risk += min_value
    return value

