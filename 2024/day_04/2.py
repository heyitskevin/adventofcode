def readfile():
    r = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            r.append(list(ln))
    return r

def main():
    a = readfile()
    res = 0
    MAS = [['M', 'A', 'S'], ['S', 'A', 'M']]
    for r, row in enumerate(a):
        for c, col in enumerate(row):
            if 1 <= r < len(a) - 1 and 1 <= c < len(row) - 1:
                if a[r][c] == 'A':
                    c1 = [a[r-1][c-1], a[r][c], a[r+1][c+1]]
                    c2 = [a[r-1][c+1], a[r][c], a[r+1][c-1]]
                    if c1 in MAS and c2 in MAS:
                        res += 1
    return res


print(main())