FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return [int(x) for x in f.read().split()]

def func():
    banks = read_file()
    
    visited = set()
    steps = 0
    lookup = {}
    while True:
        if tuple(banks) in visited:
            break
        visited.add(tuple(banks))
        lookup[tuple(banks)] = steps
        max_val = max(banks)
        ix = 0
        for x in range(len(banks)):
            if banks[x] == max_val:
                ix = x
                break
        banks[ix] = 0
        ix += 1
        while max_val:
            banks[ix % len(banks)] += 1
            max_val -= 1
            ix += 1
        
        steps += 1
    return steps - lookup[tuple(banks)] 

print(func())