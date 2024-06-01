FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [x.strip() for x in f.read().split(', ')]
        
def manhattan(steps):
    rotator = [1, 1, -1, -1]
    start_direction = 0
    x = 0
    y = 0
    for s in steps:
        turn = s[0]
        j = int(s[1:])
        if turn == 'L':
            start_direction -= 1
        else:
            start_direction += 1
        start_direction = start_direction % 4
        if start_direction%2 == 0:
            y = y + (j * rotator[start_direction])
        else:
            x = x + (j * rotator[start_direction])
    return abs(x) + abs(y)

def func():
    s = read_file()
    d = manhattan(s)
    print(d)

func()