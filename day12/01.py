from collections import defaultdict, deque
from typing import Deque, Tuple, Dict, Set, Optional

caves: Dict[str, Set[str]] = defaultdict(set)
with open('01.txt') as f:
    for line in f.readlines():
        node_a, node_b = line.strip().split('-')
        caves[node_a].add(node_b)
        caves[node_b].add(node_a)


def find_routes_p1(grid: Dict[str, Set[str]]):
    routes = set()
    queue: Deque[Tuple[str, ...]] = deque()
    queue.append(('start',))
    while queue:
        route = queue.popleft()
        node = route[-1]
        for dest in grid[node]:
            next_route = (*route, dest)
            if dest == 'end':
                routes.add(next_route)
            elif dest.islower() and dest not in route:
                queue.append(next_route)
            elif dest.isupper():
                queue.append(next_route)
    return routes


def find_routes_p2(grid: Dict[str, Set[str]]):
    routes = set()
    queue: Deque[Tuple[Tuple[str, ...], Optional[str]]] = deque()
    queue.append((('start',), None))
    while queue:
        route, double = queue.popleft()
        node = route[-1]
        for dest in grid[node]:
            if dest == 'start':
                continue
            next_route = (*route, dest)
            if dest == 'end':
                routes.add(next_route)
            elif dest.islower() and dest in route and not double:
                queue.append((next_route, dest))
            elif dest.islower() and dest not in route:
                queue.append((next_route, double))
            elif dest.isupper():
                queue.append((next_route, double))
    return routes


result = find_routes_p1(caves)
print('Part 1:', len(result))
result = find_routes_p2(caves)
print('Part 2:', len(result))
