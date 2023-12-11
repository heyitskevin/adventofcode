FILENAME = 'input.txt'

# Can't just naively expand the universe, have to count the number of intersections

def read_file():
    with open(FILENAME) as f:
        return [list(ln.strip()) for ln in f]
    

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

def taxicab_geometry(pairs, empty_rows, empty_cols):
    geos = []
    gmap = {}
    expansion_factor = 1000000
    expansion_factor -= 1 # Decrement by one for inclusion
    
    for p in pairs:
        start, end = p
        # since range() only works in the positive direction we gotta do some finnicking
        # we don't have to check equivalence b/c that means the line is occupied
        row_range = range(start[0], end[0]) if start[0] < end[0] else range(end[0], start[0])
        col_range = range(start[1], end[1]) if start[1] < end[1] else range(end[1], start[1])
        offset = 0
        for r_ix in empty_rows:
            if r_ix in row_range:
                offset += 1
        for c_ix in empty_cols:
            if c_ix in col_range:
                offset += 1
        taxi_dist = abs(end[0] - start[0]) + abs(end[1] - start[1]) + (offset * expansion_factor)
        geos.append(taxi_dist)
        gmap[p] = taxi_dist
    return geos, gmap


def func():
    u = read_file()
    emptys = get_empty_rows_and_cols(u)
    g = find_galaxies(u)
    g_p = make_pairs(g)
    geos, gmap = taxicab_geometry(g_p, emptys[0], emptys[1])
    print(sum(geos))
func()