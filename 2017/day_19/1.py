FILENAME = 'input.txt'

def readfile():
    res = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            res.append(list(ln))

    return res

def get_start(grid):
    for ix, i in enumerate(grid[0]):
        if i != ' ':
            return 0, ix

def is_end(grid, r, c, direction):
    if direction == 'u':
        if r > 0 and grid[r-1][c] != ' ':
            return False, 'u', r - 1 , c
        if c > 0 and grid[r][c-1] != ' ':
            return False, 'l', r, c - 1
        if c < len(grid[0]) - 1 and grid[r][c+1]  != ' ':
            return False, 'r', r, c + 1
        return True, -1, -1, -1
    if direction == 'd':
        if r < len(grid) - 1 and grid[r+1][c] != ' ':
            return False, 'd', r + 1, c
        if c > 0 and grid[r][c-1] != ' ':
            return False, 'l', r, c - 1
        if c < len(grid[0]) - 1 and grid[r][c+1]  != ' ':
            return False, 'r', r, c + 1
        return True, -1, -1, -1
    if direction == 'l':
        if c > 0 and grid[r][c-1] != ' ':
            return False, 'l', r, c - 1
        if r > 0 and grid[r-1][c] != ' ':
            return False, 'u', r - 1, c
        if r < len(grid) - 1 and grid[r+1][c] != ' ':
            return False, 'd', r + 1, c
        return True, -1, -1, -1
    if direction == 'r':
        if c < len(grid[0]) - 1 and grid[r][c+1] != ' ':
            return False , 'r', r, c + 1
        if r > 0 and grid[r-1][c] != ' ':
            return False, 'u', r - 1, c
        if r < len(grid) - 1 and grid[r+1][c] != ' ':
            return False, 'd', r + 1, c
        return True, -1, -1, -1

def func():
    grid = readfile()
    r, c = get_start(grid)
    direction = 'd'
    letters = []
    while True:
        if grid[r][c].isalpha():
            letters.append(grid[r][c])
        e, d, nr, nc = is_end(grid, r, c, direction)
        if e:
            break
        else:
            r = nr
            c = nc
            direction = d

    return ''.join(letters)

print(func())
        
