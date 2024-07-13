SAFE = '.'
TRAP = '^'
FILENAME = 'input.txt'

def first_row():
    with open(FILENAME) as f:
        return f.read().strip()
    
def count_row(row):
    c = 0
    for x in row:
        if x == SAFE:
            c += 1
    return c

def make_row(prev):
    n = ""
    for ix in range(len(prev)):
        if ix == 0:
            left = SAFE
        else:
            left = prev[ix-1]
        if ix == len(prev) - 1:
            right = SAFE
        else:
            right = prev[ix+1]
        if left != right:
            n+= '^'
        else:
            n+= '.'
    return n

def func():
    r = first_row()
    ct = count_row(r)

    i = 1
    #  Lazy implementation means double counting
    while i < 400000:
        r = make_row(r)
        ct += count_row(r)
        i += 1
    print(ct)

func()