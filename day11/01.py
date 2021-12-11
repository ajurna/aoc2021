import math
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)

    def neighbours(self, max_x=math.inf, max_y=math.inf):
        # directions = [Point(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
        directions = (Point(x=-1, y=-1), Point(x=-1, y=0), Point(x=-1, y=1), Point(x=0, y=-1), Point(x=0, y=1),
                      Point(x=1, y=-1), Point(x=1, y=0), Point(x=1, y=1))
        return (self + p for p in directions if 0 <= (self + p).x < max_x and 0 <= (self + p).y < max_y)


grid = []
with open('01.txt') as f:
    for line in f.readlines():
        grid.append([int(x) for x in line.strip()])


def print_grid(g):
    for row in g:
        print(''.join(map(str, row)))
    print()


width = 10
height = 10

flash_count = 0
iteration = 0
while sum([sum(k) for k in grid]) != 0:
    iteration += 1
    grid = [[p + 1 for p in row] for row in grid]
    flashed = set()
    while max([max(j) for j in grid]) > 9:

        for y in range(height):
            for x in range(width):
                point = Point(x, y)
                if point in flashed:
                    continue
                if grid[point.y][point.x] > 9:
                    flashed.add(point)
                    grid[point.y][point.x] = 0
                    for neighbour in point.neighbours(width, height):
                        if neighbour not in flashed:
                            grid[neighbour.y][neighbour.x] += 1
    flash_count += len(flashed)
    if iteration == 100:
        print('Part 1:', flash_count)

print('Part 2:', iteration)
