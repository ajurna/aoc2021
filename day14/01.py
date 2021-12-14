from collections import Counter, defaultdict
from functools import lru_cache
from operator import itemgetter
from typing import Dict

from parse import compile

parser = compile('{in} -> {out}')
trans = dict()
with open('01.txt') as f:
    initial = f.readline().strip()
    f.readline()
    for li in f.readlines():
        t = parser.parse(li.strip())
        trans[t['in']] = t['out']


@lru_cache(maxsize=None)
def poly_count(poly, depth) -> Dict:
    children = defaultdict(int)
    for i in range(len(poly)-1):
        new_p = trans[poly[i]+poly[i+1]]
        children[new_p] += 1
        if depth == 1:
            continue
        else:
            for k, v in poly_count(poly[i]+new_p+poly[i+1], depth-1).items():
                children[k] += v
    return children


count = defaultdict(int)
for k, v in Counter(initial).items():
    count[k] += v
for k, v in poly_count(initial, 10).items():
    count[k] += v
sorted_letters = sorted(count.items(), key=itemgetter(1))
print('Part 1:', sorted_letters[-1][1] - sorted_letters[0][1])

count = defaultdict(int)
for k, v in Counter(initial).items():
    count[k] += v
for k, v in poly_count(initial, 40).items():
    count[k] += v
sorted_letters = sorted(count.items(), key=itemgetter(1))
print('Part 2:', sorted_letters[-1][1] - sorted_letters[0][1])
