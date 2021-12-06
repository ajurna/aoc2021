from collections import defaultdict

fish = defaultdict(int)
with open('01.txt') as f:
    for x in f.read().strip().split(','):
        fish[int(x)] += 1

day_80 = False
for x in range(256):
    new_fish = defaultdict(int)
    for timer, count in fish.items():
        if timer == 0:
            new_fish[8] = count
            new_fish[6] += count
        else:
            new_fish[timer-1] += count
    fish = new_fish
    if x == 79:
        day_80 = sum(fish.values())

print('Part 1:', day_80)
print('Part 2:', sum(fish.values()))
