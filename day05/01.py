from dataclasses import dataclass
from parse import compile


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def diagonal(self):
        return not any([self.x1 == self.x2, self.y1 == self.y2])

    def line_path(self):
        points = []
        cur_x = self.x1
        cur_y = self.y1
        points.append((cur_x, cur_y))
        while cur_x != self.x2 or cur_y != self.y2:
            if cur_x < self.x2:
                cur_x += 1
            elif cur_x > self.x2:
                cur_x -= 1
            if cur_y < self.y2:
                cur_y += 1
            elif cur_y > self.y2:
                cur_y -= 1
            points.append((cur_x, cur_y))
        return points


parser = compile('{},{} -> {},{}')
lines = []
max_x = 0
max_y = 0
with open('01.txt') as f:
    for line in f.readlines():
        new_line = Line(*[int(x) for x in parser.parse(line.strip())])
        lines.append(new_line)
        max_x = max([max_x, new_line.x1, new_line.x2])
        max_y = max([max_y, new_line.y1, new_line.y2])
grid = [[0 for _ in range(max_x+1)]for _ in range(max_y+1)]

for line in lines:
    if not line.diagonal():
        for point in line.line_path():
            grid[point[1]][point[0]] += 1

print('Part 1:', sum([sum([1 for y in x if y > 1]) for x in grid]))


grid = [[0 for _ in range(max_x+1)]for _ in range(max_y+1)]

for line in lines:
    for point in line.line_path():
        grid[point[1]][point[0]] += 1

print('Part 2:', sum([sum([1 for y in x if y > 1]) for x in grid]))
