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


def solve(Ax, Ay, Bx, By, X, Y):
    # Ax * a_press + Bx * b_press = X
    # Ay * a_press + By * b_press = Y
    # Two unknowns, solve by elmination
    # Ax * Ay * a_press + Bx * Ay * b_press = X * Ay
    # Ax * Ay * a_press + By * Ax * b_Press = Y * Ax
    # b_press * (Bx * Ay - By * Ax) = X * Ay - Y * Ax
    b_press = ((X * Ay) - Y * Ax) / ((Bx * Ay) - By * Ax)
    if b_press == int(b_press):
        a_press = (X - (Bx * b_press)) / Ax
        if a_press == int(a_press):
            return int(3 * a_press + b_press)
    return 0
    

def main():
    data = readfile()
    tkn = 0
    for d in data:
        tkn += solve(
            d['A']['X'], 
            d['A']['Y'], 
            d['B']['X'],
            d['B']['Y'],
            d['price']['X'] + 10000000000000,
            d['price']['Y'] + 10000000000000
        )
    return tkn


print(main())