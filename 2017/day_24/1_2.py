import copy
FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return [tuple([int(x) for x in ln.split('/')]) for ln in f.read().split('\n')]
    

def build_all(start, graph):
    res =[]
    paths_remaining = True
    while paths_remaining:
        new_path = []
        curr = start
        visited = set()
        paths_remaining = False
    return res



def func():
    data = readfile()
    graph = {d: [] for d in data}
    print(graph)
    

# From reddit
data = readfile()
bridge = ([], 0)

def run(b, d):
    available = [a for a in d if b[1] in a]
    if len(available) == 0:
        yield b
    else:
        for a in available:
            d_ = d.copy()
            d_.remove(a)
            for q in run((b[0] + [a], a[0] if b[1] == a[1] else a[1]), d_):
                yield q

# part 1
print(max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), run(bridge, data))) )

# part 2
max_len = max(map(lambda bridge: len(bridge[0]), run(bridge, data)))
long = filter(lambda bridge: len(bridge[0]) == max_len, run(bridge, data))
print(max(map(lambda bridge: sum([a + b for a, b in bridge[0]]), long)) )
