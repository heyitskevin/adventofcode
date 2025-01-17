import sys
from copy import deepcopy
from functools import cache

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def readfile():
    grid = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            a = []
            for c in ln:
                a.append(c)
            grid.append(a)

    return grid


def get_end(grid):
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == 'E':
                return i, j
    print("not found")
    raise Exception


def get_start(grid):
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == 'S':
                return i, j
    print("not found")
    raise Exception


def make_distance_matrix(grid, start):
    srow, scol = start

    dist_matrix = [[-1 for _ in range(len(grid[0]))] for __ in range(len(grid))]

    q = [(srow, scol, 0)]
    visited = set()

    while q:
        row, col, steps = q.pop(0)
        dist_matrix[row][col] = steps
        visited.add((row, col))

        for d in DIRS:
            r = row + d[0]
            c = col + d[1]

            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#':
                if (r, c) not in visited:
                    q.append((r, c, steps + 1))
    return dist_matrix, visited


def main():
    grid = readfile()
    # get the distance to the end at every point in the grid since there is only one route
    # take two steps in any direction and see if the distance new dist is >= 100
    start_row, start_col = get_start(grid)
    end_row, end_col = get_end(grid)
    dm, v = make_distance_matrix(grid, (end_row, end_col))
    cheats = set()
    assert dm[end_row][end_col] == 0
    assert dm[start_row][start_col] == len(v) - 1
    for r, c in v:
        for d1 in DIRS:
            for d2 in DIRS:
                nr = r + d1[0] + d2[0]
                nc = c + d1[1] + d2[1]
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    new_dist = dm[nr][nc]
                    if new_dist != -1 and dm[r][c] - new_dist > 100:
                        if ((nr, nc), (r,c)) not in cheats:
                            cheats.add(((r,c), (nr, nc)))
    
   
    return len(cheats)

print(main())