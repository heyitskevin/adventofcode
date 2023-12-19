FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f: # UGLY
        return [ (elem[0], int(elem[1]), elem[2])
            for elem in [
                ln.split(' ') for ln in f.read().split('\n')
            ] 
        ]
    
def dig_hole(instructions):
    result = []
    current = (0,0)
    xy_lookup = { # X IS FIRST VALUE, Y IS SECOND, VERY CARTESIAN
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    for inst in instructions:
        direction, count, _ = inst
        dd = xy_lookup[direction]
        for i in range(count):
            new_row = current[0] + dd[0]
            new_col = current[1] + dd[1]
            current = (new_row, new_col)
            result.append(current)
    return result

def shoelace(points):
    points = list(points)
    area = 0
    for ix, p in enumerate(points):
        x_coord, y_coord = p
        y_next, y_prev = 0, 0
        if ix in range(1, len(points)-1):
            y_next = points[ix+1][1]
            y_prev = points[ix-1][1]
        if ix == 0:
            y_next = points[ix+1][1]
            y_prev = points[-1][1]
        if ix == len(points) - 1:
            y_next = points[0][1]
            y_prev = points[ix-1][1]

        area += (x_coord * (y_next - y_prev))
    area = area / 2
    return abs(area)

def func():
    instructions = read_file()
    xycoords = dig_hole(instructions)
    print(xycoords, len(xycoords))
    a = shoelace(xycoords)
    picks =  int(a + 1 - (len(xycoords)/2))
    print(a)
    print('picks', a + 1 - len(xycoords)/2)
    print(picks + len(xycoords))


func()