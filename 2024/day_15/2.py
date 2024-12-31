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

def double_grid(grid):
    dg = []
    for row in grid:
        dr = []
        for col in row:
            if col == '#':
                dr += ['#', '#']
            elif col == 'O':
                dr += ['[', ']']
            elif col == '.':
                dr += ['.', '.']
            elif col == '@':
                dr += ['@', '.']
        dg.append(dr)
    return dg


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
        direction = i.pop(0)
        dr, dc = lookup[direction]
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
            elif g[nr][nc] in '[]':
                # push
                # L/R push is just move each element up by one
                # U/D push is the same, just a different capture of elements
                if direction in '<>':
                    # horizontal
                    offset = 0
                    
                    hrow, hcol = nr, nc
                    while g[hrow][hcol] not in '[]':
                        hrow += dr
                        hcol += dc
                        offset += 1
                    if g[hrow][hcol] == '#':
                        # can't push
                        continue
                    elif g[hrow][hcol] == '.':
                        # room to push
                        new_row = copy.deepcopy(g[hrow])
                        if dc > 0:
                            # going right
                            slc = g[nc:hcol] 
                            for x in range(offset):
                                new_row[nc + x] = '.'
                            new_row = new_row[:nc + 1] + slc + new_row[hcol+1:]
                        else:
                            # going left
                            slc = g[hcol:nc]
                            for x in range(offset):
                                new_row[nc - x] = '.'
                            new_row = new_row[hcol - 1:] + slc + new_row[:nc - 1]
                        g[hrow] = new_row
                    row, col = nr, nc
                elif direction in 'v^':
                    # vertical
                    blocked = False
                    vrow, vcol = nr, nc
                    aboves = [[(vrow, vcol)]]
                    if g[vrow][vcol + 1] in '[]':
                        aboves[0].append((vrow, vcol+1))
                    else:
                        aboves[0].append((vrow, vcol-1))
                    while not blocked:
                        new_aboves = set()
                        for ab in aboves[-1]:
                            ab_row, ab_col = ab
                            if g[ab_row + dr][ab_col] in '[]':
                                new_aboves.add((ab_row + dr, ab_col))
                                if g[ab_row + dr][ab_col] == '[':
                                    new_aboves.add((ab_row + dr, ab_col + 1))
                                else:
                                    new_aboves.add((ab_row + dr, ab_col - 1))
                            elif g[ab_row + dr][ab_col] == '#':
                                blocked = True
                                break
                        if len(new_aboves) == 0:
                            break
                        else:
                            aboves.append(list(new_aboves))
                    # print(aboves)
                    if blocked:
                        continue
                    else:
                        for above_row in aboves[::-1]:
                            for shift in above_row:
                                shift_row, shift_col = shift
                                g[shift_row + dr][shift_col] = g[shift_row][shift_col]
                                g[shift_row][shift_col] = '.'
                    row, col = nr, nc
        # for ln in g:
        #     print(''.join(ln))
        # print('--------------')
    return g

def score(grid):
    s = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if grid[i][j] == '[':
                s += (100 * i) + j
    return s


def main():
    grid, inst = readfile()

    grid = [
        list("##########"),
        list("#..O..O.O#"),
        list("#......O.#"),
        list("#.OO..O.O#"),
        list("#..O...O.#"),
        list("#O#@.O...#"),
        list("#O..O..O.#"),
        list("#.OO.O.OO#"),
        list("#....O...#"),
        list("##########")
    ]

    inst = list("<^^>>>vv<v>>v<<")
    grid = double_grid(grid)
    fg = traverse(grid, inst)
    for ln in fg:
        print(''.join(ln))
    return score(fg)


 # Yoinked from reddit b/c im going insane
grid, moves = open('input.txt').read().split('\n\n')

for grid in grid, grid.translate(str.maketrans(
        {'#':'##', '.':'..', 'O':'[]', '@':'@.'})):

    grid = {i+j*1j:c for j,r in enumerate(grid.split())
                     for i,c in enumerate(r)}

    p, = [p for p in grid if grid[p] == '@']

    for m in moves.replace('\n', ''):
        d = {'<':-1, '>':+1, '^':-1j, 'v':+1j}[m]
        swap = []
        todo = [p]
        for t in todo:
            if grid[t] == '#': break
            if grid[t] == '.': continue
            t += d
            swap += [t]
            todo += [t]
            if d.imag and grid[t] == '[': todo += [t+1]
            if d.imag and grid[t] == ']': todo += [t-1]

        else:
            done = set()
            for s in swap[::-1]:
                if s in done: continue
                done.add(s)
                grid[s], grid[s-d] = grid[s-d], grid[s]
            p += d

    ans = sum(pos for pos in grid if grid[pos] in 'O[')
    print(int(ans.real + ans.imag*100))
