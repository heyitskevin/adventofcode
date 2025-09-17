def readfile():
    arr = []
    with open('input.txt') as f:
        for ln in f.readlines():
            arr.append(list(ln.rstrip('\n')))
    return arr


def get_positions(grid):
    pos = []
    id = 1
    dirs = ['<', '^', '>', 'v']
    for rix, row in enumerate(grid):
        for cix, elem in enumerate(row):
            if elem in dirs:
                pos.append((id, rix, cix, dirs.index(elem)))
                id += 1
    return pos

def is_collision(positions):
    if not positions:
        return True
    ps = [(r, c) for _, r, c, d in positions]
    v = set()
    for r, c in ps:
        if (r, c) in v:
            # print("POSOSSOSO", ps)
            return (r, c)
        v.add((r, c))
    return False
    

def main():
    grid = readfile()
    positions = get_positions(grid)
    # replace carts
    for _, r, c, d in  positions:
        elem = grid[r][c]
        if elem == '<' or elem == '>':
            grid[r][c] = '-'
        if elem == 'v' or elem == '^':
            grid[r][c] = '|'
    
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)] # L, U, R, D
    turns = {i: 0 for i, _, __, ___ in positions}
    positions = sorted(positions, key = lambda x: (x[1], x[2]))
    while True:
        # advance the position of every cart
        new_pos = []
        for curr_ix, v in enumerate(positions):
            i, r, c, d = v
            dr, dc = dirs[d]
            next_val = grid[r + dr][c + dc]
            if next_val == '/':
                if d == 0:
                    step = (i, r + dr, c + dc, 3)
                elif d == 1:
                    step = (i, r + dr, c + dc, 2)
                elif d == 2:
                    step = (i, r + dr, c + dc, 1)
                elif d == 3:
                    step = (i, r + dr, c + dc, 0)
            elif next_val == '\\':
                if d == 0:
                    step = (i, r + dr, c + dc, 1)
                elif d == 1:
                    step = (i, r + dr, c + dc, 0)
                elif d == 2:
                    step = (i, r + dr, c + dc, 3)
                elif d == 3:
                    step = (i, r + dr, c + dc, 2)
            elif next_val == '+':
                turns[i] += 1
                if turns[i] % 3 == 1: # Turn Left
                    step = (i, r + dr, c + dc, (d - 1) % 4)
                elif turns[i] % 3 == 2: # Straight
                    step = (i, r + dr, c + dc, d)
                else: # Turn Right
                    step = (i, r + dr, c + dc, (d + 1) % 4)
            else:
                step = (i, r + dr, c + dc, d)
            for np in sorted(new_pos, key=lambda x: (x[1], x[2])) + positions[curr_ix + 1:]:
                if np[1] == r + dr and np[2] == c + dc and np[0] != i:
                    
                    return step
            new_pos.append(step)
        positions = sorted(new_pos, key=lambda x: (x[1], x[2]))

print(main()) # R C needs to be flippe din answer to be X Y