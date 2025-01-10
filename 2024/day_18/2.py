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
    
    
    directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
    # Brute force babyyyy
    # There's a memoization strat in here somewhere
    for node in bytes[1024:]:
        nodex, nodey = node
        grid[nodey][nodex] = '#'

        q = [(0,0)]
        visited = set()

        while q:
            row, col = q.pop(0)
            if (row, col) in visited:
                continue
            else:
                visited.add((row, col))
                for d in directions:
                    x, y = d
                    r = row + x
                    c = col + y
                    if 0 <= r < height and 0 <= c < width:
                        if grid[r][c] != '#':
                            q.append((r, c))
        if (70, 70) not in visited:
            return (nodex, nodey)


print(main())
