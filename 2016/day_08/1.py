FILENAME = 'input.txt'

HEIGHT = 6
WIDTH = 50

ON = '*'
OFF = '.'

def read_file():
    with open(FILENAME) as f:
        return [ln.strip() for ln in f.read().split('\n')]
    

BOARD = [
    [OFF for _ in range(WIDTH)] for _ in range(HEIGHT)
]

def draw_rect(cmd):
    dims = cmd.split(' ')[-1]
    w, h = dims.split('x')
    w = int(w)
    h = int(h)
    
    for hh in range(h):
        for ww in range(w):
            BOARD[hh][ww] = ON

def rotate(cmd):
    is_row = "column" not in cmd
    rotate_params = cmd.split('=')[-1]
    
    ix, rot = rotate_params.split(' by ')
    ix = int(ix)
    rot = int(rot)
    
    if is_row:
        new_arr = [OFF for _ in range(WIDTH)]
        for ax in range(len(new_arr)):
            new_arr[(ax + rot) % WIDTH] = BOARD[ix][ax]
        BOARD[ix] = new_arr
    else:
        new_arr = [OFF for _ in range(HEIGHT)]
        for bx in range(HEIGHT):
            new_arr[(bx + rot) % HEIGHT] = BOARD[bx][ix]
        for n_x in range(HEIGHT):
            BOARD[n_x][ix] = new_arr[n_x]
        
def count_board():
    c = 0
    for r in BOARD:
        for ele in r:
            if ele == ON:
                c += 1
    print(c)

def pprint_board():
    for r in BOARD:
        for c in r:
            print(c, end='')
        print()

def exec_command(cmd):
    if "rect" in cmd:
        draw_rect(cmd)
    else:
        rotate(cmd)

def func():
    commands = read_file()
    for cmd in commands:
        exec_command(cmd)
    pprint_board()
    print('---------')
    count_board()


func()