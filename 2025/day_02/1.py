def readfile():
    ids_ranges = []
    with open("input.txt") as f:
        for ln in f.read().strip().split(","):
            l, r = ln.strip().split("-")
            ids_ranges.append((int(l), int(r)))
    return ids_ranges


def main():
    r = readfile()
    invalid = 0
    for rr in r:
        start, end = rr
        for n in range(start, end + 1):
            s = str(n)
            if len(s) % 2 == 0:
                halfway = len(s) // 2
                h1, h2 = s[:halfway], s[halfway:]
                if h1 == h2:
                    invalid += int(s)
    return invalid


print(main())