from collections import defaultdict
from dataclasses import dataclass, field
from typing import Set

count = 0
lines = []
with open('01.txt') as file:
    for line in file.readlines():
        line = line.strip()
        lines.append(line)
        line = line.split(' | ')
        count += sum([1 for x in line[1].split() if len(x) in [2, 4, 3, 7]])
print('Part 1:', count)

wires = ('a', 'b', 'c', 'd', 'e', 'f', 'g')


@dataclass
class Wiring:
    a: Set[str] = field(default_factory=lambda: set(wires))
    b: Set[str] = field(default_factory=lambda: set(wires))
    c: Set[str] = field(default_factory=lambda: set(wires))
    d: Set[str] = field(default_factory=lambda: set(wires))
    e: Set[str] = field(default_factory=lambda: set(wires))
    f: Set[str] = field(default_factory=lambda: set(wires))
    g: Set[str] = field(default_factory=lambda: set(wires))

    def set_one(self, one: Set):
        for segment in [self.a, self.b, self.d, self.e, self.g]:
            segment -= one
        self.c = self.c.intersection(one)
        self.f = self.f.intersection(one)

    def set_seven(self, seven: Set):
        for segment in [self.b, self.d, self.e, self.g]:
            segment -= seven
        self.a = self.a.intersection(seven)
        self.c = self.c.intersection(seven)
        self.f = self.c.intersection(seven)

    def set_four(self, four: Set):
        for segment in [self.a, self.e, self.g]:
            segment -= four
        self.b = self.b.intersection(four)
        self.c = self.c.intersection(four)
        self.d = self.d.intersection(four)
        self.f = self.f.intersection(four)

    def set_three(self, three: Set):
        for segment in [self.b, self.e]:
            segment -= three
        self.a = self.a.intersection(three)
        self.c = self.c.intersection(three)
        self.d = self.d.intersection(three)
        self.f = self.c.intersection(three)
        self.g = self.g.intersection(three)

    def set_six(self, six: Set):
        self.c -= six
        self.f = self.f.intersection(six)

    def get_dictionary(self):
        a = next(iter(self.a))
        b = next(iter(self.b))
        c = next(iter(self.c))
        d = next(iter(self.d))
        e = next(iter(self.e))
        f = next(iter(self.f))
        g = next(iter(self.g))

        return {
            ''.join(sorted([a, b, c, e, f, g])): 0,
            ''.join(sorted([c, f])): 1,
            ''.join(sorted([a, c, d, e, g])): 2,
            ''.join(sorted([a, c, d, f, g])): 3,
            ''.join(sorted([b, c, d, f])): 4,
            ''.join(sorted([a, b, d, f, g])): 5,
            ''.join(sorted([a, b, d, e, f, g])): 6,
            ''.join(sorted([a, c, f])): 7,
            ''.join(sorted([a, b, c, d, e, f, g])): 8,
            ''.join(sorted([a, b, c, d, f, g])): 9,
        }


total = 0
for line in lines:
    inp, out = line.split(' | ')
    data = inp.split()
    data.extend(out.split())
    wiring = Wiring()
    line_by_length = defaultdict(list)
    for item in data:
        line_by_length[len(item)].append(set(item))

    wiring.set_one(line_by_length[2][0])
    wiring.set_seven(line_by_length[3][0])
    wiring.set_four(line_by_length[4][0])

    possible_three = wiring.a | wiring.c | wiring.f
    for five_len in line_by_length[5]:
        if possible_three.issubset(five_len):
            wiring.set_three(five_len)
            break

    possible_six = wiring.c | wiring.f
    for six_len in line_by_length[6]:
        if not possible_six.issubset(six_len):
            wiring.set_six(six_len)

    wiring_dict = wiring.get_dictionary()
    result = [wiring_dict[''.join(sorted(x))] for x in data]
    total += int(''.join(map(str, result[-4:])))

print('Part 2:', total)
