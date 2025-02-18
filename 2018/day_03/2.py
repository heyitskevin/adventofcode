def readfile():
    r = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            fabric, coords = ln.split('@')
            corner, size = coords.strip().split(':')
            cx, cy = corner.strip().split(',')
            w, h = size.strip().split('x')
            r.append((int(fabric[1:]), (int(cx), int(cy)), (int(w), int(h))))
    return r


def main():
    dat = readfile()
    spread = {}
    s = set()
    for row in range(1500):
        for col in range(1500):
            spread[(row, col)] = []
    for d in dat:
        fabric, corner, size = d
        
        for rr in range(corner[0], corner[0] + size[0]):
            for cc in range(corner[1], corner[1] + size[1]):
                spread[(rr, cc)].append(fabric)
    for k, v in spread.items():
        if len(v) > 1:
            for claim in v:
                s.add(claim)

    return set(x[0] for x in dat) - s


print(main())
