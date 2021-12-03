from parse import compile

parser = compile('{} {}')

position = 0
p1_depth = 0
p2_depth = 0
aim = 0
with open('01.txt') as f:
    for line in f.readlines():
        line = line.strip()
        direction, distance = parser.parse(line)
        match direction:
            case 'forward':
                position += int(distance)
                p2_depth += int(distance) * aim
            case 'down':
                p1_depth += int(distance)
                aim += int(distance)
            case 'up':
                p1_depth -= int(distance)
                aim -= int(distance)
print('Part 1:', position * p1_depth)
print('Part 2:', position * p2_depth)