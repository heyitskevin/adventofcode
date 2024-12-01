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
    r = 0
    a, b = read_file()
    a = sorted(a)
    b = sorted(b)
    for ix in range(len(a)):
        r += abs(a[ix] - b[ix])
    return r
print(main())