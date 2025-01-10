def readfile():
    b = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            i, j = ln.strip().split(',')
            b.append((int(i), int(j)))
    return b


def main():
    height = 71
    width = 71
    bytes = readfile()

    grid = [['.' for _ in range(width)] for __ in range(height)]
    for k in range(1024):
        r, c = bytes[k]
        grid[c][r] = '#'

    # BFS
    
    q = [(0, 0, 0)]
    visited = set()
    final = set()
    directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
    while q:
        row, col, steps = q.pop(0)
        if (row, col) in visited:
            continue
        else:
            visited.add((row, col))
            
            if row == 70 and col == 70:
                final.add(steps)
                continue
            steps += 1
            for d in directions:
                x, y = d
                r = row + x
                c = col + y
                if 0 <= r < height and 0 <= c < width:
                    if grid[r][c] != '#':
                        q.append((r, c, steps))
            
    return min(final)

print(main())
