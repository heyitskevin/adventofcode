# THIS FILE IS FROM ME DEBUGGING LIKE CRAZY ONLY TO REALIZE I DIDN'T READ THE PROBLEM
# LEAVING THIS HERE TO REMIND MYSELF OF MY BOZO

FILENAME = 'example.txt'

import math
import itertools
from collections import defaultdict
import heapq

def read_file():
    with open(FILENAME) as f:
        return [[int(c) for c in ln] for ln in f.read().split('\n')]

def get_next_nodes(height, width, start_row, start_col, current_direction, previous_directions):
    directionizer = {
        'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r': (0, 1)
    }
    # Left, Right or Go Straight 3 - previous elements
    neighbors = []
    if current_direction in ['u', 'd']:
        neighbors.append(((start_row , start_col - 1), 'l'))
        neighbors.append(((start_row, start_col + 1), 'r'))
    elif current_direction in ['l', 'r']:
        neighbors.append(((start_row - 1, start_col), 'u'))
        neighbors.append(((start_row + 1, start_col), 'd'))
    count_preceding = len([p == current_direction for p in previous_directions])
    for multi in range(3 - count_preceding): # Go up to 3 in this direction
        rrr, ccc = directionizer[current_direction]
        rrr = rrr * (multi + 1)
        ccc = ccc * (multi + 1)
        neighbors.append(((start_row + rrr, start_col + ccc), current_direction))
    
    # Filter out by boundedness
    def f(n):
        loc, _ = n
        r, c = loc
        if 0 <= r < height or 0 <= c < width:
            return True
        return False
    print(neighbors)
    return [item for item in neighbors if f(item)]
        
def get_previous_directions(prev_node_map, current_row, current_col):
    # Hard access b/c we initialize the dict to have all keys w/ values None
    first_prev = prev_node_map[(current_row, current_col)]
    second_prev = None
    third_prev = None
    if first_prev:
        second_prev = prev_node_map[(first_prev[0], first_prev[1])]
    if second_prev:
        third_prev = prev_node_map[(second_prev[0], second_prev[1])]
    all_three = [i for i in (first_prev, second_prev, third_prev) if i]

    direction_diff = {
        (-1, 0): 'u',
        (1, 0): 'd',
        (0, 1): 'r',
        (0, -1): 'l'
    }
    prev_dirs = []
    print('at', all_three)
    for prev in all_three:
        row_diff = current_row - prev[0]
        col_diff = current_col - prev[1]
        r_ix = 0
        c_ix = 0
        
        if row_diff > 0:
            r_ix = 1
        elif row_diff < 0:
            r_ix = -1
        if col_diff > 0:
            c_ix = 1
        elif col_diff < 0:
            c_ix = -1

        print(r_ix, c_ix)
        diff = direction_diff.get((r_ix, c_ix))
        if diff:
            prev_dirs.append(diff)
    return prev_dirs


def find_best_path(grid, start, end):
    # An implementation of Dijkstra's
    height = len(grid)
    width = len(grid[0])
    start_row, start_col = start
    
    heap = []
    dist_to_node = {(i, j): math.inf for i, j in itertools.product(range(height), range(width))}
    previous_node = {(i, j): None for i, j in itertools.product(range(height), range(width))}
    
    nodes_visited = set()

    dist_to_node[(start_row, start_col)] = 0
    # (Cost, (row_ix, col_ix), current_direction)
    heapq.heappush(heap, (0, (start_row, start_col), 'r'))
    heapq.heappush(heap, (0, (start_row, start_col), 'd'))

    while heap:
        _, ixes, current_direction = heapq.heappop(heap)
        if ixes == end:
            return dist_to_node, previous_node
        nodes_visited.add(ixes)
        current_row, current_col = ixes
        previous_directions = get_previous_directions(previous_node, current_row, current_col)
        
        next_nodes = get_next_nodes(
            height, 
            width,
            current_row,
            current_col,
            current_direction,
            previous_directions
        )
        
        for nn in next_nodes:
            nn_ixes, next_direction = nn
            nn_r, nn_c = nn_ixes
            # Check bounds
            if (nn_r < 0 or nn_r >= height) or (nn_c < 0 or nn_c >= width):
                continue
            if nn_ixes in nodes_visited:
                continue

            nn_weight = grid[nn_r][nn_c]
            test_cost_to_this_node = dist_to_node[(current_row, current_col)] + nn_weight # From current node + nn_weight
            
            if dist_to_node[(nn_r, nn_c)] > test_cost_to_this_node:
                previous_node[(nn_r, nn_c)] = ixes
                dist_to_node[(nn_r, nn_c)] = test_cost_to_this_node
                heapq.heappush(heap, (test_cost_to_this_node, (nn_r, nn_c), next_direction))
    return previous_node, dist_to_node

def func():
    grid = read_file()
    height = len(grid)
    width = len(grid[0])
    a, b = find_best_path(grid, (0,0), (height - 1, width - 1))
    import pprint

    pprint.pprint(a)
    print('---')
    pprint.pprint(b)
func()
