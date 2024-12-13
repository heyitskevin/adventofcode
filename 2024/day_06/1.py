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
            

def main():
    grid = readfile()
    steps = set()
    row, col = get_start_row_col(grid)
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_dir = 0
    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        # visit current
        steps.add((row, col))
        next_r, next_c = row + dirs[curr_dir][0], col + dirs[curr_dir][1]
        if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]) and grid[next_r][next_c] == '#':
            # turn
            curr_dir = (curr_dir + 1) % 4
            next_r, next_c = row + dirs[curr_dir][0], col + dirs[curr_dir][1]
        row, col = next_r, next_c
    return len(steps)



print(main())