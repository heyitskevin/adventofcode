FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return list(f.read())
    

def houses_visited(directions):
    santa = (0,0)
    robo = (0,0)

    visited = set()
    visited.add(santa)

    turn = True

    directionalize = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0)
    }


    while directions:
        next_dir = directionalize[directions.pop(0)]

        if turn:
            x, y = santa
            x = x + next_dir[0]
            y = y + next_dir[1]
            santa = (x,y)
            visited.add(santa)
            turn = False
        else:
            x, y = robo
            x = x + next_dir[0]
            y = y + next_dir[1]
            robo = (x,y)
            visited.add(robo)
            turn = True
    print(len(visited))

def func():
    d = read_file()
    houses_visited(d)

func()
        
