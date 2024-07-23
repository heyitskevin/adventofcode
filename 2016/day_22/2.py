from itertools import permutations
FILENAME = "input.txt"

def read_file():
    with open(FILENAME) as f:
        return [ln.strip() for ln in f.read().split('\n')]
    
def get_nodes(full_file):
    return [[l for l in ln.split(" ") if l]for ln in full_file[2:]]


def build_grid(nodes):
    res = [[0 for _ in range(28)] for __ in range(38)]

    for node in nodes:
        name, size, used, ava, percent = node
        x, y = name.split('/')[-1].split('-')[1:]
        x = int(x[1:])
        y = int(y[1:])
        res[x][y] = int(percent[:-1])
        if int(size[:-1]) > 100:
            res[x][y] = 'B'
        if x == 37 and y == 0:
            res[x][y] = 'G'
    
    return res


def func():
    d = read_file()
    n = get_nodes(d)
    g = build_grid(n)
    for ln in g:
        print(ln)


func()
a = 5 * 36
a += 26 + 3 + 28 + 23 + 1
print(a)

# Solved by staring at the grid and doing pen and paper LOL