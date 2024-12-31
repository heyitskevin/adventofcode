import copy

def readfile():
    grid, instructions = [], []

    with open('input.txt') as f:
        g, i = f.read().split('\n\n')
        for gg in g.split('\n'):
            grid.append(list(gg))
        
        for ii in i.split('\n'):
            for c in ii:
                instructions.append(c)
    return grid, instructions

def get_robot(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == '@':
                return (i, j)
    return (-1, -1)


def traverse(grid, inst):
    # Just feel like keeping a copy of the grid for reasons idk
    g = copy.deepcopy(grid)
    i = copy.deepcopy(inst)

    lookup = {
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0)
    }
    row, col = get_robot(g)
    g[row][col] = '.' # remove the robot from the grid so we can move around
    while i:
        dr, dc = lookup[i.pop(0)]
        nr, nc = row + dr, col + dc
        # attempt to move
        if 0 <= nr < len(g) and 0 <= nc < len(g[0]):
            # in range
            if g[nr][nc] == '.':
                # basic move
                row, col = nr, nc
            elif g[nr][nc] == '#':
                # wall
                continue
            elif g[nr][nc] == 'O':
                # a push is just updating the current element to . and the last element + 1 to O
                push_row, push_col = nr, nc
                while 0 <= push_row < len(g) and 0 <= push_col < len(g[0]) and g[push_row][push_col] == 'O':
                    push_row += dr
                    push_col += dc
                if g[push_row][push_col] == '.':
                    # open space
                    g[push_row][push_col] = 'O'
                    g[nr][nc] = '.'
                    row = nr
                    col = nc
                else: # we know it's a wall in this case
                    continue
    return g


def score(grid):
    s = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] == 'O':
                s += (100 * i) + j
    return s



def main():
    grid, inst = readfile()

    final_grid = traverse(grid, inst)
    return score(final_grid)


print(main())