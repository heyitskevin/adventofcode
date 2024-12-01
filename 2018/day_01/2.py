FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return f.read().split('\n')
    
def func():
    seen = set()
    b = 0
    seen.add(0)
    while True:
        for ln in readfile():
            nxt = ln[1:]
            if '+' in ln:
                b += int(nxt)
            else:
                b -= int(nxt)
            if b in seen:
                return b
            seen.add(b)

    return None

print(func())