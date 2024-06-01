FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [x.strip() for x in f.read().split(', ')]
    
def with_visitation(steps):
    visited = set()

    rotator = [1, 1, -1, -1]
    start_direction = 0
    x = 0
    y = 0

    visited.add((x, y))
    for s in steps:
        turn = s[0]
        j = int(s[1:])
        if turn == 'L':
            start_direction -= 1
        else:
            start_direction += 1
        start_direction = start_direction % 4
        if start_direction%2 == 0:
            new_y = 0
            for yy in range (1, j+1):
                new_y = y + (rotator[start_direction] * yy)
                if (x, new_y) in visited:
                    return abs(x) + abs(new_y)
                else:
                    visited.add((x, new_y))
            y = new_y
        else:
            new_x = 0
            for xx in range(1, j+1):
                new_x = x + (rotator[start_direction] * xx)
                if (new_x, y) in visited:
                    return abs(new_x) + abs(y)
                else:
                    visited.add((new_x, y))
            x = new_x


def func():
    s = read_file()
    d = with_visitation(s)
    print(d)

func()