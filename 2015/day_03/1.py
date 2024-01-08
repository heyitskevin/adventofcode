FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return list(f.read())
    
def houses_visited(directions):
    visited = set()

    current = (0,0)
    visited.add(current)
    directionalize = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    while directions:
        next_dir = directionalize[directions.pop(0)]
        x, y = current
        x = x + next_dir[0]
        y = y + next_dir[1]
        current = (x,y)
        visited.add(current)

    print(len(visited))

def func():
    directions = read_file()
    
    houses_visited(directions)

func()