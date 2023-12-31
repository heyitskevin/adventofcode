FILENAME = 'input.txt'
import pprint
import sys

def read_file():
    with open(FILENAME) as f:
        return [list(ln.strip()) for ln in f.read().split('\n')]
    
def get_start_and_end(trails):
    start_row = trails[0]
    end_row = trails[-1]
    
    for ix, e in enumerate(start_row):
        if e == '.':
            start_ix = ix
            break
    for ix, e in enumerate(end_row):
        if e == '.':
            end_ix = ix
            break
    return (0, start_ix), (len(trails) - 1, end_ix)

# DFS doesn't get us the max path, it gets us all nodes visited on the way to the path. Not correct
def dfs(trails, start, end, visited): 
    slopes = '<>^v' # L R U D
    height = len(trails)
    width = len(trails[0])
    r, c = start
    while start != end:
        if start in visited:
            break
        print('visiting', start)
        visited.add(start)
        slope_ix = slopes.find(trails[r][c])
        # get neighbors
        neighbors = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)] # L R U D
        if slope_ix > -1:
            # when on a slope only go in one direction
            neighbors = [neighbors[slope_ix]] # maintain an array for iteration
        
        for n in neighbors:
            new_row, new_col = n
            if new_row in range(height) and new_col in range(width) and trails[new_row][new_col] != '#':
                # DFS each neighbor
                dfs(trails, (new_row, new_col), end, visited)
        
        
    return visited, len(visited)

def search_max_path_length(trails, start, end, path_so_far, final_paths):
    if start == end:
        final_paths.append(path_so_far)
        return
    if start in path_so_far: # Illegal step
        return
    slopes = '<>^v' # L R U D
    height = len(trails)
    width = len(trails[0])
    r, c = start
    new_path = path_so_far + [start]
    slope_ix = slopes.find(trails[r][c])
    # get neighbors
    neighbors = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)] # L R U D
    if slope_ix > -1:
        # when on a slope only go in one direction
        neighbors = [neighbors[slope_ix]] # maintain an array for iteration
    
    for n in neighbors:
        new_row, new_col = n
        if new_row in range(height) and new_col in range(width) and trails[new_row][new_col] != '#':
            search_max_path_length(trails, (new_row, new_col), end, new_path, final_paths)
    return final_paths
        

def func():
    sys. setrecursionlimit(12000) # LMAO BTW, arbitrarily large number
    trails = read_file()
    start, end = get_start_and_end(trails)
    final_paths = []
    d = search_max_path_length(trails, start, end, [], final_paths)
    # visited = set()
    # print(start, end)
    # d = dfs(trails, start, end, visited)
    print(max([len(x) for x in d]))

func()