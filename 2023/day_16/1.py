FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [list(ln) for ln in f.read().split('\n')]

def get_next_position_indexes(current_position, current_direction):
    match current_direction:
        case 'right':
            return current_position[0], current_position[1] + 1
        case 'left':
            return current_position[0], current_position[1] - 1
        case 'up':
            return current_position[0] - 1, current_position[1]
        case 'down':
            return current_position[0] + 1, current_position[1]
        
def get_directions_by_element(element, direction):
    hor = ['left', 'right']
    ver = ['up', 'down']
    if element == '.':
        return [direction] # Continue in the same direction
    if element == '-' and direction in hor:
        return [direction]
    if element == '|' and direction in ver:
        return [direction]
    # Splitters
    if element == '-' and direction in ver:
        return ['left', 'right']
    if element == '|' and direction in hor:
        return ['up', 'down']
    # Mirrors
    if element == '/':
        match direction:
            case 'up':
                return ['right']
            case 'down':
                return ['left']
            case 'left':
                return ['down']
            case 'right':
                return ['up']
    if element == '\\':
        match direction:
            case 'up':
                return ['left']
            case 'down':
                return ['right']
            case 'left':
                return ['up']
            case 'right':
                return ['down']

def get_starting_config(starting_element):
    directions = get_directions_by_element(starting_element, 'right')
    return [((0,0), d) for d in directions]

def bfs(grid):
    q = get_starting_config(grid[0][0])
    visited = {}
    while q:
        current_position, current_direction = q.pop(0)
        
        if current_position in visited:
            visited_directions = visited[current_position]
            if current_direction in visited_directions:
                continue # We have traveled to this tile in this direction before, loop detected
            else:
                visited_directions.append(current_direction)
                visited[current_position] = visited_directions
        else:
            visited[current_position] = [current_direction]
        next_position = get_next_position_indexes(current_position, current_direction)
        # Check bounds
        if (next_position[0] < 0 or next_position[0] > len(grid) - 1) or (next_position[1] < 0 or next_position[1] > len(grid[0]) - 1):
            continue # Light is out of bounds, don't update and advance queue
        next_element = grid[next_position[0]][next_position[1]]
        next_direction = get_directions_by_element(next_element, current_direction)
        for nd in next_direction:
            q.append(((next_position[0], next_position[1]), nd))
        
    return visited

import pprint

def func():
    grid = read_file()
    
    visited = bfs(grid)
    pprint.pprint((visited, len(visited)))

func()

