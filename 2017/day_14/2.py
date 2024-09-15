FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return f.read().strip()

def hash(input_string: str):
    numbers = [i for i in range(256)]
    current_pos = 0
    skip = 0
    as_ascii = [ord(c) for c in input_string]
    as_ascii += [17, 31, 73, 47, 23]
    for _ in range(64):
        for l in as_ascii:
            if l > len(numbers):
                continue
            end = current_pos + l
            if end > len(numbers):
                sub = numbers[current_pos:] + numbers[:end - len(numbers)]
                sub = sub[::-1]
                
                numbers = numbers[:current_pos] + sub
                trunc = numbers[256:]
                numbers = trunc + numbers[len(trunc):256]
            else:
                sub = numbers[current_pos:end][::-1]
                numbers = numbers[:current_pos] + sub + numbers[end:]
            
            current_pos = (end + skip) % len(numbers)
            skip += 1
    hash = []
    for i in range(16):
        ix = i*16
        s = numbers[ix:ix+16]
        v = 0
        for j in s:
            v ^= j
        h = hex(v)[2:]
        if len(h) == 1:
            h = '0' + h
        hash.append(h)
    return ''.join(hash)

def islands(grid):
    if not grid:
        return 0
    isl = 0
    def dfs(g, row, col):
        if row < 0 or col < 0 or row >= len(g) or col >= len(g[0]) or g[row][col] != '1':
            return
        g[row][col] = 'x'
        dfs(g, row-1, col)
        dfs(g, row+1, col)
        dfs(g, row, col-1)
        dfs(g, row, col+1)

    for r in range(len(grid)):
        for c in range((len(grid[0]))):
            if grid[r][c] == '1':
                isl += 1
                dfs(grid, r, c)
    return isl

import sys
sys.setrecursionlimit(10000000)

def func():
    start = readfile() 
    res = 0
    b = []
    for r in range(128):
        h = f'{start}-{r}'
        o = hash(h)
        bs = ''
        for cc in o:
            bb = bin(int(cc, 16))[2:]
            if len(bb) < 4:
                for _ in range(4- len(bb)):
                    bb = '0' + bb
            bs += bb
        b.append(list(bs))
    return islands(b)

print(func())
