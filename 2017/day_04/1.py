FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return f.read().split('\n')

def func():
    d = read_file()
    v = 0
    for ln in d:
        s = ln.split()
        if len(s) == len(set(s)):
            v += 1
    return v


print(func())