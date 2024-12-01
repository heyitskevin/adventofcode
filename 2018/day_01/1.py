FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return f.read().split('\n')
    
def func():
    b = 0
    for ln in readfile():
        nxt = ln[1:]
        if '+' in ln:
            b += int(nxt)
        else:
            b -= int(nxt)
    return b

print(func())