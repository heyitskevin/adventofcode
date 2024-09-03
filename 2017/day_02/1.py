FILENAME = "input.txt"

def read_file():
    arr = []
    with open(FILENAME) as f:
        for x in f.read().split('\n'):
            r = []
            for s in x.split():
                r.append(int(s))
            arr.append(r)
    return arr

def func():
    a = read_file()
    s = 0
    for r in a:
        x = max(r)
        n = min(r)
        s += (x - n)
    return s

print(func())