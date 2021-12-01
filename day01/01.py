with open('01.txt') as f:
    data = list(map(int, map(str.strip, f.readlines())))

depth = data[0]
increases = 0
for d in data:
    if d > depth:
        increases += 1
    depth = d
print('Part 1:', increases)

increases = 0
for i in range(len(data)-3):
    first_num = data[i] + data[i+1] + data[i+2]
    second_num = data[i+1] + data[i+2] + data[i+3]
    if second_num > first_num:
        increases += 1
print('Part 2:', increases)
