FILENAME = 'input.txt'

def rotate_pattern(pattern):
    p = [list(ln) for ln in pattern.split('/')]
    res = [[0 for _ in p[0]] for r in p]
    # row R becomes col of size - R
    for rix in range(len(p)):
        for cix in range(len(p[0])):
            res[cix][len(p) - rix - 1] = p[rix][cix]
    return '/'.join([''.join(ln) for ln in res])


def flip_horiz(pattern):
    return '/'.join([ln[::-1] for ln in pattern.split('/')])

def flip_vert(pattern):
    return '/'.join(pattern.split('/')[::-1])

def all_options(pattern):
    res = [pattern, flip_horiz(pattern), flip_vert(pattern)]

    for _ in range(3):
        pattern = rotate_pattern(pattern)
        res.append(pattern)
        res.append(flip_horiz(pattern))
        res.append(flip_vert(pattern))

    return list(set(res)) # Dedupe
    

def readfile():
    lookup = {}
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            k, v = ln.split(' => ')
            lookup[k.strip()] = v.strip()
    return lookup


def chunk(string_grid, chunk_size, lookup):
    chunks = []
    ng = []
    rows = string_grid.split('/')
    
    for cr in range(0, len(rows), chunk_size):
        for chunk_start in range(0, len(rows), chunk_size):
            cgr = [i[chunk_start:chunk_start+chunk_size] for i in rows[cr:cr+chunk_size]] 
            chunks.append('/'.join(cgr))
    
    for ch in chunks:
        options = all_options(ch)
        for o in options:
            if o in lookup:
                new_chunk = lookup[o]
                break
        ng.append(new_chunk)
        
    flat = []
    slc = len(rows) // chunk_size   
    for new_chunk_start in range(0, len(ng), slc):
        p = [ln.split('/') for ln in ng[new_chunk_start:new_chunk_start + slc]]
        
        for ix in range(len(p[0])):
            r = ""
            for block in p:
                r += block[ix]
            flat.append(r)
    
    return "/".join(flat)


def func():
    lookup = readfile()
    string_grid = ".#./..#/###"
    for _ in range(18):
        as_grid = [list(ln) for ln in string_grid.split('/')]
        size = len(as_grid)
        if size % 2 == 0:
            new_string = chunk(string_grid, 2, lookup)
        elif size % 3 == 0:
            new_string = chunk(string_grid, 3, lookup)
        string_grid = new_string
    ct = 0
    for chr in string_grid:
        if chr == '#':
            ct += 1
    return ct
print(func())