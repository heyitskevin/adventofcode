from collections import Counter

def read_file():
    aa = []
    bb = []
    with open('input.txt') as f:
        for ln in f:
            a, b = ln.split()
            aa.append(int(a.strip()))
            bb.append(int(b.strip()))
    return aa, bb


def main():
    sim = 0
    a, b = read_file()
    ca = Counter(a)
    cb = Counter(b)
    for ix in range(len(a)):
        sim += a[ix] * cb[a[ix]]
    return sim
print(main())