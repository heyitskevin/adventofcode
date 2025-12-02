def readfile():
    r = []
    with open('input.txt') as f:
        for ln in f.readlines():
            r.append(ln.strip())
    return r


def main():
    instructions = readfile()
    dial = 50
    ct = 0
    for i in instructions:
        lr, amt = i[0], int(i[1:])
        mult = 1
        if lr == "L":
            mult = -1
        elif lr == "R":
            mult = 1
        dial += (mult * amt)
        dial = dial % 100
        if dial == 0:
            ct += 1
    return ct




print(main())