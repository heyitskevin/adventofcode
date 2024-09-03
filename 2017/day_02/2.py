FILENAME = "input.txt"

def read_file():
    arr = []
    with open(FILENAME) as f:
        for x in f.read().split('\n'):
            r = []
            for s in x.split():
                r.append(int(s))
            arr.append(r)
    return arr

def func():
    a = read_file()
    s = 0
    
    for r in a:
        found = False
        for i in range(len(r)):
            for j in range(1, len(r)):
                if i != j:
                    if (r[i] % r[j]) == 0:
                        s += (r[i] // r[j])
                        found = True
                        break
                    if (r[j] % r[i]) == 0:
                        s += (r[j] // r[i])
                        found = True
                        break
            if found:
                break
    return s

print(func())