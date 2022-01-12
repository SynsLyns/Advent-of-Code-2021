fishes = list(map(int, open("6.txt", "r").read().split(',')))

for i in range(80):
    for j in range(len(fishes)):
        if fishes[j] == 0:
            fishes[j] = 6
            fishes.append(8)
        else:
            fishes[j] -= 1

print("Part 1: " + str(len(fishes)))

fishes = list(map(int, open("6.txt", "r").read().split(',')))

alt = [0]*9

for fish in fishes:
    alt[fish] += 1

for i in range(256):
    new_alt = [0]*9
    for j in range(len(alt)):
        if j == 0:
            new_alt[6] += alt[j]
            new_alt[8] += alt[j]

        else:
            new_alt[j-1] += alt[j]
    alt = new_alt.copy()


print("Part 2: " + str(sum(alt)))