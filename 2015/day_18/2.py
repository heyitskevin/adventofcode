FILENAME = 'input.txt'

def readfile():
    grid = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            grid.append(list(ln.strip()))
    return grid

import copy
def make_next_grid(grid):
    newgrid = copy.deepcopy(grid)

    def get_neighbor_ix(row, col, height, width):
        neighbors =  [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
            (row - 1, col + 1),
            (row - 1, col - 1),
            (row + 1, col + 1),
            (row + 1, col - 1)
        ]
        valid_neighbors = []
        for r, c in neighbors:
            if r < 0 or c < 0 or r > height - 1 or c > width - 1:
                continue
            else:
                valid_neighbors.append((r, c))
        return valid_neighbors
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in  [
                (0,0),
                (0, len(grid[0]) - 1),
                (len(grid) - 1, 0),
                (len(grid) - 1, len(grid[0]) - 1)
            ]:
                continue
            current_element = grid[row][col]
            neighbors = get_neighbor_ix(row, col, len(grid), len(grid[0]))
            num_on = 0 # num_off is just 8 - num_on
            for r, c in neighbors:
                if grid[r][c] == '#':
                    num_on += 1
            # If state is ON and neighbors ON are 2 or 3: Turn OFF
            if current_element == '#' :
                if num_on == 2 or num_on == 3:
                    newgrid[row][col] = '#'
                else:
                    newgrid[row][col] = '.'
            # If state is OFF and neighbors ON is 3: Turn ON
            if current_element == '.':
                if num_on == 3:
                    newgrid[row][col] = '#'
                else:
                    newgrid[row][col] = '.'
    
    return newgrid

def count_lights(grid):
    c = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                c += 1
    return c


def func():
    grid = readfile()
    # Set always on 
    grid[0][0] = '#'
    grid[-1][0] = '#'
    grid[0][-1] = '#'
    grid[-1][-1] = '#'

    for _ in range(100):
        grid = make_next_grid(grid)
    lights = count_lights(grid)
    print(lights)

func()
# 861 too low