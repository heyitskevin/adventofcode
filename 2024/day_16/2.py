from heapq import heappop, heappush

def readfile():
    res = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            res.append(list(ln))

    return res

def get_start(grid):
    for ix, row in enumerate(grid):
        for cx, col in enumerate(row):
            if col == 'S':
                return ix, cx
    return -1, -1


def get_end(grid):
    for ix, row in enumerate(grid):
        for cx, col in enumerate(row):
            if col == 'E':
                return ix, cx
    return -1, -1


def main():
    grid = readfile()
    srow, scol = get_start(grid)
    erow, ecol = get_end(grid)
    # grid[srow][scol] = '.'
    grid[erow][ecol] = '.'

    # A Pile of Dijkstra's spaghet

    directions = [(0,1), (1,0), (0, -1), (-1, 0)]
    heap = [(0, 0, srow, scol, {(srow, scol)})] # score, direction, row, col, path
    visited = {}
    min_score = None
    paths = set()

    def is_visitable(direction, row, col, score):
        prev_score = visited.get((direction, row, col))
        if prev_score and prev_score < score:
            return False
        visited[(direction, row, col)] = score
        return True
    
    while heap:
        score, di, row, col, p = heappop(heap)
        if min_score and min_score < score:
            break
        if (row, col) == (erow, ecol):
            min_score = score
            paths |= p
        if not is_visitable(di, row, col, score):
            continue
        r = row + directions[di][0]
        c = col + directions[di][1]

        if grid[r][c] == '.' and is_visitable(di, r, c, score+1):
            heappush(
                heap, 
                (score + 1, di, r, c, p | {(r, c)})
            )
        ccw = (di - 1) % 4
        cw = (di + 1) % 4

        if is_visitable(ccw, row, col, score + 1000):
            heappush(
                heap,
                (score + 1000, ccw, row, col, p)
            )
        
        if is_visitable(cw, row, col, score + 1000):
            heappush(
                heap,
                (score + 1000, cw, row, col, p)
            )
    return len(paths)
    

print(main())
