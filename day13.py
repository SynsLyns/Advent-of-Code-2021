f = open("13.txt", "r").read().splitlines()

dots = [list(map(int, x.split(','))) for x in f[:f.index('')]]
instructions = [[x[0][-1], x[1]] for x in [element.split('=') for element in f[f.index('') + 1:]]]

instruction = instructions[0]
fold = int(instruction[1])
for dot in dots:
    if instruction[0] == 'y':
        if dot[1] > fold and 2 * fold - dot[1] >= 0 and [dot[0], 2 * fold - dot[1]] not in dots:
            dots.append([dot[0], 2 * fold - dot[1]])
    elif instruction[0] == 'x':
        if dot[0] > fold and 2 * fold - dot[0] >= 0 and [2 * fold - dot[0], dot[1]] not in dots:
            dots.append([2 * fold - dot[0], dot[1]])
if instruction[0] == 'y':
    dots = [dot for dot in dots if dot[1] < fold]
else:
    dots = [dot for dot in dots if dot[0] < fold]

print("Part 1: " + str(len(dots)))

dots = [list(map(int, x.split(','))) for x in f[:f.index('')]]
instructions = [[x[0][-1], x[1]] for x in [element.split('=') for element in f[f.index('') + 1:]]]

for instruction in instructions:
    fold = int(instruction[1])
    for dot in dots:
        if instruction[0] == 'y':
            if dot[1] > fold and 2 * fold - dot[1] >= 0 and [dot[0], 2 * fold - dot[1]] not in dots:
                dots.append([dot[0], 2 * fold - dot[1]])
        elif instruction[0] == 'x':
            if dot[0] > fold and 2 * fold - dot[0] >= 0 and [2 * fold - dot[0], dot[1]] not in dots:
                dots.append([2 * fold - dot[0], dot[1]])
    if instruction[0] == 'y':
        dots = [dot for dot in dots if dot[1] < fold]
    else:
        dots = [dot for dot in dots if dot[0] < fold]

print(dots)

for i in range(100):
    for j in range(100):
        if [j,i] in dots:
            print('#', end='')
        else:
            print('.', end='')
    print()
