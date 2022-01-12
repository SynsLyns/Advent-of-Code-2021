f = open("8.txt", "r").read().splitlines()

f = [i.split('|') for i in f]
f = [[j.split() for j in i] for i in f]

special = [2, 3, 4, 7]
total = 0

for output in f:
    for single in output[1]:
        if len(single) in special:
            total += 1

print("Part 1: " + str(total))

places = [0, 1, 3, 4, 6]
assign = {2 : "1",
          3 : "7",
          4 : "4",
          7 : "8"}
total = 0

for output in f:
    orientation = [[]] * 7
    for single in output[0]:
        if len(single) == 2:
            orientation[2] = [char for char in single]
            orientation[5] = [char for char in single]
        elif len(single) == 3:
            orientation[0] = [char for char in single]
        elif len(single) == 4:
            orientation[1] = [char for char in single]
            orientation[3] = [char for char in single]
        elif len(single) == 7:
            orientation[4] = [char for char in single]
            orientation[6] = [char for char in single]

    for place in places:
        new_list = []
        if place == 4 or place == 6:
            for char in orientation[place]:
                if char not in orientation[3] and char not in orientation[0] and char not in orientation[2] :
                    new_list.append(char)
            orientation[place] = new_list.copy()
        else:
            for char in orientation[place]:
                if char not in orientation[2]:
                    new_list.append(char)
            orientation[place] = new_list.copy()

    word = []
    for letter in output[1]:
        letter = [char for char in letter]
        if len(letter) in assign:
            word.append(assign[len(letter)])
        elif len([x for x in orientation[2] if x not in letter]) == 1:
            if len([x for x in orientation[4] if x not in letter]) == 1:
                word.append('5')
            else:
                if len([x for x in orientation[1] if x not in letter]) == 1:
                    word.append('2')
                else:
                    word.append('6')
        elif len([x for x in orientation[1] if x not in letter]) == 1:
            if len([x for x in orientation[4] if x not in letter]) == 1:
                word.append('3')
            else:
                word.append('0')
        else:
            word.append('9')
    total += int(''.join(word))

print("Part 2: " + str(total))
