from collections import Counter
def readfile():
    res = []
    with open('input.txt') as f:
        for ln in f.readlines():
            res.append(ln.strip())
    return res

def main():
    d = readfile()
    for ln in d:
        diff = 0
        ixx = -1
        for pa in d:
            if diff > 1:
                diff = 0
                ixx = -1
                continue
            if pa == ln:
                continue
            for ix, chr in enumerate(ln):
                if chr != pa[ix]:
                    diff += 1
                    ixx = ix
            if diff == 1:
                return(ln, pa, ixx, ln[:ixx]+ln[ixx+1:])
    return -1


print(main())