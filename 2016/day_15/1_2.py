FILENAME = "processed_input.txt"

def read_file():
    r = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            a = tuple(int(x) for x in ln.split(' '))
            r.append(a)
    return r

def sync(data):
    tzero = 1
    found = False
    while not found:
        found = all(
            [
                tzero%d[1] == (d[1] - d[2]- d[0] - 1)%d[1]
                for d in data
            ]
        )
        tzero += 1
    return tzero

def func():
    data = read_file()
    # Part 2:
    data.append((7,11,0))
    t = sync(data)
    print(t)

func()
