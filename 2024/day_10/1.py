def readfile():
    res = []
    with open("input.txt") as f:
        for ln in f.read().split('\n'):
            res.append(list(ln.strip()))
    
    return res

def trailheads(grid):
    th = []
    for ix, row in enumerate(grid):
        for yx, col in enumerate(row):
            if col == '0':
                th.append((ix, yx))
    return th

def traverse(grid, start_row, start_col):
    dirs = [(-1, 0), (1, 0), (0, -1),  (0, 1)] # up, down, left, right
    score = set()
    q = [(start_row, start_col)]
    height = len(grid)
    width = len(grid[0])
    while q:
        row, col  = q.pop(0)
        val = grid[row][col]
        if val == '9':
            score.add((row, col))
            continue
        else:
            next_val = str(int(val) + 1)
            for d in dirs:
                dy, dx = d
                d_r = row + dy
                d_c = col + dx
                if 0 <= d_r < height and 0 <= d_c < width and grid[d_r][d_c] == next_val:
                    q.append((d_r, d_c))
    
    return len(score)


def main():
    grid = readfile()
    tr = trailheads(grid)
    res = 0
    for t in tr:
        r, c = t
        res += traverse(grid, r, c)
    return res

print(main())
