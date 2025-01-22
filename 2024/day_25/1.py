def readfile():
    obj = []
    with open('input.txt') as f:
        for elem in f.read().split('\n\n'):
            arr = []
            for e in elem.split('\n'):
                arr.append(list(e.strip()))
            obj.append(arr)
    return obj

def process(data):
    locks = []
    keys = []
    size = len(data[0])
    
    for d in data:
        cols = [0 for _ in range(size)]
        for row in d:
            for ix, c in enumerate(row):
                if c == '#':
                    cols[ix] += 1
        if '#' in d[0]:
            locks.append(cols)
        else:
            keys.append(cols)

    return locks, keys

def main():
    data = readfile()
    # We could do this in readfile() but break it apart for readable consistency
    locks, keys = process(data)
    height = len(data[0])
    width = len(locks[0])
    match = set()
    
    for lock in locks:
        for key in keys:
            fits = True
            for ix in range(width):
                if lock[ix] + key[ix] > height:
                    fits = False
            if fits:
                s_lock = ''.join(str(x) for x in lock)
                s_key = ''.join(str(y) for y in key)
                match.add((s_lock, s_key))

    assert len(locks) + len(keys) == len(data)

    return len(match)


print(main())