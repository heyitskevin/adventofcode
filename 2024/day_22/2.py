from collections import defaultdict

def readfile():
    with open('input.txt') as f:
        return [int(x) for x in f.read().split('\n')]
    

def do_op(n):
    x = n
    ones = []
    # Problem states 2000 changes AFTER the first one so run 2001 times
    for s in range(2001):
        ones.append(int(str(x)[-1]))
        m = x * 64
        x = m ^ x
        x =  x % 16777216

        d = x // 32
        x = d ^ x
        x = x % 16777216

        t = x * 2048
        x = t ^ x
        x = x % 16777216
    return x, ones


def main():
    d = readfile()
    lookup = defaultdict(list)
    
    for c in d:
        x, ones, = do_op(c)
        
        temp = {}
        for ix in range(4, len(ones)):
            seq = tuple(
                ones[ix - (dd - 1)] - ones[ix - dd] for dd in range(4, 0, -1)
            )
            assert len(seq) == 4
            if seq not in temp:
                temp[seq] = ones[ix]
        for k, v in temp.items():
            lookup[k].append(v)
    
    return max([sum(vx) for vx in lookup.values()])


print(main())
