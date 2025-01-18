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


def make_coord_diffs(size):
    coords = set()
    for s in range(2, size + 1):
        for d in range(s + 1):
            coords.add((d, s - d))
            coords.add((-d, s - d))
            coords.add((d, -(s - d)))
            coords.add((-d, -(s - d)))
            
    return coords


def main():
    grid = readfile()
    # Same as part 1 except take 20 steps

    end_row, end_col = get_end(grid)
    dm, v = make_distance_matrix(grid, (end_row, end_col))
    cheats = set()
    
    diffs = make_coord_diffs(20)
    for row, col in v:
        for drow, dcol in diffs:
            nr = row + drow
            nc = col + dcol
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                new_dist = dm[nr][nc]
                # We subtract abs(drow) + abs(dcol) to account for options that don't net us a movement of more than 100 steps
                if new_dist != -1 and dm[row][col] - new_dist - (abs(drow) + abs(dcol)) >= 100:
                    cheats.add(((row, col), (nr, nc)))
                    

    
    return len(cheats)

print(main())
