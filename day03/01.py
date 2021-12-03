from collections import Counter

data = []
with open('01.txt') as f:
    for line in f.readlines():
        data.append(line.strip())

freq = [Counter(x) for x in zip(*data)]
gamma = ''
epsilon = ''
for fr in freq:
    if fr['0'] > fr['1']:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print('Part 1:', int(gamma, base=2) * int(epsilon, base=2))


def oxygen_filter(grid, bit):
    freqs = [Counter(x) for x in zip(*grid)][bit]
    if freqs['1'] >= freqs['0']:
        bit_to_filter = '1'
    else:
        bit_to_filter = '0'
    return list(filter(lambda x: x[bit] == bit_to_filter, grid))


def co2_filter(grid, bit):
    freqs = [Counter(x) for x in zip(*grid)][bit]
    if freqs['0'] <= freqs['1']:
        bit_to_filter = '0'
    else:
        bit_to_filter = '1'
    return list(filter(lambda x: x[bit] == bit_to_filter, grid))


OG_data = data.copy()
CO_data = data.copy()
data_width = len(data[0])
current_bit = 0
while True:
    OG_data = oxygen_filter(OG_data, current_bit)
    if len(OG_data) == 1:
        break
    current_bit += 1
    if not current_bit < data_width:
        current_bit = 0
current_bit = 0
while True:
    CO_data = co2_filter(CO_data, current_bit)
    if len(CO_data) == 1:
        break
    current_bit += 1
    if not current_bit < data_width:
        current_bit = 0

print('Part 2:', int(OG_data[0], base=2) * int(CO_data[0], base=2))