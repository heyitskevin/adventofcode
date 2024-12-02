def readfile():
    res = []
    with open('input.txt') as f:
        for ln in f.read().split('\n'):
            res.append([int(x) for x in ln.strip().split(' ')])
    return res


def main():
    a = readfile()
    safe = 0
    for rep in a:
        inc = False
        dec = False
        if rep == sorted(rep):
            inc = True
        elif rep == sorted(rep)[::-1]:
            dec = True
        is_safe = False
        if inc or dec:
            for ix, elem in enumerate(rep):
                if ix == len(rep) - 1:
                    continue
                nxt = rep[ix + 1]
                diff = abs(elem - nxt)
                if diff > 3 or diff < 1:
                    is_safe = False
                    break
                else:
                    is_safe = True
            if is_safe:
                safe += 1

    return safe

print(main())