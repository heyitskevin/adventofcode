FILENAME = 'input.txt'

def read_file():
    with open(FILENAME) as f:
        return f.read().split('\n')
    
def func():
    d = read_file()
    v = 0
    for ln in d:
        f = False
        p = ln.split()
        lookup = set()
        for pp in p:
            if ''.join(sorted(pp)) in lookup:
                f = True
                break
            else:
                lookup.add(''.join(sorted(pp)))
        if not f:
            v += 1
    return v

print(func())