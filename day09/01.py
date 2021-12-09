from collections import deque
from functools import reduce
from typing import NamedTuple

grid = []
with open('01.txt') as f:
    for line in f.readlines():
        grid.append([int(x) for x in line.strip()])


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other: "Point"):
        return Point(self.x + other.x, self.y + other.y)


directions = [Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0)]
max_y = len(grid)
max_x = len(grid[0])
low_points = []


def part1():
    total = 0
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            position = Point(x, y)
            neighbours = [position+p for p in directions
                          if 0 <= (position+p).x < max_x and 0 <= (position + p).y < max_y]
            if value < min([grid[p.y][p.x] for p in neighbours]):
                low_points.append(position)
                total += value + 1
    return total


print('Part 1:', part1())


def find_basin(starting_pos: Point):
    global grid
    queue = deque()
    queue.append(starting_pos)
    visited = set()
    while queue:
        cur_pos = queue.popleft()
        visited.add(cur_pos)
        neighbours = [cur_pos+p for p in directions if 0 <= (cur_pos+p).x < max_x and 0 <= (cur_pos + p).y < max_y]
        for neighbour in neighbours:
            if neighbour not in visited and grid[neighbour.y][neighbour.x] < 9:
                queue.append(neighbour)
    return len(visited)


basins = []
for low_point in low_points:
    basins.append(find_basin(low_point))

print('Part 2:', reduce(lambda x, y: x*y, sorted(basins)[-3:]))
