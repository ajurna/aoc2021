import math

with open('01.txt') as f:
    initial_state = tuple([int(x) for x in f.read().strip().split(',')])

lowest_fuel_1 = math.inf
lowest_fuel_2 = math.inf

for pos in range(min(initial_state), max(initial_state)+1):
    fuel_used_1 = sum([abs(x - pos) for x in initial_state])
    fuel_used_2 = sum([sum([y for y in range(abs(x - pos)+1)]) for x in initial_state])
    lowest_fuel_1 = min(fuel_used_1, lowest_fuel_1)
    lowest_fuel_2 = min(fuel_used_2, lowest_fuel_2)

print('Part 1:', lowest_fuel_1)
print('Part 2:', lowest_fuel_2)