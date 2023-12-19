FILENAME = 'input.txt'

import math
import itertools
from collections import defaultdict
from heapq import heappop, heappush

def read_file():
    with open(FILENAME) as f:
        return [[int(c) for c in ln] for ln in f.read().split('\n')]

def dijkstra(grid, start_row, start_col):
    # cost , row, col, prev direction
    q = [(0, start_row, start_col , -1)]
    visited = set()

    dist_to_node = {}
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        cost, row, col , pdir = heappop(q)
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return cost
        if (row, col, pdir) in visited:
            continue
        visited.add((row, col, pdir))
        for direction in range(4):
            if direction == pdir or (direction + 2) % 4 == pdir:
                continue
            cost_at_new_node = 0
            for step_dist in range(1,4):
                new_row = row + DIRECTIONS[direction][0] * step_dist
                new_col = col + DIRECTIONS[direction][1] * step_dist

                if new_row in range(0, len(grid)) and new_col in range(0, len(grid[0])):
                    cost_at_new_node += grid[new_row][new_col]
                    if step_dist < 1:
                        continue
                    candidate_cost = cost + cost_at_new_node
                    if dist_to_node.get((new_row, new_col, direction), math.inf) > candidate_cost:
                        dist_to_node[(new_row, new_col, direction)] = candidate_cost
                    heappush(q, (candidate_cost, new_row, new_col, direction))



def func():
    grid = read_file()
    d = dijkstra(grid, 0, 0)
    print(d)
    
func()
