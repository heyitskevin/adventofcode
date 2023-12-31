FILENAME = 'input.txt'
import pprint
import sys
from heapq import heappop, heappush
import math
from collections import defaultdict

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

# def dijkstra(trails, start, end):
#     visited = set()
#     q = [(0, *start)]
#     dist_to_node = {start: 0}
#     height = len(trails)
#     width = len(trails[0])
#     directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # L R U D
#     while q:
#         cost, row, col = heappop(q)
#         cost = -1 * cost
#         if (row, col) == end:
#             return cost, dist_to_node
#         if (row, col) in visited:
#             continue
#         visited.add((row, col))
#         new_cost = cost + 1
#         for d in directions:
#             new_row = row + d[0]
#             new_col = col + d[1]
#             if new_row in range(height) and new_col in range(width) and trails[new_row][new_col] != '#':
#                 if new_cost > dist_to_node.get((new_row, new_col), -math.inf):
#                     dist_to_node[(new_row, new_col)] = new_cost
#                 heappush(q, (-1 * new_cost, new_row, new_col))


# def bfs(trails, start, end):
#     q = [(0, *start)]

#     height = len(trails)
#     width = len(trails[0])
#     directions = [ (0, 1), (1, 0), (0, -1), (-1, 0),] 
#     visited = set()
#     res = []
#     while q:
#         dist, row, col = q.pop(0)
#         if (row, col) == end:
#             res.append(dist)
#             continue
#         new_dist = dist + 1
#         if (row, col) in visited:
#             continue
#         visited.add((row, col))

#         for d in directions:
#             new_row = row + d[0]
#             new_col = col + d[1]
#             if new_row in range(height) and new_col in range(width) and trails[new_row][new_col] != '#':
#                 q.append((new_dist, new_row, new_col))
#     return res

def graph_solution(trails, start, end): # Help from Reddit, turns out longest path is an NP hard problem and that's 3 hard 5 me
    edges = defaultdict(set)
    height = len(trails)
    width = len(trails[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for r, row in enumerate(trails):
        for c, col in enumerate(row):
            if col != '#':
                for d1, d2 in directions:
                    new_row = r + d1
                    new_col = c + d2
                    if new_row in range(height) and new_col in range(width) and trails[new_row][new_col] != '#':
                        edges[(r, c)].add((new_row, new_col, 1)) # Row, col, distance cardinality to be used later
                        edges[(new_row, new_col)].add((r, c, 1)) # Build bidirectional graph
    while True: # Squash corridors until no corridors left
        for node, edge_set in edges.items(): 
            if len(edge_set) == 2: # We are in a corridor, squash
                e1, e2 = edge_set
                edges[e1[:2]].remove(node + (e1[2],))
                edges[e2[:2]].remove(node + (e2[2],))
                edges[e1[:2]].add((e2[0], e2[1], e1[2]+e2[2]))
                edges[e2[:2]].add((e1[0], e1[1], e1[2]+e2[2]))
                del edges[node]
                break
        else:
            break
    # Do search
    q = [(*start, 0)]
    visited = set()
    longest = 0
    while q:
        r, c, dist = q.pop()
        if dist == -1:
            visited.remove((r,c))
            continue
        if (r, c) == end:
            longest = max(longest, dist)
            continue
        if (r, c) in visited:
            continue
        visited.add((r,c))
        q.append((r, c, -1))
        for new_row, new_col, new_dist in edges[(r,c)]:
            q.append((new_row, new_col, new_dist + dist))
    print('dist', longest)


import time
def func(): 
    trails = read_file()
    start, end = get_start_and_end(trails)
    print(start, end)
    # c, dist = dijkstra(trails, start, end)
    graph_solution(trails, start, end)
    
    
start = time.time()
func()
end = time.time()
print('timing', end - start)

# 4346 too low