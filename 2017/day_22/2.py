FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return [list(ln.strip()) for ln in f.read().split('\n')]


def pad_array(arr, N):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0

    new_rows = rows + 2 * N
    new_cols = cols + 2 * N
    
    padded_array = [['.'] * new_cols for _ in range(new_rows)]
    
    for i in range(rows):
        for j in range(cols):
            padded_array[i + N][j + N] = arr[i][j]
    
    return padded_array

def pprint_grid(grid):
    print("\n".join(["".join(ln) for ln in grid]))

def func():
    grid = readfile()
    grid = pad_array(grid, 5000)
    count = 0

    r = len(grid) // 2
    c = len(grid[0]) // 2
    steps = 10000000
    # [l, u, r, d]
    directions = [(0, -1), (-1 , 0), (0, 1), (1, 0)]
    current_dir = 1
    for _ in range(steps):
        # pprint_grid(grid)
        node = grid[r][c]
        if node == '.':
            current_dir = (current_dir - 1) % 4
            grid[r][c] = 'W'
        elif node == 'W':
            grid[r][c] = '#'
            count += 1
        elif node == '#':
            grid[r][c] = 'F'
            current_dir = (current_dir + 1) % 4
        elif node == 'F':
            grid[r][c] = '.'
            current_dir = (current_dir + 2) % 4
        
        d = directions[current_dir] 
        r += d[0]
        c += d[1]
        # print('--------')
    return count

print(func())