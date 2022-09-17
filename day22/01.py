from typing import NamedTuple

from parse import compile


class Action(NamedTuple):
    action: str
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    min_z: int
    max_z: int

    def sub_cubes(self):
        return set([Cube(x, y, z)
                    for x in range(self.min_x, self.max_x + 1)
                    for y in range(self.min_y, self.max_y + 1)
                    for z in range(self.min_z, self.max_z + 1)])


parser = compile('{} x={}..{},y={}..{},z={}..{}')
actions = []
with open('01.txt') as f:
    for line in f.readlines():
        parsed = parser.parse(line.strip())
        actions.append(Action(parsed[0], *map(int, parsed[1:])))


class Cube(NamedTuple):
    x: int
    y: int
    z: int


on_cubes = set()
for action in actions:
    if not -50 <= action.min_x <= 50:
        continue

    if action.action == 'on':
        on_cubes.update(action.sub_cubes())
    else:
        on_cubes -= action.sub_cubes()
print(len(on_cubes))
