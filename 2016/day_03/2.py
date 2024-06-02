FILENAME = 'input.txt'

def read_file():
    arr = []
    c1 = []
    c2 = []
    c3 = []
    container = [c1, c2, c3]
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            for ix, v in enumerate([int(x) for x in ln.strip().split(' ') if x]):
                container[ix].append(v)
            
    return container

def func():
    v = read_file()
    count = 0
    for row in v:
        for i in range(0, len(row), 3):
            # Nest IF statements to more prettily simulate a pack of ANDs
            if row[i] + row[i+1] > row[i+2]:
                if row[i+1] + row[i+2] > row[i]:
                    if row[i+2] + row[i] > row[i+1]:
                        count += 1
    print(count)

func()