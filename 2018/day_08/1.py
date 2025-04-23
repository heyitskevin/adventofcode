def readfile():
    with open('input.txt') as f:
        return [int(x) for x in f.read().strip().split()]
    

def main():
    d = readfile()
    metadata = 0
    def recur():
        # We could probably compartmentalize this better than using the nonlocal keyword but I wanted to try it out
        nonlocal d
        nonlocal metadata
        children, m_blocks = d[:2]
        rest = d[2:]
        d = rest
        for c in range(children):
            recur()
        metadata += sum(d[:m_blocks])
        d = d[m_blocks:]
    recur()
    return metadata
    

print(main())