import copy
def readfile():
    a = []
    with open ('input.txt') as f:
        for ln in f.read().split('\n'):
            a.append(list(ln.strip()))
    return a

def get_start_row_col(grid):
    for ix, row in enumerate(grid):
        for cix, col in enumerate(row):
            if col == '^':
                return ix, cix
            
    return -1, -1
            

def next_step(r, c, curr_dir):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return r + dirs[curr_dir][0], c + dirs[curr_dir][1]


def test_loop(r, c, curr_dir, o_r, o_c, base_grid):
    history = {}
    width = len(base_grid)
    height = len(base_grid[0])
    while True:
        n_r, n_c = next_step(r, c, curr_dir)
        if not (0 <= n_r < width and 0 <= n_c < height):
            return False
        if base_grid[n_r][n_c] == '#' or (n_r, n_c) == (o_r, o_c):
            curr_dir = (curr_dir + 1) % 4
            continue
        if (n_r, n_c) in history and curr_dir in history[(n_r, n_c)]:
            return history
        r, c = n_r, n_c
        if (n_r, n_c) in history:
            history[(n_r, n_c)].append(curr_dir)
        else:
            history[(n_r, n_c)] = [curr_dir]


def main():
    base_grid = readfile()
    width = len(base_grid)
    height = len(base_grid[0])
    row, col = get_start_row_col(base_grid)
    curr_dir = 0

    result = set()
    visited = set()
    while True:
        n_r, n_c = next_step(row, col, curr_dir)
        if not (0 <= n_r < width and 0 <= n_c < height):
            break
        if base_grid[n_r][n_c] == '#':
            curr_dir = (curr_dir + 1) % 4
            continue
        test_obstacle = (n_r, n_c)

        if (test_obstacle not in result) and (test_obstacle != get_start_row_col(base_grid)) and (test_obstacle not in visited):
            loop = test_loop(row, col, curr_dir, n_r, n_c, base_grid)
            if loop:
                result.add(test_obstacle)
        row, col = n_r, n_c
        visited.add((row, col))

    return len(result)


print(main())