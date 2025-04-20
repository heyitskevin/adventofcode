def readfile():
    r = set()
    max_x, max_y = -1, -1
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            x, y = ln.split(',')
            x = int(x)
            y = int(y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            r.add((x, y))
    return r, max_x, max_y


def main():
    nodes, max_rows, max_cols = readfile()
    max_dist = 10_000

    soln = 0

    for r in range(max_rows + 1):
        for c in range(max_cols + 1):
            soln += int(sum(abs(rr - r) + abs(cc - c) for rr, cc in nodes) < max_dist)
    return soln


print(main())