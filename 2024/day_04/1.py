def readfile():
    r = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            r.append(list(ln))
    return r

def main():
    a = readfile()
    MAS = ['M', 'A', 'S']
    width = len(a[0])
    height = len(a)
    res = 0
    diag = [[1,1], [-1,1], [1,-1], [-1,-1], [0,1], [1, 0], [-1,0],[0,-1]]
    for r, row in enumerate(a):
        for c, col in enumerate(row):
            elem = a[r][c]
            if elem == 'X':
                for di in diag:
                    addr, addc = di
                    x, y = r, c
                    cc = []
                    for _ in range(3):
                        x += addr
                        y += addc
                        if 0 <= x < width and 0 <= y < height:
                            cc.append(a[x][y])
                    if cc == MAS:
                        res += 1
                    
    return res


print(main())