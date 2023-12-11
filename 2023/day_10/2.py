FILENAME = 'input.txt'
INVALID_CHARACTER ='0'

"""
Part 2 using one of my favorite facts from graphics engineering: lets say you have an enclosed shape, and you want to color every pixel inside of it. How do you know if a given pixel is inside the shape or not? Well, it turns out: if you shoot a ray in any direction from the pixel and it crosses the boundary an odd number of times, it's inside. if it crosses an even number of times, it's outside. Works for all enclosed shapes, even self-intersecting and non-convex ones.

It does, however, interact badly if your ray and one of the edges of the shape is collinear, so you have to be clever about it for this problem. 
"""


def read_maze():
    maze = []
    with open (FILENAME) as f:
        for ln in f:
            ln = ln.strip()
            maze.append(list(ln))
    return maze

def find_s(maze):
    for row, val in enumerate(maze):
        for col, val2 in enumerate(val):
            if val2 == 'S':
                return row, col
    return -1, -1

def pretty_print_maze(maze):
    for row in maze:
        print(''.join(row))

def get_starting_directions(maze, start_row, start_col):
    starts = []
    # Look left
    if start_col > 0:
        left = maze[start_row][start_col - 1]
        if left in ['-', 'L', 'F']:
            starts.append([start_row, start_col - 1, 'W'])
    # Look Right
    if start_col < len(maze[0]) - 1:
        right = maze[start_row][start_col + 1]
        if right in ['-', 'J', '7']:
            starts.append([start_row, start_col + 1, 'E'])
    # Look Up
    if start_row > 0:
        up = maze[start_row - 1][start_col]
        if up in ['|', '7', 'F']:
            starts.append([start_row - 1, start_col, 'N'])
    # Look Down
    if start_row < len(maze) - 1:
        down = maze[start_row + 1][start_col]
        if down in ['|', 'J', 'L']:
            starts.append([start_row + 1, start_col, 'S'])
    
    return starts

def visit_maze(maze, start, end, starting_directions):
    row, col, going_in_this_direction = starting_directions.pop(0)
    curr_element = maze[row][col]
    s_loc = maze[start][end]
    steps = 1
    visited = []
    while curr_element != s_loc:
        # visited.append((row, col))
        match going_in_this_direction:
            case 'N':
                if curr_element == '|':
                    row = row - 1
                    going_in_this_direction = 'N'
                elif curr_element == '7':
                    col = col - 1
                    going_in_this_direction = 'W'
                elif curr_element == 'F':
                    col = col + 1
                    going_in_this_direction = 'E'
                next_element = maze[row][col]
            case 'S':
                if curr_element == '|':
                    row = row + 1
                    going_in_this_direction = 'S'
                elif curr_element == 'J':
                    col = col - 1
                    going_in_this_direction = 'W'
                elif curr_element == 'L':
                    col = col + 1
                    going_in_this_direction = 'E'
                next_element = maze[row][col]
            case 'E':
                if curr_element == '-':
                    col = col + 1
                    going_in_this_direction = 'E'
                elif curr_element == 'J':
                    row = row - 1
                    going_in_this_direction = 'N'
                elif curr_element == '7':
                    row = row + 1
                    going_in_this_direction = 'S'
                next_element = maze[row][col]
            case 'W':
                if curr_element == '-':
                    col = col - 1
                    going_in_this_direction = 'W'
                elif curr_element == 'L':
                    row = row - 1
                    going_in_this_direction = 'N'
                elif curr_element == 'F':
                    row = row + 1
                    going_in_this_direction = 'S'
                next_element = maze[row][col]
        
        visited.append((row, col))
        steps += 1
        curr_element = next_element

    return visited

def clean_maze(maze, path_set): # used for printing
    clean = []
    for ixr, row in enumerate(maze):
        clean_row = []
        for ixc, col_elem in enumerate(row):
            coord = (ixr, ixc)
            elem = INVALID_CHARACTER
            if coord in path_set or col_elem == 'S':
                elem = col_elem
            clean_row.append(elem)
        clean.append(clean_row)
    return clean


def clean_row(row): # uSed for printing
    clean_ixes = []
    ix = 0
    base_ix = 0
    bound_encountered = False
    while not bound_encountered:
        if ix > len(row) - 1:
            clean_ixes.append((base_ix, ix))
            break
        elem = row[ix]
        if elem != INVALID_CHARACTER:
            bound_encountered = True
            clean_ixes.append((base_ix, ix))
        ix += 1
    return clean_ixes

def purge_maze(cleaned_maze):
    new_maze = []
    # Make outer bounds
    for row in cleaned_maze:
        if not all([r == INVALID_CHARACTER for r in row]):
            new_maze.append(row)
    
    boundary_by_row = {
        ix: [] for ix , r in enumerate(new_maze)
    }

    for rix, row in enumerate(new_maze):
        l_clean = clean_row(row)
        r_clean = clean_row(row[::-1])
        r_clean = [(len(row) - x[1], len(row) - x[0]) for x in r_clean]
        boundary_by_row[rix] += l_clean + r_clean
    
    for ixr, row in enumerate(new_maze):
        inelligible_indexes = boundary_by_row[ixr]
        new_maze[ixr] = [' ' if any([ixc in range(*tup) for tup in inelligible_indexes]) else elem for ixc, elem in enumerate(row)]
        
    # pretty_print_maze(new_maze)
    return new_maze

def clean_row(row): # Used for printng
    clean_ixes = []
    ix = 0
    base_ix = 0
    bound_encountered = False
    while not bound_encountered:
        if ix > len(row) - 1:
            clean_ixes.append((base_ix, ix))
            break
        elem = row[ix]
        if elem != INVALID_CHARACTER:
            bound_encountered = True
            clean_ixes.append((base_ix, ix))
        ix += 1
    return clean_ixes
    

def func():
    maze = read_maze()
    s_row, s_col = find_s(maze)
    starting_directions = get_starting_directions(maze, s_row, s_col)
    rr, cc, xx = starting_directions[0]
    visited = visit_maze(maze, s_row, s_col, starting_directions)
    print(len(visited))
    vis_set = {(rr, cc): 0} # Stupid weird edge case coverage b/c I did some funny pop() calls above
    for elem in visited:
        if elem in vis_set:
            pass
        else:
            vis_set[elem] = 0
    # sparse = clean_maze(maze,visited)
    tot = 0
    for ix, r in enumerate(maze):
        for ixx, c in enumerate(r):
            if (ix, ixx) in vis_set:
                continue
            intersections = 0
            x, y = ixx, ix
            while x < len(maze[0]) and y < len(maze):
                candidate = maze[y][x]
                if (y, x) in vis_set and candidate != 'L' and candidate != '7':
                    # Omit L and 7 b/c we are going down and right 
                    # i.e. x +=  1 and y+= 1
                    intersections += 1
                x += 1
                y += 1
            if intersections % 2 == 1:
                tot += 1
    print(tot)
    

func()
