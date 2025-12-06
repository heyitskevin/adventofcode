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
            for step_size in range(1, len(s) // 2 + 1):
                chunks = []
                for i in range(0, len(s), step_size):
                    chunks.append(s[i:i+step_size])
                elems = set(chunks)
                if len(elems) == 1:
                    invalid += int(s)
                    break
            
    return invalid


print(main())