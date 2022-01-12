f = open("14.txt", "r").read().splitlines()

initial = f[0]
rules_temp = [x.split(' -> ') for x in f[2:]]
rules = dict()
alpha = set([char for char in initial])

for rule in rules_temp:
    rules[rule[0]] = rule[1]

for i in range(10):
    temp = initial
    t_index = 0
    for index in range(1, len(initial)):
        t_index += 1
        if initial[index - 1:index + 1] in rules:
            temp = temp[:t_index] + rules[initial[index - 1:index + 1]] + temp[t_index:]
            alpha.add(rules[initial[index - 1:index + 1]])
            t_index += 1
    initial = temp

counts = []

for letter in alpha:
    counts.append(initial.count(letter))

print("Part 1: " + str(max(counts) - min(counts)))

initial = f[0]
occurrences = dict()

for index in range(1, len(initial)):
    if initial[index - 1:index + 1] not in occurrences:
        occurrences[initial[index - 1:index + 1]] = 1
    else:
        occurrences[initial[index - 1:index + 1]] += 1

for i in range(40):
    temp_occurrences = occurrences.copy()
    for key in occurrences:
        if occurrences[key] != 0:
            if key[0] + rules[key] not in temp_occurrences:
                temp_occurrences[key[0] + rules[key]] = occurrences[key]
            else:
                temp_occurrences[key[0] + rules[key]] += occurrences[key]
            if rules[key] + key[1] not in temp_occurrences:
                temp_occurrences[rules[key] + key[1]] = occurrences[key]
            else:
                temp_occurrences[rules[key] + key[1]] += occurrences[key]
        temp_occurrences[key] -= occurrences[key]
    occurrences = temp_occurrences.copy()

counts = []

for letter in alpha:
    count = 0
    for key in occurrences.keys():
        if letter in key:
            count += key.count(letter) * occurrences[key]
    if count % 2 != 0:
        counts.append(int(count/2) + 1)
    else:
        counts.append(int(count / 2))

print("Part 2: " + str(max(counts) - min(counts)))
