FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [list(ln.strip()) for ln in f]
    
def expand_universe(universe, emptys):
    new_universe = []
    empty_row_indexes, empty_col_indexes = emptys
    # print(emptys)
    for ix, row in enumerate(universe): 
        new_row = []
        for col_ix, col in enumerate(row):
            if col_ix in empty_col_indexes:
                new_row.append('.')
            new_row.append(col)
        if ix in empty_row_indexes: # Expand rows
            new_universe.append(new_row)
        new_universe.append(new_row)

    return new_universe

def find_galaxies(universe):
    galaxies = []
    for r_ix, row in enumerate(universe):
        for c_ix, col in enumerate(row):
            if col == '#':
                galaxies.append((r_ix, c_ix))
    return galaxies

def get_empty_rows_and_cols(universe):
    empty_rows = []
    empty_cols = []
    for r_ix, row in enumerate(universe):
        if all([r == '.' for r in row]):
            empty_rows.append(r_ix)
    for ix in range(len(universe[0])):
        is_ix_empty = True
        for row in universe:
            if row[ix] != '.':
                is_ix_empty = False
        if is_ix_empty:
            empty_cols.append(ix)
    return empty_rows, empty_cols

def make_pairs(galaxies):
    from itertools import combinations
    combos = combinations(galaxies, 2)
    return list(combos)

def taxicab_geometry(pairs):
    geos = []
    gmap = {}
    for p in pairs:
        start, end = p
        taxi_dist = abs(end[0] - start[0]) + abs(end[1] - start[1])
        geos.append(taxi_dist)
        gmap[p] = taxi_dist
    return geos, gmap

def func():
    u = read_file()
    emptys = get_empty_rows_and_cols(u)
    e_u = expand_universe(u, emptys)
    g = find_galaxies(e_u)
    g_p = make_pairs(g)
    
    geos, gmap = taxicab_geometry(g_p,)
    # print(gmap)
    print(sum(geos))
    # print('\n'.join([''.join(r) for r in e_u]))
    

func()
