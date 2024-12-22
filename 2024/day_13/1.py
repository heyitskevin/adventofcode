import sys

def readfile():
    res = []
    with open('input.txt') as f:
        for blob in f.read().split('\n\n'):
            d = {}
            for ln in blob.split('\n'):
                if 'Button' in ln:
                    k, data = ln.split(':')
                    x, y  = data.split(',')
                    x = x.strip().split('+')[1]
                    y = y.strip().split('+')[1]
                    k = k.strip().split(' ')[1]
                    d[k] = {
                        "X": int(x),
                        "Y": int(y)
                    }
                else:
                    data = ln.split(':')[1]
                    x, y = data.split(',')
                    x = x.strip().split('=')[1]
                    y = y.strip().split('=')[1]
                    d["price"] = {
                        "X": int(x),
                        "Y": int(y)
                    }
            res.append(d)
    return res

def calc_tokens(Ax, Ay, Bx, By, X, Y):
    tokens = sys.maxsize
    changed = False
    for a_press in range(0, 101):
        for b_press in range(0, 101):
            if (Ax * a_press) + (Bx * b_press) == X:
                if (Ay * a_press) + (By * b_press) == Y:
                    changed = True
                    tokens = min(tokens, (3 * a_press) + b_press)
    if not changed:
        tokens = 0
    return tokens

def main():
    data = readfile()
    tokens = 0
    for pset in data:
        tokens += calc_tokens(
            pset['A']['X'],
            pset['A']['Y'],
            pset['B']['X'],
            pset['B']['Y'],
            pset['price']['X'],
            pset['price']['Y']
        )
    
    return tokens

print(main())