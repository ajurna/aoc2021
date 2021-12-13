from typing import NamedTuple
from parse import compile
from itertools import zip_longest


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)


def print_grid(data):
    for line in data:
        print(''.join(map(lambda j: '#' if j == 1 else ' ', line)))


points = []
folds = []
max_x = 0
max_y = 0
parser = compile('fold along {}={}')
with open('01.txt') as f:
    file_data = f.readlines()
    while True:
        f_line = file_data.pop(0).strip()
        if not f_line:
            break
        x, y = [int(i) for i in f_line.split(',')]
        points.append(Point(x, y))
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    for f_line in file_data:
        axis, ind = parser.parse(f_line.strip())
        folds.append((axis, int(ind)))

grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for point in points:
    grid[point.y][point.x] = 1

for i, fold in enumerate(folds):
    fold_ind = fold[1]
    if fold[0] == 'y':
        top = grid[0:fold_ind]
        bottom = grid[fold_ind + 1:]
        fill = [0 for _ in range(len(top[0]))]
        grid = [[max(y) for y in zip_longest(*x)] for x in zip_longest(top[::-1], bottom, fillvalue=fill)][::-1]
    else:
        left = [x[0:fold_ind][::-1] for x in grid]
        right = [x[fold_ind + 1:] for x in grid]
        grid = [[max(y) for y in zip_longest(*x, fillvalue=0)][::-1] for x in zip_longest(left, right)]
    if i == 0:
        print('Part 1:', sum([sum(x) for x in grid]))

print('Part 2:')
print_grid(grid)
