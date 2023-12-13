FILENAME = 'example.txt'

def read_file():
    with open(FILENAME) as f:
        return [[list(ln.strip()) for ln in blck.split('\n')]for blck in f.read().split('\n\n')]

def func():
    rocks = read_file()
    print(rocks)
func()