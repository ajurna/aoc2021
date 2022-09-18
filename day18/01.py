import re
from itertools import combinations, permutations
from typing import Tuple
from math import ceil


def explode(num: str) -> Tuple[str, bool]:
    depth = 0
    for idx in range(len(num)):
        if num[idx] == '[':
            depth += 1
        if num[idx] == ']':
            depth -= 1
        if depth > 4:
            end_idx = num.find(']', idx)
            possible_number = num[idx + 1:end_idx]
            if possible_number.count('[') == 0 and possible_number.count(']') == 0:
                first, second = [int(x) for x in possible_number.split(',')]
                try:
                    left_match = list(re.finditer(r'(\d+)', num[:idx]))[-1]
                except IndexError:
                    left_match = None
                try:
                    right_match = next(re.finditer(r'(\d+)', num[end_idx:]))
                except StopIteration:
                    right_match = None

                if right_match:
                    num = num[:right_match.start() + end_idx] + \
                        f'{int(right_match.group(0))+second}' + \
                          num[right_match.start() + end_idx + len(right_match.group(0)):]
                num = num[:idx] + '0' + num[end_idx + 1:]

                if left_match:
                    num = num[:left_match.start()] + f'{int(left_match.group(0)) + first}' + num[left_match.start() + len(
                        left_match.group(0)):]

                return num, True
            break
    return num, False


def split(num: str) -> Tuple[str, bool]:
    for match in re.finditer(r'\d{2,}', num):
        value = int(match.group(0))
        num = num[:match.start()]+f'[{value//2},{ceil(value/2)}]'+num[match.end():]
        return num, True
    return num, False


def process_number(num) -> str:
    processing = True
    while processing:
        num, exploded = explode(num)
        if exploded:
            continue
        num, has_split = split(num)
        if has_split:
            continue
        processing = False
    return num


def calculate_magnitude(num):
    if type(num[0]) is list:
        val_0 = calculate_magnitude(num[0])
    else:
        val_0 = num[0]
    if type(num[1]) is list:
        val_1 = calculate_magnitude(num[1])
    else:
        val_1 = num[1]
    val_0 *= 3
    val_1 *= 2
    return val_0 + val_1

with open('01.txt') as f:
    lines = [x.strip() for x in f.readlines()]

puzzle = lines.pop(0)
puzzle = process_number(puzzle)

while lines:
    puzzle = f'[{puzzle},{lines.pop(0)}]'
    puzzle = process_number(puzzle)
part_1 =  calculate_magnitude(eval(puzzle))
print(f'{part_1=}')

with open('01.txt') as f:
    lines = [x.strip() for x in f.readlines()]

part_2 = 0
for combo in permutations(lines, r=2):
    combo = f'[{combo[0]},{combo[1]}]'
    score = calculate_magnitude(eval(process_number(combo)))
    part_2 = max(part_2, score)

print(f'{part_2=}')