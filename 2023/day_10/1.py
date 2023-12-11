FILENAME = 'input.txt'

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
    

def loop(maze, start, end, starting_directions):
    row, col, going_in_this_direction = starting_directions.pop(0)
    curr_element = maze[row][col]
    s_loc = maze[start][end]
    steps = 1
    while curr_element != s_loc:
        print(f'visiting {row}, {col}', curr_element)
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
        steps += 1
        curr_element = next_element

    return steps


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

def func():
    maze = read_maze()
    row, col = find_s(maze)
    starting_directions = get_starting_directions(maze, row, col)
    res = loop(maze, row, col, starting_directions)
    print(res//2)


func()


