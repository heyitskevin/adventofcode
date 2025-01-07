import sys
import copy

def readfile():
    res = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            res.append(list(ln))

    return res

def get_start(grid):
    for ix, row in enumerate(grid):
        for cx, col in enumerate(row):
            if col == 'S':
                return ix, cx
    return -1, -1


def get_end(grid):
    for ix, row in enumerate(grid):
        for cx, col in enumerate(row):
            if col == 'E':
                return ix, cx
    return -1, -1

def paths(grid, start_row, start_col):
    directions = [(0,1), (1, 0), (0, -1), (-1,0)]
    dist_matrix = [[-1 for _ in range(len(grid[0]))] for __ in range(len(grid))]

    for ix, row in enumerate(grid):
        for cix, col in enumerate(row):
            if grid[ix][cix] != '#':
                dist_matrix[ix][cix] = sys.maxsize
    
    q = [(start_row, start_col, 0, 0)]
    
    while q:
        r, c, d, s = q.pop(0) # row, col, direction, score
        if s < dist_matrix[r][c]:
            dist_matrix[r][c] = s
            cw = (d - 1) % 4
            ccw = (d + 1) % 4
            st = d

            next_candidates = [
                (r + directions[cw][0], c + directions[cw][1], cw, s + 1001),
                (r + directions[ccw][0], c + directions[ccw][1], ccw, s + 1001),
                (r + directions[st][0], c + directions[st][1], st, s + 1)
            ]

            for nc in next_candidates:
                if grid[nc[0]][nc[1]] != '#':
                    q.append(nc)
    er, ec = get_end(grid)
    return dist_matrix[er][ec]



def main():
    grid = readfile()
    srow, scol = get_start(grid)
    grid[srow][scol] = '.'
    return paths(grid, srow, scol)

print(main())