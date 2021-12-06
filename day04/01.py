from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class BingoCard:
    line_1: List[int]
    line_2: List[int]
    line_3: List[int]
    line_4: List[int]
    line_5: List[int]
    index: Dict[int, int] = field(default_factory=dict)
    key: List[List[bool]] = field(default_factory=lambda: [[False for _ in range(5)] for _ in range(5)])
    lines: List[List[int]] = field(default_factory=list)

    def __post_init__(self):
        self.lines = [self.line_1, self.line_2, self.line_3, self.line_4, self.line_5]
        for i, line in enumerate(self.lines):
            for c in line:
                self.index[c] = i

    def call_number(self, num: int):
        if num in self.index:
            line = self.index[num]
            self.key[line][self.lines[line].index(num)] = True

    def check_winner(self):
        horizontal_lines = [all(x) for x in self.key]
        if any(horizontal_lines):
            return self
        vertical_lines = [all(x) for x in zip(*self.key)]
        if any(vertical_lines):
            return self
        return False

    def unmarked_sum(self):
        total = 0
        for n_line, k_line in zip(self.lines, self.key):
            total += sum([x for x, y in zip(n_line, k_line) if not y])
        return total


cards = []
with open('01.txt') as f:
    numbers = [int(x) for x in f.readline().strip().split(',')]
    input_data = f.readlines()
    while input_data:
        input_data.pop(0)
        cards.append(BingoCard(*[[int(x) for x in input_data.pop(0).strip().split()] for _ in range(5)]))

part_1 = False
last_winners = []
while numbers:
    number = numbers.pop(0)
    for card in cards:
        card.call_number(number)
    winners = [x.check_winner() for x in cards]
    if not part_1 and any(winners):
        winner = [x for x in winners if x][0]
        print('Part 1:', winner.unmarked_sum() * number)
        part_1 = True
    if all(winners):
        winner = [x for x in winners if x not in last_winners][0]
        print('Part 2:', winner.unmarked_sum() * number)
        break
    last_winners = winners
