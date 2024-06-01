FILENAME = 'input.txt'

def read_file():
    arr = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            arr.append([c for c in ln.strip()])
    return arr

def update_coords(coords, step):
    r, c = coords
    match step:
        case 'U':
            if coords[0] == 0:
                pass
            else:
                r -= 1
        case 'D':
            if coords[0] == 2:
                pass
            else:
                r += 1
        case 'L':
            if coords[1] == 0:
                pass
            else:
                c -= 1
        case 'R':
            if coords[1] == 2:
                pass
            else:
                c += 1
    return (r, c)

def process_instructions(instructions, coords):
    c = coords
    for step in instructions:
        c = update_coords(c, step)
    return c

def func():
    s = read_file()
    coords = (1, 1)

    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for instructions in s:
        coords = process_instructions(instructions, coords)
        print(board[coords[0]][coords[1]])
func()