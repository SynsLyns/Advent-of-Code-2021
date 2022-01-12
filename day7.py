f = list(map(int, open("7.txt", "r").read().split(',')))

best_fuel = None
best_no = 0

for i in range(min(f) + 1, max(f) + 1):
    fuel = 0
    for j in f:
        fuel += abs(j - i)
    if best_fuel is None or fuel < best_fuel:
        best_fuel = fuel
        best_no = i

print("Part 1: " + str(best_fuel))

best_fuel = None
best_no = 0

for i in range(min(f) + 1, max(f) + 1):
    fuel = 0
    for j in f:
        fuel += int((abs(j-i)*(1+abs(j-i)))/2)
    if best_fuel is None or fuel < best_fuel:
        best_fuel = fuel
        best_no = i

print("Part 2: " + str(best_fuel))
