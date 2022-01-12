f = open("10.txt", "r").read().splitlines()

matchings = {'[': ']',
             '(': ')',
             '{': '}',
             '<': '>'}

point_dic = {')': 3,
             ']': 57,
             '}': 1197,
             '>': 25137}

illegal = []

incomplete = []

for line in f:
    stack = []
    incomplete.append(line)
    for char in line:
        if char in matchings:
            stack.append(char)
        else:
            if matchings[stack[-1]] == char:
                stack.pop()
            else:
                illegal.append(char)
                incomplete.pop()
                break

score = 0
for item in illegal:
    score += point_dic[item]

print("Part 1: " + str(score))

incomplete_point = {')': 1,
                    ']': 2,
                    '}': 3,
                    '>': 4}

scores = []

for line in incomplete:
    stack = []
    for char in line:
        if char in matchings:
            stack.append(char)
        elif matchings[stack[-1]] == char:
            stack.pop()
    stack = [matchings[char] for char in reversed(stack)]
    total = 0
    for item in stack:
        total *= 5
        total += incomplete_point[item]
    scores.append(total)

print("Part 2: " + str(sorted(scores)[int(len(scores)/2)]))
