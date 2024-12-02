from collections import Counter
def readfile():
    res = []
    with open('input.txt') as f:
        for ln in f.readlines():
            res.append(ln.strip())
    return res


def main():
    a = readfile()
    cs = 0
    twos = 0
    tres = 0
    for e in a:
        ct = Counter(e)
        t = 0
        r = 0
        for k, v in ct.items():
            if v == 2:
                t = 1
            if v == 3:
                r = 1
        twos += t
        tres += r
    return twos * tres
print(main())