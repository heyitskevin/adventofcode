FILENAME = 'example.txt'
import pprint
import sys
from heapq import heappop, heappush
import math

def read_file():
    with open(FILENAME) as f:
        return [list(ln.strip()) for ln in f.read().split('\n')]
    
def get_start_and_end(trails):
    start_row = trails[0]
    end_row = trails[-1]
    
    for ix, e in enumerate(start_row):
        if e == '.':
            start_ix = ix
            break
    for ix, e in enumerate(end_row):
        if e == '.':
            end_ix = ix
            break
    return (0, start_ix), (len(trails) - 1, end_ix)

def dijkstra(trails, start, end):
    visited = set()
    q = [(0, *start)]
    dist_to_node = {start: 0}
    height = len(trails)
    width = len(trails[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # L R U D
    while q:
        cost, row, col = heappop(q)
        cost = -1 * cost
        if (row, col) == end:
            return cost, dist_to_node
        if (row, col) in visited:
            continue
        visited.add((row, col))
        new_cost = cost + 1
        for d in directions:
            new_row = row + d[0]
            new_col = col + d[1]
            if new_row in range(height) and new_col in range(width) and trails[new_row][new_col] != '#':
                if new_cost > dist_to_node.get((new_row, new_col), -math.inf):
                    dist_to_node[(new_row, new_col)] = new_cost
                heappush(q, (-1 * new_cost, new_row, new_col))


def bfs(trails, start, end):
    q = [(0, *start)]

    height = len(trails)
    width = len(trails[0])
    directions = [ (0, 1), (1, 0), (0, -1), (-1, 0),] 
    visited = set()
    res = []
    while q:
        dist, row, col = q.pop(0)
        if (row, col) == end:
            res.append(dist)
            continue
        new_dist = dist + 1
        if (row, col) in visited:
            continue
        visited.add((row, col))

        for d in directions:
            new_row = row + d[0]
            new_col = col + d[1]
            if new_row in range(height) and new_col in range(width) and trails[new_row][new_col] != '#':
                q.append((new_dist, new_row, new_col))
    return res


def func(): 
    trails = read_file()
    start, end = get_start_and_end(trails)
    print(start, end)
    # c, dist = dijkstra(trails, start, end)
    dist = bfs(trails, start, end)
    pprint.pprint(dist)
    

func()

# 4346 too low